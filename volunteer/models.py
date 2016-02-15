from django.db import models




class Social(models.Model):
	id=models.AutoField(primary_key=True)
	fname=models.CharField(max_length=128,default='firstname')
	lname=models.CharField(max_length=128,default='lastname')
	DOB=models.CharField(max_length=128,default='10-10-2010')
	gender=models.CharField(max_length=128,default='M')
	Hostpital_name=models.CharField(max_length=128,default='q')
	Doctor_name=models.CharField(max_length=128,default='Dr.')
	ownLaptop=models.CharField(max_length=128,default='yes')
	ownVechile=models.CharField(max_length=128,default='yes')


	def __str__(self):
		return self.fname




class Education(models.Model):
	id=models.AutoField(primary_key=True)
	school_name=models.CharField(max_length=123,default='x')
	school_yearofpassing=models.CharField(max_length=124,default='y')
	graduation=models.CharField(max_length=12,default='Yes')
	college_name=models.CharField(max_length=124,default='o')
	grad_yearofpassing=models.CharField(max_length=123,default='z')

	def __str__(self):
		return self.school_name



class Contact(models.Model):
	id=models.AutoField(primary_key=True)
	state=models.CharField(max_length=33,default='MP')
	city=models.CharField(max_length=21,default='JBP')
	zone=models.CharField(max_length=23,default='napier town')
	address=models.CharField(max_length=127,default='23 Ranjhi Market')
	contactno=models.IntegerField(default='+91')
	alt_contactno=models.IntegerField(default='+91')


	def __str__(self):
		return self.city




# Create your models here.
