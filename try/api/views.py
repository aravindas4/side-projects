# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#   from django.shortcuts import render
from api.models import Company, Catalog
from django.contrib.auth.models import User
from api.serializers import CompanySerializer, CatalogSerializer, UserSerializer
#from rest_framework import generics
#from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.response import Response
#from rest_framework.reverse import reverse
#from rest_framework import renderers
#from rest_framework_extensions.mixins import NestedViewSetMixin
# Create your views here.
from rest_framework import viewsets

import pdb
'''class CompanyListCatalog(viewsets.ReadOnlyModelViewSet):
    #queryset = get_queryset()
    serializer_class = CatalogSerializer
    #@property
    def get_queryset(self):
        return Catalog.objects.filter(company=self.kwargs['company_pk'])

    queryset = Catalog.objects.filter(company=request['company_pk'])
    def get(self, request, company_id):
        catalogs = Catalog.objects.filter(company=company_id)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)'''


class CompanyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`,  `retrieve`,
    actionsself.

    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(users = self.request.user.username)

'''class CompanyViewSet2(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()

    def list(self, request, company_pk=None):
        queryset = self.queryset.filter(company_id=company_pk)
        serializer = CatalogSerializer(queryset, many=True)
        return Response(serializer.data)'''


class CatalogViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`,  `retrieve`,
     actionsself.

    """
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

    def list(self, request, company_pk=None):
        queryset = self.queryset.filter(company_id=company_pk)
        serializer = CatalogSerializer(queryset, many=True)
        return Response(serializer.data)

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsOwnerOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`,`retrieve`,
     actionsself.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsOwnerOrReadOnly,)'''
