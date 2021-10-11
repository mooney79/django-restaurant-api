from .models import Menuitem
from rest_framework import generics
from .serializers import MenuitemSerializer

# Create your views here.

class MenuitemListAPIView(generics.ListAPIView):
    queryset=Menuitem.objects.all()   
    serializer_class = MenuitemSerializer

# class MenuitemListView(generics.ListView):
#     model = Menuitem
    # queryset=Menuitem.objects.all()


