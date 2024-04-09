from  django.views.generic import ListView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User,Course

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



def check_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            # If email exists, redirect to home page
            return redirect('index') 
        else:
            # If email does not exist, proceed with registration
           return redirect('register_user') 
    else:
        # If not a POST request, render a form for email input
        return render(request, 'email_check.html')
     

class CourseListView(ListView):
    model = Course
    template_name = 'cs_courses.html'
    

def course_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'mcq.html',{'obj':course})