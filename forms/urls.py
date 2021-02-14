from django.urls import path, include
from django.conf.urls import url
from filemanager import path_end
from . import views

urlpatterns = [
    # path('', views.upload_file, name='index')
    # path('', views.FileFieldView.as_view(), name='index')
    url('' + path_end, views.filemanager_view, name='index')
]