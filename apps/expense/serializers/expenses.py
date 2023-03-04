from rest_framework import serializers

from apps.expense.models import Expense
from apps.expense.serializers.categories import ExpenseCategorySerializer


class ExpenseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'category', 'date', 'description', 'spent_by', 'amount']
        extra_kwargs = {'category': {'write_only': True}}


class ExpenseListSerializer(serializers.ModelSerializer):
    category = ExpenseCategorySerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'category', 'date', 'description', 'spent_by', 'amount']
