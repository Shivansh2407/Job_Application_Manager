
from __future__ import unicode_literals
from .models import Student
from django.contrib import admin
from django.contrib.auth.models import Group, User

admin.site.register(Student)
admin.site.site_header='Hostel Management Dashboard'
