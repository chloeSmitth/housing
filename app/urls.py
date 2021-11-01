from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view()),

    #Filter paths
    path('filter/', views.FilterView, name='filter'),
    path('filter/<str:name>', views.PropertyView, name='property'),
    path('filter_result/', views.FilterResultView.as_view(), name='filter_result'),

    #Map paths
    path('map/', views.MapView.as_view(), name='map'),

    #About
    path('about/', views.AboutView.as_view(), name='about'),
]