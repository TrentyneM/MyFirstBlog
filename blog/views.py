from django.shortcuts import render
from django.utils import timezone

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


