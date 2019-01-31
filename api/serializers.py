from rest_framework import serializers
from api.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('hash', 'block_number', 'from_address', 'to_address', 'quantity', 'timestamp', 'input_data')
