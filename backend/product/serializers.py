from rest_framework.serializers import ModelSerializer
from .models import ProductDetails, KeywordTbl, Platform, ProjectIdentifier

class ProductDetailsPlatformSerializer(ModelSerializer):

    class Meta:
        model = ProductDetails
        fields = ['platform', 'product', 'crawl_date', 'price']

class KeywordListSerializer(ModelSerializer):

    class Meta:
        model = KeywordTbl
        fields = ['id', 'keyword']

class PlatformListSerializer(ModelSerializer):

    class Meta:
        model = Platform
        fields = ['id', 'platform_name']

class BrandListSerializer(ModelSerializer):

    class Meta:
        model = ProjectIdentifier
        fields = ['id', 'brand']
