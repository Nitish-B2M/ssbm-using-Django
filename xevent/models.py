from django.db import models

# Create your models here.  
class fetchEventRecord(models.Model):
    ename = models.CharField(max_length=100)
    eorganization = models.CharField(max_length=100)
    edate = models.CharField(max_length=100)
    evenue = models.CharField(max_length=100)
    estarttime = models.CharField(max_length=100)
    eendtime = models.CharField(max_length=100)
    edesc = models.CharField(max_length=500)
    ecol = models.CharField(max_length=100)
    erow = models.CharField(max_length=100,null=True)
    seatprice = models.CharField(max_length=100)    
   
    class Meta:
        db_table = "event_record"

class fetchSeatRecord(models.Model):
    eventname = models.CharField(max_length=100)
    seat_srno = models.AutoField(primary_key=True)
    seatname = models.CharField(max_length=100)
    seatstatus = models.CharField(max_length=100)
    no_row = models.CharField(max_length=100)
    no_col = models.CharField(max_length=100)
    row_count = models.CharField(max_length=100)
    class Meta:            
        db_table = "event_seatRecord"
    
class fetchUserRecord(models.Model):
    user_srno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    useremail = models.CharField(max_length=100)
    userseat = models.CharField(max_length=100)
    no_seat = models.CharField(max_length=100)
    seattotalprice = models.CharField(max_length=100)
    eventname = models.CharField(max_length=100)
    class Meta:
        db_table = "event_seat_UserBooking"

class fetchFeedbackRecord(models.Model):
    feedback_srno = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=5000)
    username = models.CharField(max_length=100)
    useremail = models.CharField(max_length=100)
    staff_behaviour = models.CharField(max_length=100)
    stadium_cleanliness = models.CharField(max_length=100)
    seat_condition = models.CharField(max_length=100)
    overall_experience = models.CharField(max_length=100)
    event_environment = models.CharField(max_length=100)
    eventname = models.CharField(max_length=100)
    class Meta:
        db_table = "event_feedback"