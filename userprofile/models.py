from django.db import models



class UsersProfile(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=28,default="a")
	password=models.CharField(max_length=29,default="a")
	emailid=models.CharField(max_length=30,default="a")
	usergroup=models.CharField(max_length=30,default="a")
	status=models.CharField(max_length=29,default="a")
	online=models.CharField(max_length=29,default="a")
	img=models.CharField(max_length=29,default="a")
	mobileno=models.CharField(max_length=29,default="a")
	createdate=models.CharField(max_length=29,default="a")
	lastdate=models.CharField(max_length=29,default="a")
	updatetime=models.CharField(max_length=29,default="a")
	sessions=models.CharField(max_length=29,default="a")
	loginfailures=models.CharField(max_length=29,default="a")

	def __str__(self):
		return self.username


class UserGroup(models.Model):
	id=models.AutoField(primary_key=True)
	groupname=models.CharField(max_length=32,default='admin')
	priviledges=models.CharField(max_length=45,default='socialinfo')




class UserGroupCustom(models.Model):
	id=models.AutoField(primary_key=True)
	uid=models.CharField(max_length=32,default="s")
	gid=models.CharField(max_length=43,default="t")
	customerPrividges=models.CharField(max_length=42,default="ty")










# Create your models here.
