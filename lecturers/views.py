from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Lecturer

class IndexView(generic.ListView):
    template_name = 'lectrures/index.html'
    context_object_name = 'latest_lecturer_list'

    def get_queryset(self):
        """Return the last five published lectrures."""
        return Lecturer.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Lecturer
    template_name = 'lectrures/detail.html'