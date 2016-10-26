from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse
from .models import Pl1516
from .parse import parse_load


def index(request):
    if not request.GET.get('hometeam'):
        return render(request, 'main/index.html')
    else:
        hometeam_filter = request.GET.get('hometeam')
        hthg_filter = request.GET.get('HTHG')
        htag_filter = request.GET.get('HTAG')
        matches = Pl1516.objects.filter(hometeam=hometeam_filter)
        if (matches.count() < 19):
            parse_load(hometeam_filter)
        context_dict = {'hthg_filter': hthg_filter, 'htag_filter': htag_filter, 'matches' : matches}
        return render(request, 'main/match_listings.html', context_dict)


