from django.contrib import admin
from django.urls import path, re_path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('city/', views.Cities_list.as_view()),
    path('city/<int:city_id>/street/', views.City_streets_list.as_view()),
    path('shop/', views.Shops_list.as_view())
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)