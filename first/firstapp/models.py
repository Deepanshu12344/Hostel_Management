from django.db import models

class Admin(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=128)

    class Meta:
        db_table = "admin"


class Hostelite(models.Model):
    hid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    room_type = models.CharField(max_length=255, null=True, blank=True)
    date_of_joining = models.DateField()
    course_detail = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_contact_no = models.CharField(max_length=15)
    mother_contact_no = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        db_table = "hostelite"

class Backup(models.Model):
    hid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    room_type = models.CharField(max_length=255, null=True, blank=True)
    date_of_joining = models.DateField()
    course_detail = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_contact_no = models.CharField(max_length=15)
    mother_contact_no = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        db_table = "backup"


class FeesStructure(models.Model):
    room_type = models.CharField(primary_key=True, max_length=255)
    amount = models.IntegerField()

    class Meta:
        db_table = "fees_structure"

class Food(models.Model):
    fid = models.AutoField(primary_key=True)
    date = models.DateField()
    breakfast = models.CharField(max_length=40)
    lunch = models.CharField(max_length=40)
    dinner = models.CharField(max_length=40)
    
    class Meta:
        db_table = "food"


class Feedback(models.Model):
    feid = models.AutoField(primary_key=True)
    hid = models.CharField(max_length=10)
    date = models.DateField()
    room_no = models.CharField(max_length=10)
    ques1 = models.TextField(default="")  # Specify default value
    ques2 = models.TextField(default="")
    ques3 = models.TextField(default="")
    ques4 = models.TextField(default="")
    rating = models.IntegerField(default="")
    suggestions = models.TextField(default="")

    class Meta:
        db_table = "feedback"



class Complaint(models.Model):
    cid = models.AutoField(primary_key=True)
    hid = models.CharField(max_length=10)
    date = models.DateField()
    room_no = models.CharField(max_length=10)
    complaint_type = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = "complaint"