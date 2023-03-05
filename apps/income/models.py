from django.db import models

from apps.users.models import AppUser


class IncomeCategory(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(AppUser, on_delete=models.RESTRICT, related_name='income_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Income Category'
        verbose_name_plural = 'Income Categories'
        db_table = 'income_categories'
        unique_together = ('name', 'user')


class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.RESTRICT)
    date = models.DateField()
    description = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(AppUser, on_delete=models.RESTRICT, related_name='incomes')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'
        db_table = 'incomes'
