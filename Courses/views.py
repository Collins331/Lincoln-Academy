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