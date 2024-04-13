from  django.views.generic import ListView
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse
from .forms import UserForm
from .models import User,Course,Department,Topic,Question
 






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

def  topic_list(request ,pk):
    courses= get_object_or_404(Course, pk=pk)
    return HttpResponse(courses)

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

def list_courses(request):
    courses= Course.objects.all()
    context={
       'courses' : courses, 
    }
 
    return render(request,'cs_courses.html',context)


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def course_list(request, department_id):
    department = Department.objects.get(pk=department_id)
    courses = department.course_set.all()
    return render(request, 'course_list.html', {'department': department, 'courses': courses})

def course_topics(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    topics = course.topic_set.all()
    return render(request, 'course_topics.html', {'course': course, 'topics': topics})

def topic_questions(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    questions = topic.question_set.all()
    return render(request, 'topic_questions.html', {'topic': topic, 'questions': questions})