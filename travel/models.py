from django.db import models
from datetime import datetime
class Travel(models.Model):
    country=models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    text=models.TextField()
    picture=models.ImageField(upload_to='image/', default='default.jpg')
    

    def __str__(self):
        return self.country