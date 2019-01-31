from django.urls import path
from api.views import TransactionView

urlpatterns = [
    path('transactions/', TransactionView.as_view()),
]
