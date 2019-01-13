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


def teamProfiles(request):
    context_dict = {}

    return render(request, 'website/teamProfiles.html', context=context_dict)



def firstTeam(request):
    context_dict = {}

    return render(request, 'website/firstTeam.html', context=context_dict)

def secondTeam(request):
    context_dict = {}

    return render(request, 'website/secondTeam.html', context=context_dict)

def thirdTeam(request):
    context_dict = {}

    return render(request, 'website/thirdTeam.html', context=context_dict)

def underTwentyOnes(request):
    context_dict = {}

    return render(request, 'website/underTwentyOnes.html', context=context_dict)

def matchReports(request):
    context_dict = {}

    return render(request, 'website/matchReports.html', context=context_dict)