from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Amenitie, Housing, Style

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'app/index.html'

class FilterView(generic.TemplateView):
    template_name = 'app/filter.html'

class MapView(generic.TemplateView):
    template_name = 'app/map.html'