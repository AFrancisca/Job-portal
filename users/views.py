from django.shortcuts import render,redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisteredUserForm
from resume.models import Resume
from company.models import Company

#REGISTER APPLICANT
def register_applicant(request):
    if request.method == 'POST':
        form = RegisteredUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit = False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Company.objects.create(User=var)
            messages.info(request,'Your account has been created.')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('register-applicant')
    else:
        form= RegisteredUserForm()
        context = {'form': form}
        return render(request,'users/register_applicant.html', context)

# REGISTER RECRUITER
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisteredUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit = False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Resume.objects.create(User=var)
            messages.info(request,'Your account has been created.')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('register-recruiter')
    else:
        form= RegisteredUserForm()
        context = {'form': form}
        return render(request,'users/register_recruiter.html', context)
    
# LOGIN A USER

def login_user(request):
    if request.method== 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, userame=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if request.user.is_applicant:
                return redirect('applicant-dashboard')
            elif request.user.is_recruiter:
                return redirect('recruiter-dashboard')
            else:
                return redirect('login')
        else:
            messages.warning(request,'users/login.html')
           

# LOGOUT A USER             
            
