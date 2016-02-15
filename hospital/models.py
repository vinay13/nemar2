from django.db import models

class Hospital(models.Model):
	fullname=models.CharField(max_length=128,blank=True)
	address=models.TextField()
	contactno=models.CharField(max_length=128,blank=True)
	OPD=models.BooleanField(default=True)
	IPD=models.BooleanField(default=False)
	ICU=models.BooleanField(default=True)
	IICU=models.BooleanField(default=True)
	MRI=models.BooleanField(default=True)
	CTSCAN=models.BooleanField(default=True)
	XRAY=models.BooleanField(default=False)
	BloodTest=models.BooleanField(default=True)


# Create your models here.
