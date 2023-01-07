from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login-register"),
    path('logout/', views.logoutPage, name="logout"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
]