from django.db import models
from django.utils import timezone

# Create your models here.

class Services(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    description = models.TextField()
    date_a = models.DateTimeField(default=timezone.now())
    date_b = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_b = timezone.now()
        self.save()

    def __str__(self):
        return self.service_type

