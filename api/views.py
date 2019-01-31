from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Transaction
from api.serializers import TransactionSerializer


class TransactionView(APIView):
    def get(self, request):
        t = Transaction.objects.all()

        if request.GET.get('fromAddress'):
            t = t.filter(from_address__iexact=request.GET.get('fromAddress'))

        if request.GET.get('toAddress'):
            t = t.filter(to_address__iexact=request.GET.get('toAddress'))

        if request.GET.get('fromDate'):
            t = t.filter(timestamp__gte=request.GET.get('fromDate'))

        if request.GET.get('toDate'):
            t = t.filter(timestamp__lt=request.GET.get('toDate'))

        serializer = TransactionSerializer(t, many=True)

        return Response(serializer.data)
