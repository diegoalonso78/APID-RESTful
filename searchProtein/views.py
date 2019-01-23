from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	latest_interaction_list = Interaction.objects.all()[:5]
    output = ', '.join([i.participant1 for i in latest_interaction_list])
   return HttpResponse(output)


def detail(request,interaction_id):
	return HttpResponse("You're looking at interaction %s." % interaction_id)