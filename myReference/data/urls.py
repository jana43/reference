from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('search', views.search , name = "search"),
    path('page/<slug:slug_text>/' , views.get_page , name = "show"),
    path('post/<slug:slug_text>/' , views.show , name = "show"),
    
] 