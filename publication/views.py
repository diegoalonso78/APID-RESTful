from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from .serializers import PublicationJSONSerializer
from interactions.models import Interaction
from .models import Paper


def index(request, pubmed_id):
    serializer = PublicationJSONSerializer()
    # TODO:  JOIN Interaction & Paper
    query = Interaction.objects.filter(papers=pubmed_id)
    publications = serializer.serialize(query)
    return JsonResponse(publications, safe=False)