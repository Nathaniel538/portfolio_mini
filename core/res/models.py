from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email=models.EmailField()
    message=models.CharField(max_length=400)
    def __str__(self):
        return self.first_name
        return self.subject
        return self.email
        return self.message
