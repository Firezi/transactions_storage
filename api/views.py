from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Transaction
from api.serializers import TransactionSerializer


class TransactionView(APIView):
    def get(self, request):
        t = Transaction.objects.all()
        serializer = TransactionSerializer(t, many=True)

        return Response(serializer.data)
