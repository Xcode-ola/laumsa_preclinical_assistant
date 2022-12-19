from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class Course_List_View(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursePageSerializer
    permission_classes = [permissions.AllowAny]

class Chapter_List_View(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None, **kwargs):
        chapters = Chapters.objects.filter(course__name = kwargs["name"])
        serializer = ChapterPageSerializer(chapters, many=True)
        return Response(serializer.data)