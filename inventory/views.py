from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Supplier, Purchase, Sale
from .serializers import ProductSerializer, SupplierSerializer, PurchaseSerializer, SaleSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


@api_view(['GET'])
def dashboard_data(request):
    total_products = Product.objects.count()
    total_stock = sum(p.stock for p in Product.objects.all())
    total_sales = sum(s.quantity * s.unit_price for s in Sale.objects.all())
    total_purchase = sum(p.quantity * p.unit_cost for p in Purchase.objects.all())

    return Response({
        "total_products": total_products,
        "total_stock": total_stock,
        "total_sales": total_sales,
        "total_purchase": total_purchase,
    })

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_product(request):
    data = request.data
    # Save to DB
    # Product.objects.create(name=data['product_name'], price=data['price'], stock=data['stock'])
    return Response({"status": "success", "message": "Product added successfully"}, status=status.HTTP_201_CREATED)

