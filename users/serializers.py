from rest_framework import serializers

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payment_history = serializers.SerializerMethodField()

    def get_payment_history(self, obj):
        return PaymentSerializer(obj.payment_set.all(), many=True).data

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "payment_history",
            "password",
        )
