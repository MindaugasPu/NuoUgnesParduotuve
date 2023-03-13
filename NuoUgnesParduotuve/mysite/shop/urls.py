from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shipping/', views.shipping, name='shipping'),
    path('payment/', views.payment, name='payment'),
    path('processorder/', views.processOrder, name='processorder'),
    path('orders/', views.UserOrdersListView.as_view(), name='orders'),
    path('orders/<int:pk>', views.orderdetail, name='order_detail'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('<int:pk>', views.productdetail, name='product-detail'),
]