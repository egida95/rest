from .views import PostView, UserView
from django.urls import path 
from rest_framework.routers import DefaultRouter as  DR

router = DR()

router.register('posts',PostView, basename= 'posts')
router.register('users',UserView, basename= 'users')

urlpatterns = []
urlpatterns += router.urls
