from django.contrib import admin

# Register your models here.

from .models import Expense, Category, CategoryItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

admin.site.register(Category, CategoryAdmin)

class CategoryItemAdmin(admin.ModelAdmin):
    list_display = ('category_item_name', 'category_item_category',)
    #raw_id_fields = ('category_item_category',)

admin.site.register(CategoryItem, CategoryItemAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    # list_display = ('expense_name', 'expense_amount', 'expense_mechant_name',
    #  'expense_category', 'expense_category_item', 'expense_description',
    #  'expense_user', 'expense_neccessity_flag')
    #raw_id_fields = ('expense_category_item','expense_category')
    pass
admin.site.register(Expense, ExpenseAdmin)
