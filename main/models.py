from django.db import models

# Create your models here.
class Menfess(models.Model):
    from_who = models.CharField(max_length=100)
    to_who = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)