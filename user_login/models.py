from django.db import models

# Create your models here.
class user_login(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.BigIntegerField(max_length=10)
    password=models.CharField(max_length=100)
    class Meta:
        db_table='crud'