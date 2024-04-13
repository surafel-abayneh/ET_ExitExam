from django.db import models
from django import forms
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128,default='0000')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name+" "+self.last_name
    


class Department(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images',null=True) 
    created_at= models.DateTimeField(auto_now_add=True,null=True )
    updated_at= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images',null=True) 
    created_at= models.DateTimeField(auto_now_add=True,null=True )
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def get_topic(self):
        return self.topic_set.all() 


 
 

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    key_points = models.TextField(max_length=1000,default='Default key points')
    created_at= models.DateTimeField(auto_now_add=True,null=True )
    updated_at= models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"course: {self.course.name}, topic: {self.name}"
 



class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    explanation = models.TextField(blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True,null=True )
    updated_at= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text
    
    def get_answer(self):
        return self.answer_set.all() 


 

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True,null=True )
    updated_at= models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"question:{self.question.text}, answer:{self.choice_text},correct: {self.correct},explanation: {self.question.explanation}" 

    



