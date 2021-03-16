from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserInfo(AbstractUser):
    """
    用户模块
    """
    nid = models.AutoField(primary_key=True)
