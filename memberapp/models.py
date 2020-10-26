from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Profile(models.Model):
    # 氏名
    name = models.CharField(max_length=200)
    # 生年月日
    birthday = models.DateTimeField(default=timezone.now)
    # 住所
    address = models.CharField(max_length=200)
    # 電話番号
    tel = models.CharField(max_length=15)
    # ユーザー所持ポイント
    point = models.IntegerField(blank=True, default=50000)
    # Usermodel
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()