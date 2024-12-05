from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Credit, Payment
from .serializers import CreditSerializer, PaymentSerializer, CreditCreationSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["normal_payment"]
    filterset_fields = ["status"]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.credit.update_status()

    def perform_update(self, serializer):
        payment = serializer.save()
        payment.credit.update_status()