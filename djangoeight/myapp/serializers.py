from rest_framework import serializers
from .models import Student, Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    course_details = CourseSerializer(
        source='course',
        read_only=True
    )

    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'age',
            'course',
            'course_details'
        ]