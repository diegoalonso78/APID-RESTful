from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from .serializers import ProteinJSONSerializer
from .models import Protein


def index(request, protein_id):
    serializer = ProteinJSONSerializer()
    query = Protein.objects.filter(Q(uniprot_id__icontains=protein_id) | Q(gene_id__icontains=protein_id) | Q(uniprot_name__icontains=protein_id))
    proteins = serializer.serialize(query)
    return JsonResponse(proteins, safe=False)
