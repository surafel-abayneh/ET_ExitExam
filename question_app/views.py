from django.shortcuts import render
from django.http import HttpResponse

from question_app.forms import UserForm

def welcome (request):
    return  render(request,'welcome.html')

def register_user (request):
    return  render(request,'register_user.html')

def index (request):
    return  render(request,'index.html')

def cs_courses (request):
    return  render(request,'cs_courses.html')

def questions (request):
    return  render(request,'questions.html')
 
def register_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return  render(request,'register_user.html',context)
