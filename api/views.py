from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate, AdvocateLink, Company
from .serializers import AdvocateSerializer, AdvocateLinkSeriizer, CompanySerializer
from .pagination import StandardResultsSetPagination


@api_view(['GET'])
def home(request):
    routes = {
        'companies': 'companies/',
        'company': 'companies/:id',
        'advocates': 'advocates/',
        'advocate': 'advocate/:id'
    }

    return Response(routes)


@api_view(['GET'])
def get_all_advocates(request):
    advocates = Advocate.objects.all() 
    if 'query' in request.GET:
        name = request.GET.get('query')
        advocates = Advocate.objects.filter(name=name)
    paginator = StandardResultsSetPagination()
    result_page = paginator.paginate_queryset(advocates, request)
    serializer = AdvocateSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def get_advocate(request, id):
    adv = Advocate.objects.get(id=id)
    serializer = AdvocateSerializer(adv ,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def get_company(request, id):
    company = Company.objects.get(id=id)
    serilizer = CompanySerializer(company, many=False)
    return Response(serilizer.data)


# @api_view(['GET'])
# def get_all_advocates(request):
#     adv = Advocate.objects.all()
#     serializer = AdvocateSerializer(adv, many=True)
#     return Response(serializer.data)


