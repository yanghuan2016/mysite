from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    return render(request, 'index.html')

def calendar(request):
    return render(request, 'calendar.html')