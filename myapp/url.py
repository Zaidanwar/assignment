from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home.as_view(),name="home"),
path('register/',Register1.as_view(),name="register"),
]