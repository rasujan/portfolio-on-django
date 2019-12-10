from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from base_app.models import Project, Profile, Webpage, AccessRecord, KnownledgeOf, StudyTimeline, Githubrepo
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, DetailView, ListView
from .forms import ContactForm
# Create your views here.


def index(request):

    kf_list = KnownledgeOf.objects.order_by('framework')
    profile = Profile.objects.order_by('name')
    project = Project.objects.order_by('number')

    # Mail ko part
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['sujan.rays99@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    context_dict = {'kf': kf_list, 'profile': profile,
                    'project': project, 'form': form}

    # Render the response and send it back!
    return render(request, 'base_app/index.html', context=context_dict)


def emailView(request):

    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
