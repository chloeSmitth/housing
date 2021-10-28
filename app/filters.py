import django_filters

from .models import *


class StyleFilter(django_filters.FilterSet):
    class Meta:
        model = Style
        fields = '__all__'