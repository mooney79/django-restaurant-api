from django.urls import path, include
# from .menuitems import views

from menuitems.views import MenuitemListAPIView
# from .orders.views import OrderListAPIView

urlpatterns = [
    path('menuitems/', MenuitemListAPIView.as_view(), name = "menu_item_list"),
    path('orders/', include('orders.urls')),
]

