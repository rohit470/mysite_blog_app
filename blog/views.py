from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Rohit',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'July 1,2025',
    },
    {
        'author':'Rahul',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'July 2,2025',
    }
]

# Create your views here.
def home(request):
    context={'posts':posts}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
