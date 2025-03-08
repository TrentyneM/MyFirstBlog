""" Here we're importing Django's function path and all of our views from the
blog application. (We don't have any yet, but we will get to that in a minute!
"""
from django.urls import path
from . import views

""" After that, we can add our first URL pattern. As you can see, we're now 
assigning a view called post_list to the root URL. 

The URL pattern will match an empty string an the Django URL resolver will 
ignore the domain name (i.e., http://127.0.0.1:8000/) that prefixes the full URL
path. 

This pattern will tell Django that views.post_list is the right place to go if 
someone enters your website at the 'http://127.0.0.1:8000' address.
"""
urlpatterns = [

    # The last part, name='post_list', is the name of the URL that will be used
    # to identify the view. This can be the same as the name of the view but it can
    # also be something completely different. 

    # We will be using the named URLs later in the project, so it is important to name
    # each URL in the app, and keep it unique and easy to remember.
    path('', views.post_list, name='post_list'),

    # This part post/<int:pk>/ specifies a URL pattern – we will explain it for you:

    # post/ means that the URL should begin with the word post followed by a /. So far so good.

    # <int:pk> – this part is trickier. It means that Django expects an integer value 
    # and will transfer it to a view as a variable called pk.

    # / - then we need a / again before finishing the URL.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish')
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
]
