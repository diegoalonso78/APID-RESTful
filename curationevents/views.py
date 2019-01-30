from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from .serializers import CurationeventsJSONSerializer
from .models import Intmetpaper, Interaction


def twoProteins(request, participant1_id, participant2_id):
    serializer = CurationeventsJSONSerializer()
    
    query = Interaction.objects.filter(Q(Q(participant1=participant1_id) & Q(participant2=participant2_id)) | Q(Q(participant1=participant2_id) & Q(participant2=participant1_id)))
    interactions = serializer.serialize(query)

    return JsonResponse(interactions, safe=False)    