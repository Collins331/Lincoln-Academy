from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'index.html')

def course_details(request):
    return render(request, 'course-details.html')


def gallery(request):
    return render(request, 'gallery.html')


def about(request):
    return render(request, 'about.html')


def events(request):
    return render(request, 'events.html')


def courses(request):
    return render(request, 'courses.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        msg = Contact(name=name, email=email, subject=subject, message=message)
        msg.save()
        messages.success(request, 'Your message has been sent successfully')
        return redirect('/')
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def event_details(request):
    return render(request, 'event-details.html')


def blog_home(request):
    return render(request, 'blog-home.html')



def blog_single(request):
    return render(request, 'blog-single.html')