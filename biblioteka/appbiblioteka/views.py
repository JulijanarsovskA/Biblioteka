from django.shortcuts import render
from .models import Knigi, Clen
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import KnigiSerializer, ClenSerializer
from django.utils.timezone import now 
from datetime import timedelta

# Create your views here.

@api_view(['GET', "POST", 'DELETE'])
def site_knigi(request):
    if request.method  == 'GET':
        site_knigi = Knigi.objects.all() 
        knigi_serializer = KnigiSerializer(site_knigi, many = True)
        return Response(knigi_serializer.data)
    elif request.method == "POST":
        knigi_serializer = KnigiSerializer(data=request.data)
        if knigi_serializer.is_valid():
            knigi_serializer.save()
            return Response(knigi_serializer.data)
        return Response(knigi_serializer.errors)
    elif request.method == 'DELETE':
        kniga_delete = Knigi.objects.get(id = request.data['id'])
        kniga_delete.delete()
        return Response ({'info': "Kniga is deleted"})    

@api_view(['GET', "POST", 'DELETE'])
def site_clenovi(request):
    if request.method  == 'GET':
        site_clenovi = Clen.objects.all() 
        clen_serializer = ClenSerializer(site_clenovi, many = True)
        return Response(clen_serializer.data)
    elif request.method == "POST":
        clen_serializer = ClenSerializer(data=request.data)
        if clen_serializer.is_valid():
            clen_serializer.save()
            return Response(clen_serializer.data)
        return Response(clen_serializer.errors)
    elif request.method == 'DELETE':
        clen_delete = Clen.objects.get(id = request.data['id'])
        clen_delete.delete()
        return Response ({'info': "Clen {} is deleted".format(id)})


 
@api_view(['GET', 'DELETE'])
def edna_kniga(request):
    if request.method  == 'GET':
        edna_knigi = Knigi.objects.get(id = request.GET['id']) 
        kniga_serializer = KnigiSerializer(edna_knigi)
        return Response(kniga_serializer.data)
    elif request.method == 'DELETE':
        kniga_delete = Knigi.objects.get(id = request.data['id'])
        kniga_delete.delete()
        return Response ({'info': "Kniga {} is deleted"})    

@api_view(['GET', 'DELETE'])
def eden_clen(request):
    if request.method  == 'GET':
        eden_clenovi = Clen.objects.get(id = request.GET['id']) 
        clen_serializer = ClenSerializer(eden_clenovi)
        return Response(clen_serializer.data)
    elif request.method == 'DELETE':
        clen_delete = Clen.objects.get(id = request.data['id'])
        clen_delete.delete()
        return Response ({'info': "Clen is deleted"})

 
 
@api_view (['GET', 'POST'])
def pozajmi(request):
    clen_id = request.data["clen_id"]
    kniga_id = request.data['kniga_id']
    clen = Clen.objects.get(id=clen_id)
    kniga = Knigi.objects.get(id=kniga_id)
    #prmena kaj clen
    clen.dali_pozajmeno = True
    clen.pozajmena_kniga = kniga 
    clen.data_pozajmuvanje = now()
    clen.save()
    #promena kaj knig
    kniga.kolicina = kniga.kolicina - 1
    kniga.save()

    clen_serializer = ClenSerializer(clen)
    return Response(clen_serializer.data)
 
@api_view (['GET', 'POST'])
def vrati(request):
    clen_id = request.data["clen_id"]
    kniga_id = request.data['kniga_id']
    clen = Clen.objects.get(id=clen_id)
    kniga = Knigi.objects.get(id=kniga_id)
    #prmena kaj clen
    clen.dali_pozajmeno = False
    clen.pozajmena_kniga = None 
    clen.save()
    #promena kaj knig
    kniga.kolicina = kniga.kolicina + 1
    kniga.save()

    clen_serializer = ClenSerializer(clen)
    return Response(clen_serializer.data)
 
 
 
 
 
 
 
 
 
 
 
 
