from distutils.errors import LinkError
from django.shortcuts import render
from .serializers import LinkSerializer
from .models import Link
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.views import APIView

# Create your views here.
class PostListApi(ListAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer


class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    
class RecentLinkView(APIView):
     """
    Returns a list of recently created active links
    """
def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
        