from django.urls import path
from .views import  HomePageView, CreatePageView, DeleteDataView, DisplayPageView

app_name = "tdo"

urlpatterns = [
    
     path('', HomePageView.as_view(), name='homePage'),
     path('add/', CreatePageView.as_view(), name='add'),
      path('detail/<int:pk>', DisplayPageView.as_view(), name='detail'),
     path('delete/<int:pk>',DeleteDataView.as_view(),name='delete'),

]