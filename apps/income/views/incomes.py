from rest_framework.viewsets import ViewSet

from apps.income.messages import incomes as messages
from apps.income.models import Income
from apps.income.serializers.incomes import IncomeCreateSerializer, IncomeListSerializer
from utilities.mixins import ResponseViewMixin


class IncomeViewSet(ViewSet, ResponseViewMixin):
    """
    ViewSet for Income Model
    """

    def list(self, request):
        incomes = request.user.incomes.all()
        serializer = IncomeListSerializer(incomes, many=True)
        return self.success_response(serializer.data, messages.INCOMES_FETCHED)

    def create(self, request):
        serializer = IncomeCreateSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            income = serializer.save(user=request.user)
            return self.success_response(IncomeListSerializer(income).data, messages.INCOME_CREATED)
        return self.error_response(serializer.errors, messages.INCOME_CREATION_FAILED)

    def update(self, request, pk=None):
        try:
            category = Income.objects.get(pk=pk, user=request.user)
            serializer = IncomeCreateSerializer(category, data=request.data, context={'user': request.user})
            if serializer.is_valid():
                serializer.save(user=request.user)
                return self.success_response(serializer.data, messages.INCOME_UPDATED)
            return self.error_response(serializer.errors, messages.INCOME_UPDATE_FAILED)
        except Income.DoesNotExist:
            return self.error_response(message=messages.INCOME_DOES_NOT_EXIST)

    def destroy(self, request, pk=None):
        try:
            category = Income.objects.get(pk=pk, user=request.user)
            category.delete()
            return self.success_response(message=messages.INCOME_DELETED)
        except Income.DoesNotExist:
            return self.error_response(message=messages.INCOME_DOES_NOT_EXIST)
