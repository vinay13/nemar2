from django.db import models
class Meanbloodglucose(models.Model):

    Level=models.CharField(max_length=128, default='SOME STRING')
    mgDL=models.CharField(max_length=128, default='SOME STRING')
    nmolL=models.IntegerField(default='1')
    Risk=models.CharField(max_length=128,default='SOME STRING')
    suggested_action=models.CharField(max_length=128, default='SOME STRING')

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
    parent_id=models.IntegerField(default='0')
    REGION_CHOICES =  (
             ('1', 'states'),
             ('2', 'District'),
             ('3', 'Zone'),
             ('4', 'ward'),
             ('5', 'Alley'),

             )
    region_type=models.CharField(max_length=128,default='state',choices=REGION_CHOICES)
    coordinate=models.CharField(max_length=128,default='abc')
#    REGORDER_CHOICES =  (
#             ('1', 'MP'),
#             ('2', 'UP'),
#             ('3', 'GUJRAT'),
#             ('4', 'Orissa'),
#             ('5', 'Punjab'),
#
#             )
    region_order=models.IntegerField(default='1')
    publish=models.IntegerField(default='0')
#    REGION_CHOICES =  (
#             ('1', 'states'),
#             ('2', 'District'),
#             ('3', 'Zone'),
#             ('4', 'ward'),
#             ('5', 'Alley'),
#             
#             )
    
#    state=models.CharField(max_length=19,default='choose',choices=STATE_CHOICES)
#    GENRE_CHOICES =  (
#             ('rock', 'Jabalpur'),
#             ('jazz/blues', 'Bhopal'),
#             ('blues', 'Itarsi'),
#             ('r&b', 'Indore'),
#             ('jazz', 'Allahabad'),
#             ('pop', 'Lucknow'), 
#             ('hip-hop', 'Varanasi'),    
#             )
#    city=models.CharField(max_length=19,default='choose',choices=GENRE_CHOICES)
    pincode=models.IntegerField(default='234098')
#    parent_id=models.IntegerField(default='0')
#    coordinate=models.CharField(max_length=128,default='abc')
#    publish=models.IntegerField(default='0')
#    region_order=models.IntegerField(default='1')
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
    sname=models.CharField(max_length=128,default='null')

    def __str__(self):
        return self.sname




class DoctorList(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128,default='Dr. ')
    home_address=models.CharField(max_length=128,default='address')
    hospital_address=models.CharField(max_length=128,default='address')
    clinic_address=models.CharField(max_length=128,default='address')
    specialize=models.ForeignKey(Specialize)
    region=models.ForeignKey(Region)
    contact_no=models.IntegerField(default='0')
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






class SocialInfo(models.Model):
    FirstName=models.CharField(max_length=128,default='abc')
    LastName=models.CharField(max_length=128,default='s')
    Dob=models.CharField(max_length=128,default='ds')
    ContactNo=models.IntegerField(default='1')
    FatherName=models.CharField(max_length=128,default=' ')
    fDOB=models.CharField(max_length=128,default=' ')
    fContactNo=models.IntegerField(default=' ')
    MotherName=models.CharField(max_length=128,default=' ')
    mDOB=models.CharField(max_length=128,default=' ')
    mContactNo=models.IntegerField(default=' ')
    Gender=models.CharField(max_length=128,default=' ')
    Siblings=models.CharField(max_length=128,default=' ')
    SpouseName=models.CharField(max_length=128,default=' ')
    sDOB=models.CharField(max_length=128,default=' ')
    MarriageDate=models.CharField(max_length=128,default=' ')
    Children=models.IntegerField(default=' ')
    GirlCount=models.IntegerField(default=' ')
    BirthPlace=models.CharField(max_length=128,default=' ')
    Delivery=models.CharField(max_length=128,default=' ')
    Domicile=models.CharField(max_length=128,default=' ')
    YearOfLiving=models.CharField(max_length=128,default=' ')

    def __str__(self):
        return self.LastName




class HealthInfo(models.Model):
    Allergy=models.CharField(max_length=128,default='abc')
    PhysicalChallenged=models.CharField(max_length=128,default='abc')
    BloodGroup=models.CharField(max_length=128,default='abc')
    HomeAddress=models.CharField(max_length=128,default='abc')
    OfficeAddress=models.CharField(max_length=128,default='abc')
    ChronicDisease1=models.CharField(max_length=128,default='abc')
    ChronicDisease2=models.CharField(max_length=128,default='abc')
    ChronicDisease3=models.CharField(max_length=128,default='abc')
    TroubleDisease1=models.CharField(max_length=128,default='abc')
    TroubleDisease2=models.CharField(max_length=128,default='abc')
    TroubleDisease3=models.CharField(max_length=128,default='abc')
    Digestion=models.CharField(max_length=128,default='abc')
    Diagnosed=models.CharField(max_length=128,default='abc')
    Preference=models.CharField(max_length=128,default='abc')

    
    def __str__(self):
        return self.Allergy


        


class FinancialInfo(models.Model):
    LivingStandard=models.CharField(max_length=128,default='abc')
    OwnLand=models.CharField(max_length=128,default='abc')
    OwnVechile=models.CharField(max_length=128,default='abc')
    Occupation=models.CharField(max_length=128,default='abc')
    AnnualIncome=models.CharField(max_length=128,default='abc')
    BankAccount=models.CharField(max_length=128,default='abc')
    Loan1=models.CharField(max_length=128,default='abc')
    Loan2=models.CharField(max_length=128,default='abc')
    Loan3=models.CharField(max_length=128,default='abc')
    ssi=models.CharField(max_length=128,default='abc')
    remark=models.CharField(max_length=128,default='abc')
    emailID=models.CharField(max_length=128,default='abc')

    def __str__(self):
        return self.LivingStandard

