from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    website = models.URLField()
    industry = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
