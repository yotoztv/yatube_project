# from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Главная страница - qq_2444-2')


def group_posts(request, slug):
    return HttpResponse(f'Группа по {slug}')

