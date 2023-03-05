from rest_framework.routers import SimpleRouter

from apps.income.views.categories import IncomeCategoryViewSet
from apps.income.views.incomes import IncomeViewSet

router = SimpleRouter()
router.register('categories', IncomeCategoryViewSet, basename='income_categories')
router.register('', IncomeViewSet, basename='incomes')

urlpatterns = router.urls + []
