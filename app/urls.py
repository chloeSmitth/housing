from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view()),
    path('filter/', views.FilterView.as_view(), name='filter'),
]