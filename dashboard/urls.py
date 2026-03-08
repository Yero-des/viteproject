from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name="index"),
    path('greeting/create/', views.GreetingCreateView.as_view(), name="greeting_create")
]
