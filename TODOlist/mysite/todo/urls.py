from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manouzduotys/', views.UzduotysListView.as_view(), name='manouzduotys'),
    path('manouzduotys/nauja/', views.UserUzduotisCreateView.as_view(), name='nauja'),
]