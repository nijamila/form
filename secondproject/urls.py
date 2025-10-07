"""
URL configuration for secondproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from fourthapp.views import *
from fifthapp.views import *
from sixthapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes', classes),
    path('major', major),
    path('cat', cat),
    path('hobby1', hobby1),
    path('hobby2', hobby2),
    path('hobby3', hobby3),
    path('car', car),
    path('spf', spf),
    path('lipstick', lipstick),
]
