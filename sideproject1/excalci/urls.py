from django.conf.urls import url

from . import views

#app_name = 'expense'
urlpatterns = [
    url(r'^expense/$', views.ExpenseListView.as_view(), name='expense_list'),
    url(r'^expense/(?P<expense_id>[0-9]+)/$', views.expense_detail, name='expense_detail')
]
