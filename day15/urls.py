"""day15 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^publisher_list/', views.publisher_list),
    # url(r'^publisher_add/', views.publisher_add),
    # url(r'^publisher_del/', views.publisher_del),
    # url(r'^publisher_edit/', views.publisher_edit),
    # url(r'^login/', views.login),
    # url(r'^index/', views.index),
    # url(r'^register/', views.register),
    url(r'app01/',include('app01.urls')),
    url(r'app02/',include('app02.urls')),
]
