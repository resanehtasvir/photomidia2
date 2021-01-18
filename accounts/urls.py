from django.urls import path , include
from . import views

urlpatterns =[
    path('signup', views.account_view),
]
