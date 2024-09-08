from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('', views.student, name='student'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
]