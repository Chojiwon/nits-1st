from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    pass


def mysum(requst, numbers):
    result = sum(int(number) for number in numbers.split('/') if number)
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}이시네요.'.format(name, age))

