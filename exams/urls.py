from django.urls import path

from . import views

urlpatterns = [
    # ex: /exams/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /exams/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]