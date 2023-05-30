from django.db import models

# Create your models here.

# changes made on 8-01-23 making model instead of database

class userData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)
    customer_fields = models.CharField(max_length=100)
    skey = models.CharField(max_length=100)
    class Meta:
        db_table = "signup_db"