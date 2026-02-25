from django.shortcuts import render
from django.http import HttpResponse

counter_value = 0

def index(request):
    global counter_value
    return render(request, 'counter/index.html', {'counter': counter_value})

def increment(request):
    global counter_value
    counter_value += 1
    return HttpResponse(str(counter_value))

def decrement(request):
    global counter_value
    counter_value -= 1
    return HttpResponse(str(counter_value))

def reset(request):
    global counter_value
    counter_value = 0
    return HttpResponse(str(counter_value))
# Create your views here.
