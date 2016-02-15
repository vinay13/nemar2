from django.db import models

class Meanbloodglucose(models.Model):

    Level=models.CharField(max_length=128, default='High')
    mgDL=models.CharField(max_length=128, default='High')
    nmolL=models.IntegerField(default=1)
    Risk=models.CharField(max_length=128,default='Low')
    suggested_action=models.CharField(max_length=128, default='Exercise')

    def __str__(self):
        return self.suggested_action


#    def __save__(self):
#        return self.suggested_action   	
# Create your models here.



class Bloodpressurechart(models.Model):
    Age=models.CharField(max_length=128)
    Min=models.IntegerField(default='10')
    Normal=models.IntegerField(default='15')
    Max=models.IntegerField(default='20')
    

    def __str__(self):
        return self.Age



class Region(models.Model):
    id=models.AutoField(primary_key=True) 
    region=models.CharField(max_length=128,default='MP')
    parent_id=models.IntegerField(default=0)
    REGION_CHOICES =  (
             ('1', 'states'),
             ('2', 'District'),
             ('3', 'Zone'),
             ('4', 'ward'),
             ('5', 'Alley'),
            )
    region_type=models.CharField(max_length=128,default='state',choices=REGION_CHOICES)
    coordinate=models.CharField(max_length=128,default='abc')
    region_order=models.IntegerField(default=1)
    publish=models.IntegerField(default=0)
    pincode=models.IntegerField(default=23409)

    def __str__(self):
        return self.region




class Cholestrolriskchart(models.Model):
    Age=models.CharField(max_length=128,default='21')
    C150=models.CharField(max_length=128,default='High')
    C151to160=models.CharField(max_length=128,default='Low')
    C161to170=models.CharField(max_length=128,default='Low')
    C171to180=models.CharField(max_length=128,default='Low')
    C181to190=models.CharField(max_length=128,default='Low')
    C191to200=models.CharField(max_length=128,default='high')
    C201to210=models.CharField(max_length=128,default='high')
    C211to220=models.CharField(max_length=128,default='high')
    C221to230=models.CharField(max_length=128,default='high')

    def __str__(self):
        return self.Age


class Specialize(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128,blank=True)

    def __str__(self):
        return self.sname




class DoctorList(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128,blank=True)
    home_address=models.CharField(max_length=128,blank=True)
    hospital_address=models.CharField(max_length=128,blank=True)
    clinic_address=models.CharField(max_length=128,blank=True)
 #   specialize=models.ForeignKey(Specialize)
 #   region=models.TextField()
    contact_no=models.IntegerField(default=0)
    def __str__(self):
        return self.name




class MedicalOperate(models.Model):
    id=models.AutoField(primary_key=True)
    operate_name=models.CharField(max_length=128,default='abc')
    OPTYPE_CHOICES =  (
             ('expertise', 'Expertise'),
             ('disease', 'Disease'),
             ('symptoms', 'Symptoms'),
             )
    operate_type=models.CharField(max_length=128,default='xyz',choices=OPTYPE_CHOICES)
    
    def __str__(self):
        return self.operate_type


