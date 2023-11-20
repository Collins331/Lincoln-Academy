from django.shortcuts import render

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
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def event_details(request):
    return render(request, 'event-details.html')


def blog_home(request):
    return render(request, 'blog-home.html')



def blog_single(request):
    return render(request, 'blog-single.html')