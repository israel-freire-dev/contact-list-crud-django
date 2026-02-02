import uuid
from django.db import models

# Create your models here.
class Contact(models.Model):
    public_id = models.UUIDField(auto_created=True, primary_key=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name