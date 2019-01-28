from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#This is blog views

posts = [
        {
        'author':'Kshitij',
        'title':'First Blog Post',
        'content':'This is the content of my first post',
        'date_posted':'22 Jan 2019'
        },
        {
        'author':'Siddhesh',
        'title':'Second Blog Post',
        'content':'This is the content of Siddheshs first post',
        'date_posted':'22 Jan 2019'
        }
        ]

def home(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>This is the blog home</h1>')
    return render(request,'blog/home.html',context)
    #Here we are returning template instead of HTTP Response

def about(request):
    #return HttpResponse('<h1>This is the blog about</h1>')
    return render(request,'blog/about.html')

