from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.income.messages.categories import CATEGORY_ALREADY_EXISTS
from apps.income.models import IncomeCategory


class IncomeCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = IncomeCategory
        fields = ['id', 'name']

    def validate(self, data):
        query = Q(name=data['name'], user=self.context['user'])
        if self.instance:
            query.add(~Q(pk=self.instance.id), Q.AND)

        if IncomeCategory.objects.filter(query).exists():
            raise ValidationError({'user': [CATEGORY_ALREADY_EXISTS]})
        return super(IncomeCategorySerializer, self).validate(data)
