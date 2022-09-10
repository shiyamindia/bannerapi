"""
Serializers for Product Apis
"""

from rest_framework import serializers

from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """ Serilizers for Product """

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'price']
        read_only_fields = ['id']

class ProductDetailSerializer(ProductSerializer):
    """ Serializer for product details """

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['description']

