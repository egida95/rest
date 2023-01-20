from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from .serializers import PostSerializer,UserSerializer
from .models import *

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class UserView(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer