from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ProductDetails, KeywordTbl, Platform, ProjectIdentifier, KeywordSearchResult, Product

class ProductDetailsPlatformSerializer(ModelSerializer):

    class Meta:
        model = ProductDetails
        fields = ['platform', 'product', 'crawl_date', 'price']

class KeywordListSerializer(ModelSerializer):

    class Meta:
        model = KeywordTbl
        fields = ['id', 'keyword']

class PlatformListSerializer(ModelSerializer):

    platform_name = serializers.SerializerMethodField()

    class Meta:
        model = Platform
        fields = ['id', 'platform_name']

    def get_platform_name(self, obj):
        return Platform.objects.get(id=obj.id).platform_name.title()

class BrandListSerializer(ModelSerializer):

    class Meta:
        model = ProjectIdentifier
        fields = ['id', 'brand']

class KeywordSearchResultSerializer(ModelSerializer):

    keyword = serializers.SerializerMethodField()
    platform = serializers.SerializerMethodField()

    class Meta:

        model = KeywordSearchResult
        fields = ['id', 'platform', 'keyword', 'product_name', 'crawl_date']

    def get_keyword(self, obj):
        return KeywordTbl.objects.get(id=obj.keyword_id).keyword

    def get_platform(self, obj):
        return Platform.objects.get(id=obj.platform_id).platform_name.title()

class ProductListSerializer(ModelSerializer):

    platform_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'platform', 'platform_name']

    def get_platform_name(self, obj):
        return Product.objects.get(id=obj.id).platform.platform_name.title()


class KeywordFilterDataSerializer(ModelSerializer):

    platform = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    keyword = serializers.SerializerMethodField()

    class Meta:
        model = KeywordSearchResult
        fields = ['product_rank', 'product_name', 'keyword', 'platform', 'date']

    def get_keyword(self, obj):
        return KeywordTbl.objects.get(id=obj.keyword_id).keyword

    def get_platform(self, obj):
        return Platform.objects.get(id=obj.platform_id).platform_name.title()

    def get_date(self, obj):
        return KeywordSearchResult.objects.get(id=obj.id).crawl_date
