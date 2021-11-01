import django_filters
from django_filters import NumberFilter, CharFilter

from .models import *


class StyleFilter(django_filters.FilterSet):
    rent_max = NumberFilter(field_name = 'rent', lookup_expr = 'lt')
    
    class Meta:
        model = Style
        fields = '__all__'
        exclude = ['name', 'rent']