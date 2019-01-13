from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^club/', views.club, name='club'),
    url(r'^teamProfiles/', views.teamProfiles, name='teamProfiles'),
    url(r'^firstTeam/', views.firstTeam, name='firstTeam'),
    url(r'^secondTeam/', views.secondTeam, name='secondTeam'),
    url(r'^thirdTeam/', views.thirdTeam, name='thirdTeam'),
    url(r'^underTwentyOnes/', views.underTwentyOnes, name='underTwentyOnes'),
    url(r'^matchReports/', views.matchReports, name='matchReports'),



]
