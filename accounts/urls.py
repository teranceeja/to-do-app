from django.urls import path
from .views import LoginPageView, RegisterPageView, LogoutPageView

app_name = "acc"

urlpatterns = [
    
    

    path('/login/', LoginPageView.as_view(), name='login'),
    path('/register/', RegisterPageView.as_view(), name='register'),
    path('/logout/', LogoutPageView.as_view(), name='logout'),


   


    
]