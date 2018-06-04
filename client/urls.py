from django.conf.urls import url
from django.urls import path, register_converter
from . import converters, views

register_converter(converters.VersionStringConverter, 'version_string')

urlpatterns = [
    path('libraries', views.libraries),
    path('libraries/', views.libraries),
    path('library/<slug:name>', views.library),
    path('library/<slug:name>/', views.library),
    path('library/<slug:name>/<version_string:version_string>', views.library_version),
    path('library/<slug:name>/<version_string:version_string>/', views.library_version),
    path('library/<slug:name>/<version_string:version>/resource', views.library_resource),
    path('library/<slug:name>/<version_string:version>/resource/', views.library_resource),
]
