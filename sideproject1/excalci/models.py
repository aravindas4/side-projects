from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.core.urlresolvers import reverse
# Create your models here.

class Category(models.Model):
    "Category describes a category "
    category_name       = models.CharField(max_length=200)
    category_created    = models.DateTimeField(auto_now_add=True)
    category_modified   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-category_created',)

    def __str__(self):
        return "%s" % self.category_name

class CategoryItem(models.Model):
    "Category Items deacibes items related to a category"
    category_item_name      = models.CharField(max_length=200)
    category_item_category  = models.ForeignKey(Category, related_name="category_items", on_delete=models.CASCADE)

    category_item_created   = models.DateTimeField(auto_now_add=True)
    category_item_modified  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-category_item_created',)

    def __str__(self):
        return "%s Item" % self.category_item_name

class ExpenseManager(models.Manager):
    "ExpenseManager filters only neccessary flagged"
    def get_queryset(self):
        return super(ExpenseManager, self).get_queryset().filter(expense_neccessity_flag=True)

class Expense(models.Model):
    "Expense is a editor for a general bill/expense object"
    expense_name            = models.CharField(max_length=200)
    expense_amount          = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    expense_mechant_name    = models.CharField(max_length=200, null=True, blank=True)
    #expense_category        = models.ForeignKey(Category, related_name="category_expenses", on_delete=models.CASCADE)
    expense_category_item   = models.ForeignKey(CategoryItem, related_name="category_items_expenses", on_delete=models.CASCADE)
    expense_description     = models.TextField(null=True, blank=True)
    expense_user            = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_slug            = models.SlugField(max_length=250, unique_for_date='expense_created', null=True, blank= True)
    expense_created         = models.DateTimeField(auto_now_add=True)
    expense_modified        = models.DateTimeField(auto_now=True)
    expense_neccessity_flag = models.BooleanField(default=True)

    objects                 = models.Manager()
    neccessary              = ExpenseManager()
    class Meta:
        ordering = ('-expense_created',)

    def __str__(self):
        return "%s" % (self.expense_name)

    def get_absolute_url(self):
        return reverse('excalci:expense_detail', args=[self.id])

    def save(self, *args, **kwargs):
        if not self.expense_slug:
            self.expense_slug = '-'.join(self.expense_name.lower().split())
        super(Expense, self).save(*args, **kwargs)
