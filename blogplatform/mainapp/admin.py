from django.contrib import admin
from .models import Attendee, Category, Event, Post, Comment

admin.site.register(Attendee)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)
