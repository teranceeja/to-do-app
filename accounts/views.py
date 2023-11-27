from django.shortcuts import render, redirect


from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, ListView,TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth.models import User

# Create your views here.


    
    


class LoginPageView(LoginView):
    template_name = 'login.html'


    def post(self, request, *args, **kwargs):
        username = self.request.POST['uName']
        password = self.request.POST['pWord']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('tdo:homePage')
    
    
    

class RegisterPageView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    

    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        firstName = self.request.POST['firstName']
        lastName = self.request.POST['lastName']
        email = self.request.POST['email']
        password = self.request.POST['password']
        user = User.objects.create_user(username=username, first_name=firstName, last_name=lastName, email=email ,password=password)
        user.save()
        return redirect('acc:login')
    

class LogoutPageView(LoginRequiredMixin, LogoutView):
    next_page = 'acc:login'




