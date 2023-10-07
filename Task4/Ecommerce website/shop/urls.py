"""rkwebstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop import views

urlpatterns = [
    path('', views.products, name = "Products"),
    path('products/', views.products, name = "Products"),
    path('product/<int:product_id>', views.viewProduct, name = "ViewProduct"),
    path('addproduct/', views.addproduct, name = "AddProduct"),
    path('tracker/', views.tracker, name = "TrackingStatus"),
    path('search/', views.search, name = "Search"),
    path('cart/', views.cart, name = "Cart"),
    path('addtocart/', views.add_to_cart, name = "add_to_cart"),
    path('addtowishlist/', views.add_to_wishlist, name = "add_to_wishlist"),
    
    path('count/<int:product_id>/<str:ar>', views.count, name = "count"),
    path('remove/<int:product_id>', views.remove_from_cart, name = "remove"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
