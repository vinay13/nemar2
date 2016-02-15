from django.db import models

class DoctorInfo(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=128,default='Dr. ')
    specialize=models.CharField(max_length=128,default='s')
    experience=models.CharField(max_length=12,default='2')
    region=models.CharField(max_length=128,default='JBP')
    contact_no=models.IntegerField(default='+91')
    home_address=models.TextField()
    hospital_address=models.TextField()
    clinic_address=models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
