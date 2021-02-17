import random
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')

def dinner(request):
    menus = ['찜닭', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {
        'pick': pick,
    }
    return render(request, 'articles/dinner.html', context)

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)

def dtl_practice(request):
    menus = ['짜장면', '짬뽕', '탕수육']
    empty_list = []
    context = {
        'menus': menus,
        'empty_list': empty_list,
    }
    return render(request, 'articles/dtl_practice.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)