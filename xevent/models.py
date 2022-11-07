from django.db import models

# Create your models here.
class fetchEventRecord(models.Model):
    id = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100)
    eorganization = models.CharField(max_length=100)
    edate = models.CharField(max_length=100)
    evenue = models.CharField(max_length=100)
    estarttime = models.CharField(max_length=100)
    eendtime = models.CharField(max_length=100)
    edesc = models.CharField(max_length=100)
    ecol = models.CharField(max_length=100)
    erow = models.CharField(max_length=100)
    seatprice = models.CharField(max_length=100)
    class Meta:
        db_table = "event_record"

eventname = "ipl"
class fetchSeatRecord(models.Model):
    seat_srno = models.AutoField(primary_key=True)
    seatname = models.CharField(max_length=100)
    seatstatus = models.CharField(max_length=100)
    no_row = models.CharField(max_length=100)
    no_col = models.CharField(max_length=100)
    row_count = models.CharField(max_length=100)
    class Meta:
        db_table = "event_"+eventname+"_seat"