from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.expense.models import ExpenseCategory


class ExpenseCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name']

    def validate(self, data):
        query = Q(name=data['name'], user=self.context['user'])
        if self.instance:
            query.add(~Q(pk=self.instance.id), Q.AND)

        if ExpenseCategory.objects.filter(query).exists():
            raise ValidationError({'user': ['Category already exists for user']})
        return super(ExpenseCategorySerializer, self).validate(data)
