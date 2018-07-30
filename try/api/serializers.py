from rest_framework import serializers
from api.models import Company, Catalog
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    #companys = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username')#,'companys')

class CompanySerializer(serializers.ModelSerializer):
    #catalogs = CatalogSerializer(many=True, read_only=True)
    #users = UserSerializer(many = True)
    #users = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    class Meta:
        model = Company
        #fields = ('id', 'name', 'phone_number')#, 'catalogs','users')
        depth = 1

class CatalogSerializer(serializers.ModelSerializer):
    #user = serializers.ReadOnlyField(source='owner.username')
    company = CompanySerializer()
    #company_phone = serializers.ReadOnlyField(source='company.phone_number')
    dynamic_total_price = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        fields = ('id','name', 'no_of_pcs', 'per_pcs_price','company','dynamic_total_price')

    def get_dynamic_total_price(self, instance):
        return instance.no_of_pcs * instance.per_pcs_price
