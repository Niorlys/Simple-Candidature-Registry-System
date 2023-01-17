from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import *

__all__ = ['TechView', 'CandidateView','CandidateTechView', 'Report']

class TechView(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechSerializer

class CandidateView(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetCandidateSerializer
        return super().get_serializer_class()


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CandidateTechView(viewsets.ModelViewSet):
    queryset = CandidateTechs.objects.all()
    serializer_class = CandidateTechSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetCandidateTechSerializer
        return super().get_serializer_class()

class Report(ListAPIView):
    queryset = CandidateTechs.objects.all()
    serializer_class = GetCandidateTechSerializer

    
    def list(self, request, *args, **kwargs):
        tech = request.query_params['tech']

        queryset = CandidateTechs.objects.filter(tech__name=tech).order_by('-experience')
        if not queryset:
            return Response(f'There is not such technology named {tech}', status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
