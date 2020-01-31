from django.urls import path

from . import views

urlpatterns = [
    # ex: /lecturer/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /lecturer/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]