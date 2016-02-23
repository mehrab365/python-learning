from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def post_create(request):
    return HttpResponse("<h1>hello create</h1>")

def post_details(request):
    context_data = {'title':'Details'}
    return render(request, 'index.html', context_data)
#     return HttpResponse("<h1>hello details</h1>")

def post_list(request):
    if request.user.is_authenticated():
        context_data = {'title': request.user.username}
        return render(request, 'index.html', context_data)
    else:
        context_data = {'title':'List'}
        return render(request, 'index.html', context_data)
#     return HttpResponse("<h1>hello list</h1>")

def post_update(request):
    return HttpResponse("<h1>hello update</h1>")

def post_delete(request):
    return HttpResponse("<h1>hello delete</h1>")