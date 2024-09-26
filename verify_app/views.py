from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, './base.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'ACCOUNT CREATED SUCCESSFULLY')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegistrationForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have been logged in successfully!')  
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form': form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request, './profile.html', {'user': request.user})
    else:
        return redirect('login')  

def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

def pass_change_1(request):
    if request.user.is_authenticated:  
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(user=request.user)
        
        return render(request, './pass_change_1.html', {'form': form})
    else:
        return redirect('login') 

def pass_change_2(request):
    if request.user.is_authenticated:  
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password was successfully updated! Please log in again.')
                return redirect('login') 
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = SetPasswordForm(user=request.user)
        
        return render(request, './pass_change_2.html', {'form': form})
    else:
        return redirect('login') 
