from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse
from .models import Pl1516
from .parse import parse_load, parse_load_all

filters = ['ht', 'htr', 'ftr', 'ref', 's', 'st', 'c', 'fc', 'yc', 'rc', 'b365', 'lad', 'vc', 'wh', 'bb25']

def index(request):
    context_dict = {(k + '_filter'): v for k, v in request.GET.items() if k in filters}
    hometeam_filter = request.GET.get('hometeam')
    awayteam_filter = request.GET.get('awayteam')

    if not request.GET.get('hometeam'):
        return render(request, 'main/index.html')

    elif request.GET.get('awayteam')=='Any' and request.GET.get('hometeam')!='Any':
        matches = Pl1516.objects.filter(hometeam=hometeam_filter)
        if matches.count() < 19:
            parse_load('home', hometeam_filter)

    elif request.GET.get('hometeam') == 'Any' and request.GET.get('awayteam') != 'Any':
        matches = Pl1516.objects.filter(awayteam=awayteam_filter)
        if matches.count() < 19:
            parse_load('away', awayteam_filter)

    elif request.GET.get('hometeam') != 'Any' and request.GET.get('awayteam') != 'Any':
        matches = Pl1516.objects.filter(hometeam=hometeam_filter, awayteam=awayteam_filter)
        if matches.count() < 1:
            parse_load('away', awayteam_filter)

    elif request.GET.get('hometeam') == 'Any' and request.GET.get('awayteam') == 'Any':
        matches = Pl1516.objects.all()
        if matches.count() < 380:
            parse_load_all

    context_dict['matches'] = matches
    return render(request, 'main/match_listings.html', context_dict)
