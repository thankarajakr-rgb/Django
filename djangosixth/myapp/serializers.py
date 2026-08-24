from rest_framework import serializers
from .models import Studentnew

class Student_serializer(serializers.ModelSerializer):

    class Meta:

        model = Studentnew
        fields = '__all__'
