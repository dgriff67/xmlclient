from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Pl1516

def index(request):
    if not request.GET.get('hometeam'):
        return render(request, 'main/index.html')
    else:
        hometeam_filter = request.GET.get('hometeam')
        matches = Pl1516.objects.filter(hometeam=hometeam_filter)
        context_dict = {'matches' : matches}
        return render(request, 'main/match_listings.html', context_dict)

