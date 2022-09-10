"""
View for the Product APis
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Product
from product import serializers

class ProductViewSet(viewsets.ModelViewSet):
    """ View for manage product APIs """

    serializer_class = serializers.ProductDetailSerializer
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Retrieve products for authenticated users && Deriving base queryset method """

        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """ return the serializer based on request """

        if self.action == 'list':
            return serializers.ProductSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """ Create new product using Save hooks from Mixin classes """

        serializer.save(user=self.request.user)
