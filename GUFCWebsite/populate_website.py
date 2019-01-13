import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','GUFCWebsite.settings')

import django
django.setup()
from website.models import MatchReport, Report, News

def populate():
# First, we will create lists of dictionaries containing the pages
# we want to add into each category.
# Then we will create a dictionary of dictionaries for our categories.
# This might seem a little bit confusing, but it allows us to iterate
# through each data structure, and add the data to our models.
    reports_1st = [
        {"title": "Good Win for 1s",
        "text":"Great performance for the lads with some cracking goals from C.Morgan, masterclass from the big man"},
        {"title":"1s in Unlucky Draw",
        "text":"Last minute equaliser doesn't do the boys justice in 8-8 draw"},
        {"title":"Tough Defeat for Firsts",
        "text":"1s surpringly lost their first game in 3 years in a narrow 1-0 defeat"} ]
    
    reports_2nd = [
        {"title": "Good Win for 2s",
        "text":"G. Kerr steals the show with a hat-trick of hat-tricks to win the game"},
        {"title": "2s in unlucky Draw",
        "text":"Drew the game, bit of a surprise but the ref was poor"},
        {"title":"Tough Defeat for Seconds",
        "text":"2s got beat, sure what can you do"} ]
    
    reports_3rd = [
        {"title": "Good Win for 3s",
        "text":"Goals galore as 3s run wild winning 8-0"},
        {"title": "3s in unlucky Draw",
        "text":"We scored the same amount as the other team so the game was a draw"},
        {"title":"Tough Defeat for Thirds",
        "text":"Unlucky for the team"} ]

    reports_u21 = [
        {"title": "Good Win for u21s",
        "text":"u21s keep winning 27 game winning streak going with a fanstatic performance"},
        {"title": "21s in unlucky Draw",
        "text":"Draw's a draw, not much else you can say"},
        {"title":"Tough Defeat for u21 Team",
        "text":"21s got beat, it happens in football"} ]

    match_reports = {"1st_team": {"reports": reports_1st},
        "2nd_team": {"reports": reports_2nd},
        "3rd_team": {"reports": reports_3rd},
        "u21_team": {"reports": reports_u21} }

# If you want to add more catergories or pages,
# add them to the dictionaries above.
# The code below goes through the cats dictionary, then adds each category,
# and then adds all the associated pages for that category.
# if you are using Python 2.x then use cats.iteritems() see
# http://docs.quantifiedcode.com/python-anti-patterns/readability/
# for more information about how to iterate over a dictionary properly.
    for team, team_report in match_reports.items():
        t = add_match_report(team)
        for r in team_report["reports"]:
            add_report(t, r["title"], r["text"])
    
    # Print out the categories we have added.
    for mr in MatchReport.objects.all():
        for r in Report.objects.filter(matchReport=mr):
            print("- {0} - {1}".format(str(mr), str(r)))

def add_report(team, title, text, views=0):
    r = Report.objects.get_or_create(matchReport=team, title=title)[0]
    r.text=text
    r.views=views
    r.save()
    return r

def add_match_report(name):
    mr = MatchReport.objects.get_or_create(name=name)[0]
    mr.save()
    return mr

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()