from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('city/', views.Cities_list.as_view()),
    path('city/<int:city_id>/street/', views.City_streets_list.as_view()),
    path('shop/', views.Shops_list.as_view())
]
