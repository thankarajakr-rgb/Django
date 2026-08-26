from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# =========================================================
# HOME PAGE
# =========================================================

def home(request):
    return render(request, 'myapp/home.html')


# =========================================================
# LOGIN / INDEX PAGE
# =========================================================

def index(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "Thankaraja" and password == "123":

            return redirect('about')

        else:

            return render( request,'myapp/index.html',{'error': 'Invalid Credentials'})

    return render(request, 'myapp/index.html')


# =========================================================
# ABOUT PAGE
# =========================================================

def about(request):

    return render(request,'myapp/about.html')


# =========================================================
# TABLE PAGE
# =========================================================

def table(request):

    student_details = [
        {
            "id": 1,
            "name": "Raja",
            "age": 29
        },
        {
            "id": 2,
            "name": "Thankaraja",
            "age": 29
        },
        {
            "id": 3,
            "name": "Deepi",
            "age": 29
        }
    ]

    return render(request,'myapp/table.html',{'student': student_details})


# =========================================================
# STUDENT HTML PAGE
# =========================================================

def student_page(request):

    if request.method == "POST":

        name = request.POST.get('name')
        age = request.POST.get('age')
        course_id = request.POST.get('course')

        course = Course.objects.get(id=course_id)

        Student.objects.create(
            name=name,
            age=age,
            course=course
        )

        return redirect('student')


    students = Student.objects.all()
    courses = Course.objects.all()

    return render(request,'myapp/student.html',{
            'students': students,
            'courses': courses
        }
    )

# =========================================================
# STUDENT HTML UPDATE
# =========================================================

def update(request, id):

    student = Student.objects.get(id=id)
    courses = Course.objects.all()

    if request.method == "POST":

        student.name = request.POST.get('name')
        student.age = request.POST.get('age')

        course_id = request.POST.get('course')

        student.course = Course.objects.get(
            id=course_id
        )

        student.save()

        return redirect('student')


    return render(request,'myapp/update.html',
        {
            'student': student,
            'courses': courses
        }
    )


# =========================================================
# STUDENT HTML DELETE
# =========================================================

def delete(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('student')


# =========================================================
# COURSE HTML PAGE
# =========================================================

def course_page(request):

    courses = Course.objects.all()

    return render(request,'myapp/course.html',
        {
            'courses': courses
        }
    )


# =========================================================
# COURSE API - GET + POST
# =========================================================

@api_view(['GET', 'POST'])
def course_api(request):

    # GET
    if request.method == "GET":

        courses = Course.objects.all()

        serializer = CourseSerializer(
            courses,
            many=True
        )

        return Response(serializer.data,status=status.HTTP_200_OK)


    # POST
    if request.method == "POST":

        serializer = CourseSerializer( data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# =========================================================
# COURSE API - PUT + DELETE
# =========================================================

@api_view(['GET', 'PUT', 'DELETE'])
def course_detail_api(request, id):

    try:

        course = Course.objects.get(id=id)

    except Course.DoesNotExist:

        return Response({"message": "Course Not Found"},status=status.HTTP_404_NOT_FOUND)


    # GET SINGLE COURSE
    if request.method == "GET":

        serializer = CourseSerializer(course)

        return Response(serializer.data,status=status.HTTP_200_OK)


    # PUT
    if request.method == "PUT":

        serializer = CourseSerializer(course,data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    # DELETE
    if request.method == "DELETE":

        course.delete()

        return Response({"message": "Course Deleted Successfully"},status=status.HTTP_200_OK)


# =========================================================
# STUDENT API - GET + POST
# =========================================================

@api_view(['GET', 'POST'])
def student_api(request):

    # GET ALL STUDENTS
    if request.method == "GET":

        students = Student.objects.all()

        serializer = StudentSerializer(students,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


    # POST STUDENT
    if request.method == "POST":

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# =========================================================
# STUDENT API - GET + PUT + DELETE
# =========================================================

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_api(request, id):

    try:

        student = Student.objects.get(id=id)

    except Student.DoesNotExist:

        return Response({"message": "Student Not Found"},status=status.HTTP_404_NOT_FOUND)


    # GET SINGLE STUDENT
    if request.method == "GET":

        serializer = StudentSerializer(student)

        return Response(serializer.data,status=status.HTTP_200_OK)


    # PUT
    if request.method == "PUT":

        serializer = StudentSerializer(student,data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    # DELETE
    if request.method == "DELETE":

        student.delete()

        return Response({"message": "Student Deleted Successfully"},status=status.HTTP_200_OK)