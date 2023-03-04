from rest_framework.viewsets import ViewSet

from apps.expense.messages import categories as messages
from apps.expense.models import ExpenseCategory
from apps.expense.serializers.categories import ExpenseCategorySerializer
from utilities.mixins import ResponseViewMixin


class ExpenseCategoryViewSet(ViewSet, ResponseViewMixin):
    """
    ViewSet for ExpenseCategory
    """

    def list(self, request):
        categories = request.user.expense_categories.all()
        serializer = ExpenseCategorySerializer(categories, many=True)
        return self.success_response(serializer.data, messages.CATEGORIES_FETCHED)

    def create(self, request):
        serializer = ExpenseCategorySerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return self.success_response(serializer.data, messages.CATEGORY_CREATED)
        return self.error_response(serializer.errors, messages.CATEGORY_CREATION_FAILED)

    def retrieve(self, request, pk=None):
        try:
            category = ExpenseCategory.objects.get(pk=pk)
            return self.success_response(ExpenseCategorySerializer(category).data, messages.CATEGORY_FETCHED)
        except ExpenseCategory.DoesNotExist:
            return self.error_response(message=messages.CATEGORY_DOES_NOT_EXIST)

    def update(self, request, pk=None):
        try:
            category = ExpenseCategory.objects.get(pk=pk, user=request.user)
            serializer = ExpenseCategorySerializer(category, data=request.data, context={'user': request.user})
            if serializer.is_valid():
                serializer.save(user=request.user)
                return self.success_response(serializer.data, messages.CATEGORY_UPDATED)
            return self.error_response(serializer.errors, messages.CATEGORY_UPDATE_FAILED)
        except ExpenseCategory.DoesNotExist:
            return self.error_response(message=messages.CATEGORY_DOES_NOT_EXIST)

    def destroy(self, request, pk=None):
        try:
            category = ExpenseCategory.objects.get(pk=pk, user=request.user)
            category.delete()
            return self.success_response(message=messages.CATEGORY_DELETED)
        except ExpenseCategory.DoesNotExist:
            return self.error_response(message=messages.CATEGORY_DOES_NOT_EXIST)
