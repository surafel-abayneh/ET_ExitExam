from django.shortcuts import render
from django.http import HttpResponse


def welcome (request):
    return  render(request,'welcome.html')

def register_user (request):
    return  render(request,'register_user.html')

def index (request):
    return  render(request,'index.html')