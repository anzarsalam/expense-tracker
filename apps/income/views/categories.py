from rest_framework.viewsets import ViewSet

from apps.income.messages import categories as messages
from apps.income.models import IncomeCategory
from apps.income.serializers.categories import IncomeCategorySerializer
from utilities.mixins import ResponseViewMixin


class IncomeCategoryViewSet(ViewSet, ResponseViewMixin):
    """
    ViewSet for IncomeCategory
    """

    def list(self, request):
        categories = request.user.income_categories.all()
        serializer = IncomeCategorySerializer(categories, many=True)
        return self.success_response(serializer.data, messages.CATEGORIES_FETCHED)

    def create(self, request):
        serializer = IncomeCategorySerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return self.success_response(serializer.data, messages.CATEGORY_CREATED)
        return self.error_response(serializer.errors, messages.CATEGORY_CREATION_FAILED)

    def retrieve(self, request, pk=None):
        try:
            category = IncomeCategory.objects.get(pk=pk)
            return self.success_response(IncomeCategorySerializer(category).data, messages.CATEGORY_FETCHED)
        except IncomeCategory.DoesNotExist:
            return self.error_response(message=messages.CATEGORY_DOES_NOT_EXIST)

    def update(self, request, pk=None):
        try:
            category = IncomeCategory.objects.get(pk=pk, user=request.user)
            serializer = IncomeCategorySerializer(category, data=request.data, context={'user': request.user})
            if serializer.is_valid():
                serializer.save(user=request.user)
                return self.success_response(serializer.data, messages.CATEGORY_UPDATED)
            return self.error_response(serializer.errors, messages.CATEGORY_UPDATE_FAILED)
        except IncomeCategory.DoesNotExist:
            return self.error_response(message=messages.CATEGORY_DOES_NOT_EXIST)

    def destroy(self, request, pk=None):
        try:
            category = IncomeCategory.objects.get(pk=pk, user=request.user)
            category.delete()
            return self.success_response(message=messages.CATEGORY_DELETED)
        except IncomeCategory.DoesNotExist:
            return self.error_response(message=messages.CATEGORY_DOES_NOT_EXIST)
