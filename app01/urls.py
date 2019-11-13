from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^publisher_list/', views.publisher_list,name='pub'),
    url(r'^publisher_add/', views.Publishadd.as_view(),name='pub-add'),
    url(r'^publisher_del/(?P<pk>\d+)$', views.publisher_del,name='pub-del'),
    url(r'^publisher_edit/(?P<pk>\d+)$', views.publisher_edit,name='pub-edit'),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^register/', views.register,name='register'),
]
