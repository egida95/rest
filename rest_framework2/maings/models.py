from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self) -> str:
        return self.username
    # @property
    # def comments(self):
    #     return self.posts.count()
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=127)
    def __str__(self) -> str:
        return self.name