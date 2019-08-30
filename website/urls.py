from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^club',views.club, name='club'),
    url(r'^news', views.club_news, name='club_news'),
    url(r'^teamProfiles', views.teamProfiles, name='teamProfiles'),
    url(r'^firstTeam', views.firstTeam, name='firstTeam'),
    url(r'^secondTeam', views.secondTeam, name='secondTeam'),
    url(r'^thirdTeam', views.thirdTeam, name='thirdTeam'),
    url(r'^underTwentyOnes', views.underTwentyOnes, name='underTwentyOnes'),
    url(r'^matchReports', views.matchReports, name='matchReports'),
    url(r'^add_news/$', views.add_report, name='add_report'),
    url(r'^events/$', views.events, name='events'),
    url(r'^club_captain/$', views.club_captain, name='club_captain'),
]
