from rest_framework.routers import SimpleRouter

from apps.expense.views.categories import ExpenseCategoryViewSet
from apps.expense.views.expenses import ExpenseViewSet

router = SimpleRouter()
router.register('categories', ExpenseCategoryViewSet, basename='expense_categories')
router.register('', ExpenseViewSet, basename='expenses')

urlpatterns = router.urls + []
