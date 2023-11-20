from django.urls import path
from . import views

app_name = 'linc'
urlpatterns = [
    path('', views.home, name='home'),
    path('course-details', views.course_details, name='course_details'),
    path('gallery', views.gallery, name='gallery'),
    path('events', views.events, name='events'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('event-details', views.event_details, name='event_details'),
    path('blog-home', views.blog_home, name='blog_home'),
    path('blog-single', views.blog_single, name='blog_single'),
]