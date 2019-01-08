from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    context_dict = {'boldmessage': "Ballin never stops"}

    return render(request, 'website/index.html', context = context_dict)

def club(request):
    
    context_dict = {}
    
    return render(request, 'website/club.html', context = context_dict)