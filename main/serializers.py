from rest_framework import serializers
from .models import *

#serializers for the api

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

class ChapterSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

#course-based serializer
class CoursePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = [
            "id",
            "name",
        ]

class ChapterPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = [
            "id",
            "name",
            "slug",
        ]

class SummaryPageSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)
    class Meta:
        model = Summary
        fields = [
            "id",
            "chapter",
            "body",
        ]