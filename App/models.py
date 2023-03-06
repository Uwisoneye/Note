from django.db import models
from django.utils import timezone
# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.title
        
    
    