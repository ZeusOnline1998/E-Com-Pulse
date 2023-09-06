from rest_framework.serializers import ModelSerializer
from .models import ProductDetails

class ProductDetailsPlatformSerializer(ModelSerializer):

    class Meta:
        model = ProductDetails
        fields = ['platform', 'product', 'crawl_date', 'price']