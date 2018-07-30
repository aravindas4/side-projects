from django.conf.urls import url

from . import views

app_name = 'expense'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<expense_id>[0-9]+)/$', views.detail, name='detail')
]
