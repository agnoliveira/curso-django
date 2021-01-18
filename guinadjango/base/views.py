# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Olá Django!!</html></body>')
