from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Amenitie, Housing, Style

# Home Page
class IndexView(generic.TemplateView):
    template_name = 'app/index.html'

# Filtering
class FilterView(generic.TemplateView):
    template_name = 'app/filter.html'

class FilterResultView(generic.TemplateView):
    template_name = 'app/filter_results.html'

class MapView(generic.TemplateView):
    template_name = 'app/map.html'

class AboutView(generic.TemplateView):
    template_name = 'app/about.html'
