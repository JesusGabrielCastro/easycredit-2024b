from rest_framework import serializers
from .models import Payment
from decimal import Decimal


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id", "normal_payment", "late_payment", "status", "credit", "due_in")

    def update(self, instance: Payment, validated_data):
        credit = instance.credit
        previous_status = instance.status

        instance.status = validated_data.get('status', instance.status)
        instance.normal_payment = validated_data.get('normal_payment', instance.normal_payment)
        instance.late_payment = validated_data.get('late_payment', instance.late_payment)
        instance.due_in = validated_data.get('due_in', instance.due_in)
        instance.save()

        if instance.status == "completed" and previous_status != "completed":
            credit.debt -= instance.normal_payment
            if credit.debt <= Decimal('0.00'):
                credit.status = "completed"
            credit.save()

        return instance