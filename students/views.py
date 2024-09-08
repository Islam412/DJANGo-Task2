from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student(request):
    query = request.GET.get('search', '')
    students = Student.objects.filter(
        first_name__icontains=query
    ) | Student.objects.filter(
        last_name__icontains=query
    ) | Student.objects.filter(
        age__icontains=query
    )
    context = {
        'students': students,
        'query': query
    }
    return render(request, 'students/home.html', context)