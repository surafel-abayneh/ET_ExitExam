"""
URL configuration for ExitExam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 
from django.urls import path
from .import views 
 




urlpatterns = [
    
    path('', views.welcome),
    path('register_user/', views.register_user , name ='register_user'),
    path('index/', views.index,name='index'),
    path('cs_courses/', views.list_courses,name='cs_course'),
    path('questions/', views.questions,name='questions'),
    path('check_email/', views.check_email,name='check_email'),
    path('<int:pk>/', views.topic_list,name='topic_list'),
    path('departments/', views.department_list, name='department_list'),
    path('courses/<int:department_id>/', views.course_list, name='course_list'), 
    path('topic/<int:topic_id>/', views.topic_questions, name='topic_questions'),
    path('course/<int:course_id>/', views.course_topics, name='course_topics'),
    path('topic/<int:topic_id>/', views.topic_questions, name='topic_questions'),
   
]
