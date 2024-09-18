from django.contrib import admin
from . models import *

# Register your models here.
class Student_display(admin.ModelAdmin):
    list_display=['name']
class Teacher_display(admin.ModelAdmin):
    list_display=['name']    

admin.site.register(Student,Student_display)
admin.site.register(Teacher,Teacher_display)