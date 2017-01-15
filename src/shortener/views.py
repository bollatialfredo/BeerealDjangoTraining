from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def beereal_training_redirect_view(request, *args, **kwargs): #FBV function based view
    return HttpResponse('hello!')

class BeerealCBV(View): #class based view
    def get(self, reques, *args, **kwargs):
        return HttpResponse('Hello again!')
