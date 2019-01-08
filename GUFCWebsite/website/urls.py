from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^club/', views.club, name = 'club'),
]