from django.shortcuts import render
from .models import Course, Lesson
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import generics
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):

     model = Course
     serializer_class = CourseSerializer
     queryset = Course.objects.all()


class LessonCreateApiView(generics.CreateAPIView):

    serializer_class = LessonSerializer


class LessonListApiView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateApiView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyApiView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()