from django.urls import path
from . import views

urlpatterns = [
    path('api/products/add/', views.add_product, name='add_product'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet, PurchaseViewSet, SaleViewSet, dashboard_data

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('suppliers', SupplierViewSet)
router.register('purchases', PurchaseViewSet)
router.register('sales', SaleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/dashboard/', dashboard_data),
]
