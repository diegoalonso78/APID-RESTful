from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from .serializers import InteractionsJSONSerializer
from .models import Interaction


def index(request, protein_id):
    serializer = InteractionsJSONSerializer()
    #query = Protein.objects.filter(Q(uniprot_id__icontains=protein_id) | Q(gene_id__icontains=protein_id) | Q(uniprot_name__icontains=protein_id))
    #proteins = serializer.serialize(query)
    query = Interaction.objects.filter(Q(participant1__icontains=protein_id) | Q(participant2__icontains=protein_id))
    interactions = serializer.serialize(query)

    return JsonResponse(interactions, safe=False)