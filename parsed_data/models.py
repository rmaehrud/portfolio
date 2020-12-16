from django.db import models




class Link(models.Model):
    mobeil_web_url = models.CharField(max_length=100,verbose_name='mobeil_web_url')
    web_url = models.CharField(max_length=100,verbose_name='web_url')
    integer=models.IntegerField(primary_key=True)



    def __str__(self):
        return self.web_url


class BigData(models.Model):
    object_type = models.CharField(max_length=100,blank=True,default="text")
    text = models.CharField(max_length=100,verbose_name='카카오톡 텍스트')
    button_title = models.CharField(max_length=100,blank=True,default="바로 확인")
    link = models.ForeignKey(Link,on_delete=models.CASCADE,default=12341234)



    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-id']



class BlogData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title
