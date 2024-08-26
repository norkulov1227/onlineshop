from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from apps.accounts.form import UserForm
# Create your views here.

class TestView(TemplateView):
    template_name = 'test-index.html'

class HomeView(TemplateView):
    template_name = 'index.html'

class LoginView(View):
    def get(self, request):
        return render(request, 'page-login.html')
    
    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(phone = phone, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('products:home')
        messages.error(request, "Phone or password entered incorrectly")
        return render(request, 'page-login.html')

class PrivacyPolicyView(TemplateView):
    template_name = 'page-privacy-policy.html'
class LogoutView(View):
    def get(self, request):
        return render(request, 'confirm-logout.html')
    def post(self, request):
        logout(request)
        messages.warning(request, "Successfully Logged Out!")
        return redirect('products:home')

class SignUpView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'page-register.html', {'form' : form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Siz tizimdan muvaffaqiyatli ro'yxatdan o'tdingiz. Iltimos tizimga qayta kiring!")
            return redirect('login')
        return render(request, 'page-register.html', {'form' : form})
