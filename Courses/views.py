from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Contact, Courses, Profile, Blog, Event, Review
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm

# Create your views here.
def home(request):
    data = Courses.objects.all()
    event = Event.objects.all()
    review =Review.objects.all()
    return render(request, 'index.html', {'data': data, 'event': event, 'review': review})

def course_details(request):
    return render(request, 'course-details.html')


def gallery(request):
    return render(request, 'gallery.html')


def about(request):
    return render(request, 'about.html')


def events(request):
    event = Event.objects.all()
    return render(request, 'events.html', {'data': event})

def addevent(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['phone']
        title = request.POST['title']
        link = request.POST['link']
        date = request.POST['date']
        detail = request.POST['detail']
        image = request.FILES['img']

        evt = Event(name=name, phone_number=number, title=title, link=link, date=date, detail=detail, poster=image)
        evt.save()
        messages.success(request, 'Event added successfully!')
        return redirect('/')
    return render(request, 'addevent.html')


def courses(request):
    student = Courses.objects.all()
    # paginator = Paginator(Courses.objects.all(), 5)
    # new_page = request.GET.get('page')
    # student = paginator.get_page(new_page)
    return render(request, 'courses.html', {'item': student})


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






def join(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='linc:users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
