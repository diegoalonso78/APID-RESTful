from django.shortcuts import render

from django.http import HttpResponse
from .models import Interaction
from django.template import loader


def index(request):
    latest_interaction_list = Interaction.objects.all()[:50]
    template = loader.get_template('searchProtein/index.html')
    context = {
        'interactions' : latest_interaction_list,
    }
    
    return HttpResponse(template.render(context,request))


def detail(request, interaction_id):
    return HttpResponse("You're looking at interaction %s." % interaction_id)
