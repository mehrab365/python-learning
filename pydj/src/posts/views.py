from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from posts.forms import PostForm
from django.db.transaction import commit
# from .forms import PostForm

# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
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

def post_update(request):
    return HttpResponse("<h1>hello update</h1>")

def post_delete(request):
    return HttpResponse("<h1>hello delete</h1>")