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


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students:student')
    else:
        form = StudentForm()
    
    return render(request, 'students/add_student.html', {'form': form})