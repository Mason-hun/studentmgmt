from django.urls import path
from . import views

urlpatterns = [
    path('', views.submission_list, name='submission_list'),
    path('add/', views.add_submission, name='add_submission'),
    path('edit/<int:pk>/', views.edit_submission, name='edit_submission'),
    path('delete/<int:pk>/', views.delete_submission, name='delete_submission'),
]