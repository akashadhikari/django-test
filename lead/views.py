import django_filters.rest_framework

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from rest_framework import filters

from common.filters import DateRangeFilter
from .permissions import IsOwnerOrReadOnly
from .models import LeadProcess
from .serializers import LeadProcessSerializer, StatsSerializer

# http://localhost:8000/api/lead/v1/leads/?end_date=2018-01-23&start_date=2018-01-20


class LeadProcessViewSet(generics.ListCreateAPIView):
    queryset = LeadProcess.objects.all()
    serializer_class = LeadProcessSerializer
    #authentication_classes = [TokenAuthentication]

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        django_filters.rest_framework.DjangoFilterBackend,
        DateRangeFilter,
        )
    
    filter_fields = ('employer_name', 'service_type', 'user__username')
    search_fields = ('employer_name', 'service_type', 'user__username')

    def perform_create(self, serializer):
        serializer.save() # Adding owner=self.request.user

class LeadProcessDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeadProcess.objects.all()
    serializer_class = LeadProcessSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    #authentication_classes = [TokenAuthentication]


class StatsViewSet(generics.ListCreateAPIView):
    queryset = LeadProcess.objects.all() # LeadProcess.objects.filter(service_type='Hardware').count()
    serializer_class = StatsSerializer