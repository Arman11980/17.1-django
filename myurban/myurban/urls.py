from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test),
    path('class/', views.ShabClass.as_view()),
]
