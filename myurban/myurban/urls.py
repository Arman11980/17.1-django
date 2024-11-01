from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from task3.views import main_page, shop_page, bin_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('shop/', shop_page),
    path('bin/', bin_page),
]
