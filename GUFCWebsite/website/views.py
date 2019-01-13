from django.http import HttpResponse
from django.shortcuts import render
from website.models import News, Report

def index(request):

    news_cat_list = News.objects.order_by("-views")[:5]
    context_dict = {'boldmessage': "Ballin never stops", "news_cats": news_cat_list}

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