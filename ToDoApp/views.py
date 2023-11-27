from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, ListView,TemplateView, CreateView, DeleteView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .models import ToTable
# Create your views here.

class HomePageView(LoginRequiredMixin, ListView):
    context_object_name = 'data'
    model = ToTable
    template_name = 'home.html'
    
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = context['data'].filter(userName = self.request.user)
        return context




    
    
class CreatePageView(LoginRequiredMixin, CreateView):
    template_name = 'add.html'
    model = ToTable
    fields = "__all__"
    #success_url = reverse_lazy('base:homePage')
    def post(self, request, *args, **kwargs):
        userName = request.user
        topic = self.request.POST['topic']
        desc = self.request.POST['description']
        data = ToTable(userName = userName, title = topic,description=desc)
        data.save()
        return redirect('tdo:homePage')
        #return super().post(request, *args, **kwargs) 



class DisplayPageView(LoginRequiredMixin, DetailView):
    model = ToTable
    template_name = 'display.html'
    context_object_name = 'data'




class DeleteDataView(LoginRequiredMixin, DeleteView):
    model = ToTable
    context_object_name = 'data'
    template_name = 'deleteConfirm.html'
    success_url = reverse_lazy('tdo:homePage')


