from django.db.models.expressions import OrderBy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .filters import StyleFilter

from .models import Amenitie, Housing, Style

# Home Page
class IndexView(generic.TemplateView):
    template_name = 'app/index.html'

# Filtering
def FilterView(request):
    #template_name = 'app/filter.html'
    
    style = Style.objects.all().order_by('name')
    names = Style.objects.values_list('name', flat=True)

    houses = Housing.objects.filter(name=names)
    myFilter = StyleFilter(request.GET, queryset=style)
    styles = myFilter.qs

    context = {'myFilter' : myFilter, 'styles':styles, 'houses':houses}


    return render(request, 'app/filter.html', context)

def PropertyView(request, name):
    property = Housing.objects.get(name=name)
    context = {'property':property}
    return render(request, 'app/property.html', context)


    

class FilterResultView(generic.TemplateView):
    template_name = 'app/filter_results.html'

class MapView(generic.TemplateView):
    template_name = 'app/map.html'

class AboutView(generic.TemplateView):
    template_name = 'app/about.html'
