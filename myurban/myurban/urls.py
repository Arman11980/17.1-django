from django.contrib import admin
from django.urls import path
# from task2.views import func_template, ClassTemplate
# from task3.views import home_page, game_page, cart_page
from task4.views import home_page, game_page, cart_page

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', func_template),
#     path('page2/', ClassTemplate.as_view())
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('page1/', game_page),
    path('page2/', cart_page),
]
