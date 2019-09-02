from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from .models import Apply
import bcrypt
from .forms import ApplForm


def index(request):
    return render(request, 'register/index.html')

def logagain(request):
    return render(request, 'register/index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf8'), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        hashed_password = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())
        if (bcrypt.checkpw( user.password.encode('utf8'),hashed_password)):
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)

def home(request):
    return render(request , 'homepage.html')

def logout(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'logout.html', context)

def apply(request):
   return render(request, 'apply.html')

def admincheck(request):
	if request.method=="POST":
		uid=request.POST.get('userid')
		upass=request.POST.get('pswrd')
		d = 0
		if uid=="hr@reach-tech.com" and upass=="reachtechnologies123":
			d=1
		if d==1:
			return render(request,'admindash.html')
		else:
			return render(request,'admin.html')

def adminpage(request):

        user = Apply.objects.create(first_name=request.POST.get['first_name'], last_name=request.POST.get['last_name'], email=request.POST.get['email'], phone=request.POST.get['phone'], city=request.POST.get['city'], state=request.POST.get['state'], zip=request.POST.get['zip'])
        user.save()
        request.session['id'] = user.id
        return redirect('/homepage')

def get(self , request):
        post = Post.objects.all()
        args = {'posts' : posts}
        return render(request ,self.template_name ,args)
