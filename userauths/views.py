from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from userauths.models import User
from userauths.forms import UserRegisterForm

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey {request.user.username}, you are already logged in")
        return redirect('students:student')   

    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hi {request.user.username}, your account has been created successfully.")
            return redirect('students:student')
    
    context = {'form': form}
    return render(request, 'userauths/sign-up.html', context)


def LoginView(request):
    if request.user.is_authenticated:
        return redirect('students:student')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are Logged In")
                return redirect('students:student')
            else:
                messages.error(request, 'Username or password does not exit.')
        
        except:
            messages.error(request, 'User does not exist')

    return HttpResponseRedirect("/")



def LogoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect("userauths:sign-up")