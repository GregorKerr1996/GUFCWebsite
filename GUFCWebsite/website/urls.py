from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^club/', views.club, name = 'club'),
    url(r'^news/(?P<news_name_slug>[\w\-]+)/$', 
    views.show_news, name='show_news')
]