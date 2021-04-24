from django.shortcuts import render

from django.http import HttpResponse

def index(request)
  return HttpResponse("仮トップページ")

def index(request):
  return render(request, "kanban/index.html")

def home(request):
  return render(request, "kanban/home.html")