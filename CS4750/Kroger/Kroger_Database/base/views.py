# from django.shortcuts import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the  base index.")
# # Create your views here.

from django.shortcuts import render, redirect
from .models import Member
 
# Create your views here.
def index(request):
    members = Member.objects.all()
    return render(request, 'blog/index.html', {'members': members})
 
  
