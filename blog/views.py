from django.shortcuts import render

posts=[
    {
        'title':'Blog Post 1',
        'author':'CoreyMS',
        'content':'First post content',
        'date_posted':'July 11, 2023'
    },
    {
        'title':'Blog Post 2',
        'author':'Priyanshu Naskar',
        'content':'Seconf post content',
        'date_posted':'July 11, 2023'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html',context={'title':'About'})
