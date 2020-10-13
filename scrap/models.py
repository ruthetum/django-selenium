from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=50, null=False)
    link = models.TextField(null=False)
    date = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.title