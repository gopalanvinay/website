from django.urls import path, include
from .views import home, resume, projects, contact, download

urlpatterns = [
    path('', home, name="home"),
    path('resume', resume, name="resume"),
    path('projects', projects, name="projects"),
    path('contact', contact, name="contact"),
    path('download', download, name="download"),
]