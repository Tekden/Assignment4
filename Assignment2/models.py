from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teachers(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    office_details=models.CharField(max_length=40)
    phone_number=models.CharField(max_length=20)
    email = models.EmailField()
    def __unicode__(self):
        return self.first_name


class Students(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    def __unicode__(self):
        return self.first_name


class Courses(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=15)
    classroom = models.CharField(max_length=15)
    times = models.DateTimeField()
    teacher = models.ForeignKey(Teachers)
    students =models.ManyToManyField(Students)
    def __unicode__(self):
        return self.name








