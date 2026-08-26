from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    course_topic = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return self.name