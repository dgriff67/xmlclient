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
        ht_filter = request.GET.get('HT')
        htr_filter = request.GET.get('HTR')
        ftr_filter = request.GET.get('FTR')
        ref_filter = request.GET.get('Ref')
        s_filter = request.GET.get('S')
        st_filter = request.GET.get('ST')
        c_filter = request.GET.get('C')
        fc_filter = request.GET.get('FC')
        yc_filter = request.GET.get('YC')
        rc_filter = request.GET.get('RC')
        b365_filter = request.GET.get('B365')
        lad_filter = request.GET.get('Lad')
        vc_filter = request.GET.get('VC')
        wh_filter = request.GET.get('WH')
        bb25_filter = request.GET.get('BB2.5')

        matches = Pl1516.objects.filter(hometeam=hometeam_filter)
        if matches.count() < 19:
            parse_load(hometeam_filter)
        context_dict = {'ht_filter': ht_filter, 'htr_filter': htr_filter,  'ftr_filter': ftr_filter,
                        'ref_filter': ref_filter,'s_filter': s_filter, 'st_filter': st_filter,
                        'c_filter': c_filter,'fc_filter': fc_filter,'yc_filter': yc_filter,'rc_filter': rc_filter,
                        'b365_filter': b365_filter, 'lad_filter': lad_filter, 'vc_filter': vc_filter, 'wh_filter': wh_filter,
                        'bb25_filter': bb25_filter, 'matches' : matches}
        return render(request, 'main/match_listings.html', context_dict)


