from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
# Create your models here.

class Category(models.Model):
    "Category describes a category "
    category_name       = models.CharField(max_length=200)
    category_created    = models.DateTimeField(auto_now_add=True)
    category_modified   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Category: %s" % category_name

class CategoryItem(models.Model):
    "Category Items deacibes items related to a category"
    category_item_name      = models.CharField(max_length=200)
    category_item_category  = models.ForeignKey(Category, related_name="category_items", on_delete=models.CASCADE)

    category_item_created   = models.DateTimeField(auto_now_add=True)
    category_item_modified  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Category Item: %s" % category_item_name

class Expense(models.Model):
    "Expense is a editor for a general bill/expense object"
    expense_name            = models.CharField(max_length=200, null=True, blank=True)
    expense_amount          = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    expense_mechant_name    = models.CharField(max_length=200, null=True, blank=True)
    expense_category        = models.ForeignKey(Category, related_name="category_expenses", on_delete=models.CASCADE)
    expense_category_item   = models.ForeignKey(CategoryItem, related_name="category_items_expenses", on_delete=models.CASCADE)
    expense_description     = models.TextField(null=True, blank=True)
    expense_user            = models.ForeignKey(User, on_delete=models.CASCADE)

    expense_created         = models.DateTimeField(auto_now_add=True)
    expense_modified        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Expense: %s - %s" % (expense_name, expense_amount)
