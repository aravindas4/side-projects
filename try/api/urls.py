from django.conf.urls import url, include
#from rest_framework.routers import DefaultRouter
from api import views

from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(r'companys', views.CompanyViewSet)
router.register(r'catalogs', views.CatalogViewSet)
router.register(r'users', views.UserViewSet)
companys_router = routers.NestedSimpleRouter(router, r'companys', lookup='company')
companys_router.register(r'catalogs', views.CatalogViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(companys_router.urls)),
]
