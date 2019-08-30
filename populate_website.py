import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','GUFCWebsite.settings')

import django
django.setup()
from website.models import Report, News

def populate():
# First, we will create lists of dictionaries containing the pages
# we want to add into each category.
# Then we will create a dictionary of dictionaries for our categories.
# This might seem a little bit confusing, but it allows us to iterate
# through each data structure, and add the data to our models.
    date = "2000-01-01"

    match_reports = [
        {"title": "Good Win for 1s",
        "text":"Great performance for the lads with some cracking goals from C.Morgan, masterclass from the big man",
        "date": date},
        {"title":"1s in Unlucky Draw",
        "text":"Last minute equaliser doesn't do the boys justice in 8-8 draw",
        "date": date},
        {"title":"Tough Defeat for Firsts",
        "text":"1s surpringly lost their first game in 3 years in a narrow 1-0 defeat",
        "date": date},
        {"title": "Good Win for 2s",
        "text":"G. Kerr steals the show with a hat-trick of hat-tricks to win the game",
        "date": date},
        {"title": "2s in unlucky Draw",
        "text":"Drew the game, bit of a surprise but the ref was poor",
        "date": date},
        {"title":"Tough Defeat for Seconds",
        "text":"2s got beat, sure what can you do",
        "date": date} 
        ]
    
    club_news = [
        {"title": "GUFC win UEFA Gold Award",
        "text":"Title says it all really, Glasgow Uni FC representatives were present at the ceremony in Bern to receive the award",
        "date": date},
        {"title": "Quiz Night!",
        "text":"GUFC happy to announce that we will be hosting our first ever GUFC Past and Present Pub Quiz in Dram",
        "date": date},
        {"title":"Transfer News",
        "text":"Don't believe what you read in the papers, C. Morgan has reassured the club of his desire to stay amidst rumours linking the centre-half to Celtic",
        "date": date} 
        ]

    events = [
        {"title": "Quiz Night",
        "text":"GUFC happy to announce that we will be hosting our first ever GUFC Past and Present Pub Quiz in Dram",
        "date": date},
        {"title": "Blood Drive",
        "text":"Glasgow University FC are participating in the annual charity blood donation scheme",
        "date": date},
    ]

    news_cats = {"match_reports": {"reports": match_reports},
        "club_news": {"reports": club_news},
        "events": {"reports": events},}

# If you want to add more catergories or pages,
# add them to the dictionaries above.
# The code below goes through the cats dictionary, then adds each category,
# and then adds all the associated pages for that category.
# if you are using Python 2.x then use cats.iteritems() see
# http://docs.quantifiedcode.com/python-anti-patterns/readability/
# for more information about how to iterate over a dictionary properly.
    for cat, news_report in news_cats.items():
        news = add_news(cat)
        for r in news_report["reports"]:
            add_report(news, r["title"], r["text"], r["date"])
    
    # Print out the categories we have added.
    for n in News.objects.all():
        for r in Report.objects.filter(news_cat=n):
            print("- {0} - {1}".format(str(n), str(r)))

def add_report(news, title, text, date, views=0):
    r = Report.objects.get_or_create(news_cat=news, title=title)[0]
    r.text=text
    r.views=views
    r.date=date
    r.save()
    return r

def add_news(name, views=0):
    n = News.objects.get_or_create(name=name)[0]
    n.views = views
    n.save()
    return n

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()