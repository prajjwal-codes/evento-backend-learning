from django.db import models  # ✅ REQUIRED IMPORT


class Contact(models.Model):
    name = models.CharField(max_length=100)   # Stores name (string, max 100 chars)
    email = models.EmailField(unique=True)   # Email, must be unique
    phone = models.CharField(max_length=15)  # Phone number, stored as string
    address = models.TextField()             # Address, allows long text

    def __str__(self):
        return self.name  # Makes it show the name in Django admin
