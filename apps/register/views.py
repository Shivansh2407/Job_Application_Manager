from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User , Student
from .forms import UserForm , StudentForm
import bcrypt


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

def get(self , request):
        post = Post.objects.all()
        args = {'posts' : posts}
        return render(request ,self.template_name ,args)


def register_stud(request):
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        user_form    = UserForm(request.POST)
        student_form = StudentForm(request.POST, request.FILES)


        if user_form.is_valid() and student_form.is_valid():
            try:
                user = user_form.save()
                # user.username(label_tag='roll_no')
                # using set_password method, hash the password
                user.is_active = False
                user.set_password(user.password)
                user.save()

                # Since we need to set the user attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.

                student  = student_form.save(commit = False)
                student.roll_no = user
                student.save()
                registered = True

                return HttpResponseRedirect('/')
            except:
                pass

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        student_form = StudentForm()


    return render(request,'register.html', {
        'user_form' : user_form,
        'student_form' : student_form,
        'registered': registered,
    })

def show_students(request):
    changer = []
    student_list = Student.objects.all()
    for i in student_list:
        user = Student.objects.get(roll_no = i.roll_no)
        changer.append([user, i])

    return render(request, 'show_students.html', {'students': changer,})
