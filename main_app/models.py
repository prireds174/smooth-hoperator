from django.db import models

# Create your models here.

class Beer(models.Model):
    name = models.CharField(max_length=90)
    brand = models.CharField(max_length=120)
    img = models.CharField(max_length=250)
    style = models.CharField(max_length=90)
    description = models.TextField(max_length=900, blank=True)
    currently_being_poured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
    
