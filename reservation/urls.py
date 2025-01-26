from django.urls import path

from .views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
    })),

     path('product', ProductViewSet.as_view({
        'get': 'liste',
    }))
]
