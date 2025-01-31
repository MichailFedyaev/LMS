from django.contrib import admin
from .models import Course, Lesson, CourseSubscription, CoursePayment
from django.apps import apps


app = apps.get_app_config("lms")

for model in app.models.values():
    admin.site.register(model)
