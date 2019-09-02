from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    join_year     = models.IntegerField(default=2016)
    GENDER_CHOICES=[
        ('male', 'Male'),
        ('female', 'Female')
    ]
    gender        = models.CharField(choices=GENDER_CHOICES, default='male',max_length = 6)
    father_name   =  models.CharField(max_length = 200, null=True)
    date_of_birth =  models.DateField(null =True, blank = True)
    fee_receipt   =  models.FileField(upload_to='receipt/', null=True)
    address       =  models.CharField(max_length = 100,null =True)
    city          =  models.CharField(max_length = 100,null =True)
    state         =  models.CharField(max_length = 100,null =True)
    pincode       = models.IntegerField(default=382009)
    roll_no       = models.CharField(max_length = 10, primary_key =True,unique = True )
    def __str__(self):
        return str(self.roll_no)


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

STATE_CHOICES = (
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadar and Nagar Haveli','Dadar and Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Lakshadeep','Lakshadeep'),
    ('Pondicherry', 'Pondicherry'),
    ('Andra Pradesh','Andra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madya Pradesh','Madya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Orissa', 'Orissa'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telagana', 'Telagana'),
    ('Tripura','Tripura'),
    ('Uttaranchal','Uttaranchal'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
)
class Apply(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(choices=STATE_CHOICES, default='Uttar Pradesh' ,max_length=255)
    zip = models.IntegerField()


