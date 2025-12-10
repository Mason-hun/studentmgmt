from django.contrib import admin
from django.urls import path, include
from student_mgmt_system import views   # global views (home, dashboard)

urlpatterns = [
    # Global routes
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Feature apps
    path('students/', include('students.urls')),
    path('assignments/', include('assignments.urls')),
    path('submissions/', include('submissions.urls')),
    path('reminders/', include('reminders.urls')),

    # Authentication
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # This automatically provides login, logout, password reset routes
]