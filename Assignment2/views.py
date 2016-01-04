from django.shortcuts import render

from form import *
from models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
# Create your views here.


def add_teacher(request):
    if request.method == 'POST':
        form = teachersform(request.POST)
        if form.is_valid():
            a = Teachers(first_name= form.cleaned_data["first_name"],
                        last_name = form.cleaned_data["last_name"],
                        office_details=form.cleaned_data["office_details"],
                        phone_number=form.cleaned_data["phone_number"],
                        email =form.cleaned_data["email"]
                             )
            a.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form = teachersform()
    return render_to_response('add_teacher.html',{'form':form},
                              RequestContext(request))

def add_student(request):
    if request.method == 'POST':
        form = studentsform(request.POST)
        if form.is_valid():
            b = Students(first_name= form.cleaned_data["first name"],
                        last_name = form.cleaned_data["last name"],
                         email =form.cleaned_data["email"])
            b.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form = studentsform()
    return render_to_response('add_student.html',{'form':form},
                            RequestContext(request))

def add_course(request):
    if request.method == 'POST':
        form = coursesform(request.POST)
        if form.is_valid():
            c = Courses(name= form.cleaned_data["name"],
                        code= form.cleaned_data["code"],
                        classroom= form.cleaned_data["classroom"],
                        times= form.cleaned_data["times"],
                        teacher= form.cleaned_data["teacher"],
                        students= form.cleaned_data["students"])
            c.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form = coursesform()
    return render_to_response('add_course.html',{'form':form},
                              RequestContext(request))

def all_teachers(request):
    return render_to_response('all_teachers.html',
    {'teacher_list': Teachers.objects.all()})

def all_courses(request):
    return render_to_response('all_courses.html',
    {'course_list': Courses.objects.all()})

def all_students(request):
    return render_to_response('all_students.html',
    {'student_list': Students.objects.all()})











