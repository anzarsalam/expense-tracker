from rest_framework import serializers

from apps.income.models import Income
from apps.income.serializers.categories import IncomeCategorySerializer


class IncomeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'category', 'date', 'description', 'amount']
        extra_kwargs = {'category': {'write_only': True}}


class IncomeListSerializer(serializers.ModelSerializer):
    category = IncomeCategorySerializer(read_only=True)

    class Meta:
        model = Income
        fields = ['id', 'category', 'date', 'description', 'amount']
