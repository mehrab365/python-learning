from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from posts.forms import PostForm
from django.db.transaction import commit
from django.http.response import HttpResponseRedirect
from django.contrib import messages
# from .forms import PostForm

# Create your views here.

def post_create(request):
    if request.method == 'POST':
        print request.POST.get('title')
        print request.POST.get('content')
    
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")
    context_data = {'form':form}
#     return HttpResponse("<h1>hello create</h1>")
    return render(request, 'post_forms.html', context_data)

def post_details(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context_data = {'title':instance.title, 'instance':instance}
    return render(request, 'post_details.html', context_data)
#     return HttpResponse("<h1>hello details</h1>")

def post_list(request):
    if request.user.is_authenticated():
        query_set = Post.objects.all()
        context_data = {'title': request.user.username, 'object_list' : query_set}
        
        return render(request, 'index.html', context_data)
    else:
        context_data = {'title':'List'}
        return render(request, 'index.html', context_data)
#     return HttpResponse("<h1>hello list</h1>")

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Failed to Update")
        
    context_data = {'title':instance.title, 'instance':instance, 'form':form}
    
    return render(request, 'post_forms.html', context_data)

def post_delete(request):
    return HttpResponse("<h1>hello delete</h1>")