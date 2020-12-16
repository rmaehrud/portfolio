from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.


class PortfolioList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    bigimage = ProcessedImageField(
        upload_to='uploads/%Y/%m/%d/',
        processors=[Thumbnail(500, 460)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60})   # 저장 옵션
    smallimage = ProcessedImageField(
        upload_to='uploads/%Y/%m/%d/',
        processors=[Thumbnail(291, 364)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60})   # 저장 옵션
    link = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title

# 게시판 삭제시 파일 동시삭제
@receiver(post_delete, sender=PortfolioList)
def file_delete_action(sender, instance, **kwargs):
    instance.smallimage.delete(False)

# 게시판 삭제시 파일 동시삭제
@receiver(post_delete, sender=PortfolioList)
def file_delete_action(sender, instance, **kwargs):
    instance.bigimage.delete(False)
