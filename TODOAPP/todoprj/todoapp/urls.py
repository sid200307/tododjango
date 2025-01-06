from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),  # Maps the root URL to the `home` view
    path('register/', views.register, name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('login/', views.loginpage, name='loginpage'),
    path('delete/<str:name>/', views.deleteTask, name='deleteTask'),
    path('update/<str:name> ',views.Update,name='update'),

]
