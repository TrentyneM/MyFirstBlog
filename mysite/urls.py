"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # This is the URL for our admin panel site.
    path('admin/', admin.site.urls),

    # Everything that comes into http://127.0.0.1:8000/
    # to be the home page of our blog and to display a list of posts.

    # To keep the urls.py file clean, we will import URLs from our blog
    # application to the main urls.py file.
    path('', include('blog.urls')),

    
]
