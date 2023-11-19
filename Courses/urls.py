from django.urls import path
from . import views

app_name = 'linc'
urlpatterns = [
    path('', views.home, name='home'),
    path('course-details', views.course_details, name='courses_details'),
    path('gallery', views.gallery, name='gallery'),
    path('events', views.events, name='events'),
    path('about', views.about, name='about'),
]