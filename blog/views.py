from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# We're going to include the model we have written in models.py
from .models import Post

# The dot before models means current directory or current
# application. Both views.py and models.py are in the same directory.
# This means we can use . and the name of the file (without .py). Then we
# import the name of the model (Post).

# As you can see, we created a function (def) called post_list
# that takes request and will return the value it gets from calling
# another function render that will render (put together) our template
# blog/post_list.html.
def post_list(request):

    # This lets us filter posts by time and published date.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # In the render function we have on parameter request (everything we
    # recieve from the user via the internet) and another giving the template
    # file ('blog/post_list.html'). The last parameter, {}, is a place in which
    # we can add some things for the template to use. We need to give them names
    # (we will stick to 'posts' right now :) )
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
    return redirect('post_list')
