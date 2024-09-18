from django.db import models

# Create your models here.
class Department(models.Model):
    dept=models.CharField(max_length=255)
class Batch(models.Model):
    bach=models.CharField(max_length=255)
class Teacher(models.Model):
    name=models.CharField(max_length=255)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
class Student(models.Model):
    sname=models.CharField(max_length=225)
    bach=models.ForeignKey(Batch,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)