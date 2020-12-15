from django.urls import path
from . import views 
urlpatterns=[
    path('',views.travel_views,name='travel_views'),
    path('form/', views.travel_form,name='travel_form'),
]