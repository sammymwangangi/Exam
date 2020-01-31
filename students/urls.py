from django.urls import path

from . import views

urlpatterns = [
    # ex: /students/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /students/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]