from rest_framework.viewsets import ViewSet

from apps.expense.messages import expenses as messages
from apps.expense.models import Expense
from apps.expense.serializers.expenses import ExpenseCreateSerializer, ExpenseListSerializer
from utilities.mixins import ResponseViewMixin


class ExpenseViewSet(ViewSet, ResponseViewMixin):
    """
    ViewSet for Expense Model
    """

    def list(self, request):
        expenses = request.user.expenses.all()
        serializer = ExpenseListSerializer(expenses, many=True)
        return self.success_response(serializer.data, messages.EXPENSES_FETCHED)

    def create(self, request):
        serializer = ExpenseCreateSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            expense = serializer.save(user=request.user)
            return self.success_response(ExpenseListSerializer(expense).data, messages.EXPENSE_CREATED)
        return self.error_response(serializer.errors, messages.EXPENSE_CREATION_FAILED)

    def update(self, request, pk=None):
        try:
            category = Expense.objects.get(pk=pk, user=request.user)
            serializer = ExpenseCreateSerializer(category, data=request.data, context={'user': request.user})
            if serializer.is_valid():
                serializer.save(user=request.user)
                return self.success_response(serializer.data, messages.EXPENSE_UPDATED)
            return self.error_response(serializer.errors, messages.EXPENSE_UPDATE_FAILED)
        except Expense.DoesNotExist:
            return self.error_response(message=messages.EXPENSE_DOES_NOT_EXIST)

    def destroy(self, request, pk=None):
        try:
            category = Expense.objects.get(pk=pk, user=request.user)
            category.delete()
            return self.success_response(message=messages.EXPENSE_DELETED)
        except Expense.DoesNotExist:
            return self.error_response(message=messages.EXPENSE_DOES_NOT_EXIST)
