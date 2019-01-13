from django.http import HttpResponse
from django.shortcuts import render
from website.models import MatchReport

def index(request):

    match_report_list = MatchReport.objects.order_by("-views")[:5]
    context_dict = {'boldmessage': "Ballin never stops", "matchReports": match_report_list}

    return render(request, 'website/index.html', context_dict)

def club(request):
    
    context_dict = {}
    
    return render(request, 'website/club.html', context = context_dict)