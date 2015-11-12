# Create your views here.
from django.utils import simplejson
from regist.models import Info
from django.shortcuts import render_to_response
from django.template import RequestContext
from time import time, localtime, strftime


def FetchDay(request):
    fetch_day = localtime(time())
    return strftime("%A", fetch_day)


def init_status(request):
    all_status = [Info.objects.get(status=1)]
    for every in all_status:
        every.status = 0
        every.save()





def Add(request):

    if request.method == 'POST':
        people_online_list = request.POST.get('idlist')

        print people_online_list
    init_status(request)

    fetch_day = FetchDay(request)

    people_online_details = []

    for id in people_online_list:
        people_online_details.append(Info.objects.get(id=id))

    for entry in people_online_details:
        entry.date_match_dict[fetch_day] += 1
        entry.status = 1
        entry.save()

    all_details = Info.objects.all()
    return render_to_response('index.html', {"all_detail": all_details}, context_instance=RequestContext(request))
