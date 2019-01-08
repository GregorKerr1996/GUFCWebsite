from django.http import HttpResponse

def index(request):
    return HttpResponse("GUFC <a href='/website/club/'>Club</a>")

def club(request):
    return HttpResponse('The club page <a href="/website/">Index</a>')