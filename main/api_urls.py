"""
This file contains API url endpoints for the application
"""
from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.user.urls')),
    path('expense/', include('apps.expense.urls')),
    path('income/', include('apps.income.urls')),
]
