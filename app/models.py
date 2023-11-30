from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Item(models.Model):
    contact_number_validator = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message='Enter a valid phone number.'
    )

    class Type(models.TextChoices):
        LOST = 'LOST',
        FOUND = 'FOUND'

    image = models.ImageField(upload_to='item/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    contact_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=13,
                                      validators=[contact_number_validator])
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=10,
                            choices=Type.choices,
                            default=Type.LOST)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.contact_name + self.contact_number
