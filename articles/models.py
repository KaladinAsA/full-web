from django.db import models
from django.conf import settings
from django.urls import reverse
from accounts.models import CustomUser

class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_detail")
    
    
    
