from django.conf.urls import url
from app02 import views
urlpatterns = [
    url(r're/',views.re),
    url(r'file_upload/',views.file_upload),

]