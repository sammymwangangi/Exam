from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('exams/', include('exams.urls')),
    path('students/', include('students.urls')),
    path('lecturers/', include('lecturers.urls')),
    path('admin/', admin.site.urls),
]
