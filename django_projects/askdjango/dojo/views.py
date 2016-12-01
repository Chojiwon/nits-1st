from django.http import HttpResponse
from django.shortcuts import render


def mysum(requst, numbers):
    result = sum(int(number) for number in numbers.split('/') if number)
    return HttpResponse(result)

