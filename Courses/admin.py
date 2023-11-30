from django.contrib import admin
from . models import Contact, Profile, Courses, Event, User, Review
# Register your models here.

admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Courses)
admin.site.register(Event)
admin.site.register(Review)
