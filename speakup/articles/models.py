from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.CharField(max_length=100)
    body  = models.TextField(max_length=2000)
    date  = models.DateTimeField(auto_now_add=True)
    # will add more fields later   


    def __str__(self):
        return self.title