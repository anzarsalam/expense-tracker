from django.db import models

from apps.users.models import AppUser


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(AppUser, on_delete=models.RESTRICT, related_name='expense_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Expense Category'
        verbose_name_plural = 'Expense Categories'
        db_table = 'expense_categories'
        unique_together = ('name', 'user')


class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.RESTRICT)
    date = models.DateField()
    description = models.CharField(max_length=255, null=True, blank=True)
    # spent_by = models.ForeignKey(AppUser, models.RESTRICT, related_name='spent_expenses') # ToDo: Implement later on group expense implementation
    user = models.ForeignKey(AppUser, on_delete=models.RESTRICT, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        db_table = 'expenses'
