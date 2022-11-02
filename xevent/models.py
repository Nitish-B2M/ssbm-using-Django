from django.db import models

# Create your models here.
class fetchEventRecord(models.Model):
    ename = models.CharField(max_length=100)
    edate = models.CharField(max_length=100)
    estime = models.CharField(max_length=100)
    eetime = models.CharField(max_length=100)
    eorg = models.CharField(max_length=100)
    edesc = models.CharField(max_length=100)
    evenue = models.CharField(max_length=100)
    class Meta:
        db_table = "event_record"