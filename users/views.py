from django.shortcuts import render,redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisteredUserForm

def register_