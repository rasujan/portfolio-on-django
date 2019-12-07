from django.shortcuts import render
from django.http import HttpResponse
from base_app.models import Githubrepo, Profile, Webpage, AccessRecord, KnownledgeOf, StudyTimeline, Gitrepo
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, DetailView, ListView
# Create your views here.


def index(request):
    # Obtain the context from the HTTP request.
    # context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the knowledge by framework in asc order.

    # Place the list in our context_dict dictionary which will be passed to the template engine.
    kf_list = KnownledgeOf.objects.order_by('framework')
    # context_dict = {'kf': kf_list}

    profile = Profile.objects.order_by('name')
    context_dict = {'kf': kf_list, 'profile': profile}

    # Render the response and send it back!
    return render(request, 'base_app/index.html', context=context_dict)
