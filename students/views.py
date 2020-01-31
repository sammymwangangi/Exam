from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Student

class IndexView(generic.ListView):
    template_name = 'students/index.html'
    context_object_name = 'latest_student_list'

    def get_queryset(self):
        """Return the last five published students."""
        return Student.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'