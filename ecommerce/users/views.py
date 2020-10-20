from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.generic import FormView, CreateView, TemplateView, DetailView

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.



class RegisterUserView(CreateView):
    """
    CreateView for Registering user/customer.
    """

    form_class = CustomUserCreationForm
    model = CustomUser
    template_name = 'users/register.html'
    success_url = '/login'

    def form_valid(self, form):
        user = form.save()
        user_name = form.cleaned_data.get('first_name')
        messages.success(self.request, f'{user_name} registered successfully!', extra_tags="alert alert-success alert-dismissible fade show")

        return super(RegisterUserView, self).form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags="alert alert-danger alert-dismissible fade show")

        return super(RegisterUserView, self).form_invalid(form)





def loginUser(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,  email=email, password=password)

        if user is not None:
            login(request, user)
            
            messages.success(request, f'Hello {email}!', extra_tags="alert alert-success alert-dismissible fade show")
            
            return redirect('home')


        else:
            messages.error(request, f'Username or password incorrect!', extra_tags="alert alert-danger alert-dismissible fade show")

    context = {}
    return render(request, 'users/login.html', context)


def logoutUser(request):

    user_name = f'{request.user.first_name} {request.user.last_name}'
    logout(request)

    messages.success(request, f'{user_name} logged out successfully!', extra_tags="alert alert-success alert-dismissible fade show")

    return redirect('login')