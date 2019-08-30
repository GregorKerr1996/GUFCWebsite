from django.http import HttpResponse
from django.shortcuts import render
from website.models import News, Report
from website.forms import ReportForm

def index(request):

    reports = Report.objects.order_by("-views")[:5]
    context_dict = {"news_reports": reports}

    return render(request, 'website/index.html', context_dict)

def club(request):
    
    context_dict = {}
    
    return render(request, 'website/club.html', context = context_dict)

def show_news(request, news_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        news_cat = News.objects.get(slug=news_name_slug)
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        reports = Report.objects.filter(news_cat=news_cat)
        # Adds our results list to the template context under name pages.
        context_dict['reports'] = reports
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['news_cat'] = news_cat
    except News.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['news_cat'] = None
        context_dict['reports'] = None
    # Go render the response and return it to the client.
    return render(request, 'website/news.html', context_dict)

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

def events(request):

    events_list = Report.objects.filter(news_cat__name = "events")
    context_dict = {"events": events_list}

    return render(request, 'website/events.html', context_dict)

def club_news(request):
    
    news_list = Report.objects.filter(news_cat__name = "club_news")
    context_dict = {"news": news_list,}

    return render(request, 'website/club_news.html', context_dict)

def matchReports(request):
    
    news_list = Report.objects.filter(news_cat__name = "club_news")
    match_reports = Report.objects.filter(news_cat__name = "match_reports")
    context_dict = {"news": news_list, "match_reports": match_reports}

    return render(request, 'website/matchReports.html', context_dict)

def add_report(request):

    form = ReportForm()
    if request.method =="POST":
        form = ReportForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print(form.errors)
    
    context_dict = {"form": form}

    return render(request, "website/add_news.html", context_dict)


def club_captain(request):
    context_dict = {}

    return render(request, 'website/club_captain.html', context=context_dict)