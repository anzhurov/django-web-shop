from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('all/', views.get_all_products),
    path('create/', views.create_new_product),
]
