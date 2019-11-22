from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^publisher_list/', views.publisher_list,name='publisher'),
    url(r'^publisher_add/', views.Publishadd.as_view(),name='pub-add'),
    url(r'^publisher_del/(?P<pk>\d+)$', views.publisher_del,name='pub-del'),
    url(r'^publisher_edit/(?P<pk>\d+)$', views.publisher_edit,name='pub-edit'),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^register/', views.register,name='register'),
    url(r'^book/$', views.book_list,name='book'),
    url(r'^book/add/$', views.BookAdd.as_view(),name='book_add'),
    url(r'^book/edit/(\d+)$', views.BookEdit.as_view(),name='book_edit'),
    url(r'^(\w+)/del/(\d+)$', views.delete,name='del'),
    url(r'^author/$', views.author_list,name='author'),
    url(r'^author/add/$', views.author_add,name='author_add'),
    url(r'^author/edit/(\d+)$', views.author_edit,name='author_edit'),
]
