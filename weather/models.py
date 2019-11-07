from django.db import models

# Create your models here.
class Cities(models.Model):
    temperature = models.DecimalField( decimal_places = 2, max_digits=4 )
    city = models.CharField(max_length=264)
    description = models.TextField()
    def __str__(self):
        return self.city