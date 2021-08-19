"""studentstudyportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from app1 import views

from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("dashbord/",views.dashbord),
    path("notes/",views.notes),
    path("homework/",views.homework),
    path("youtube/",views.youtube),
    path("todo/",views.todo),
    path("books/",views.books),
    path("dictionary/",views.dictionary),
    path("wiki/",views.wiki),
    path("conversion/",views.conversion),
    path("register/",views.register),
    path("delete/<int:id>",views.delNotes),
    path("notesshow/<int:id>",views.notesshow),
    path("homedel/<int:id>",views.homedel),
    path("deltodo/<int:id>",views.deltodo),
    path("todoup/<int:id>",views.todoup),
    path("accounts/",include("django.contrib.auth.urls")),
]
