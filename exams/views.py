from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Exam

class IndexView(generic.ListView):
    template_name = 'exams/index.html'
    context_object_name = 'latest_exam_list'

    def get_queryset(self):
        """Return the last five published exams."""
        return Exam.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Exam
    template_name = 'exams/detail.html'