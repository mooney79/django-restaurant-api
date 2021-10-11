from django.urls import path
from menuitems.views import MenuitemListAPIView

urlpatterns = [
    path('menuitems/', MenuitemListAPIView.as_view(), name = "menu_item_list")
]
