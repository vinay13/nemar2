from django.db import models
from django.db import connection
#from django.contrib.auth.models import AbstractBaseUser



class SocialInfo(models.Model):
    firstname=models.CharField(max_length=128,default='abc')
    lastname=models.CharField(max_length=128,default='s')
    dob=models.CharField(max_length=128,default='ds')
    contactno=models.IntegerField(default=1)
    fathername=models.CharField(max_length=128,default='ds')
    fdob=models.CharField(max_length=128,default='ds')
    fcontactno=models.IntegerField(default=1)
    mothername=models.CharField(max_length=128,default='ds')
    mdob=models.CharField(max_length=128,default='ds')
    mcontactno=models.IntegerField(default=0)
    gender=models.CharField(max_length=128,default='ds')
    siblings=models.CharField(max_length=128,default='ds')
    spouseName=models.CharField(max_length=128,default='ds')
    sDOB=models.CharField(max_length=128,default='ds')
    marriagedate=models.CharField(max_length=128,default='ds')
    children=models.IntegerField(default=0)
    girlCount=models.IntegerField(default=0)
    birthplace=models.CharField(max_length=128,blank=True)
    delivery=models.CharField(max_length=128,blank=True)
    domicile=models.CharField(max_length=128,blank=True)
    yearofliving=models.CharField(max_length=128,blank=True)
    #lastInsert_Id=property(n_search)



#insert array data into social_info and then generate a last_inserted_id and post array data in health n finance on basis of id.
    def n_search(self):
        cur=connection.cursor()
        cur.execute('select FirstName from patient_socialinfo')
        results = cur.fetchall()  
       # cur.close()  
  
        # wrap the results up into Document domain objects   
        #return self._foobar
        return results

    
    custom_id=property(n_search)


    def __str__(self):
        return self.FirstName




class HealthInfo(models.Model):
    Allergy=models.CharField(max_length=128,default='abc')
    PhysicalChallenged=models.CharField(max_length=128,default='abc')
    #uuid=models.ForeignKey(Account)
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

"""
    def get_last_id(self):
        return self.uuid.lastinsertedId
"""

"""
    def push_array_data(self,uuid):
        cur=connection.cursor()
        cur.execute('SELECT my_insert("Health_data") where Id is %s,[uuid,]')
        results = cur.fetchone()  
        cur.close()

        return something
"""

    
    
class FinancialInfo(models.Model):
    LivingStandard=models.CharField(max_length=128,default='abc')
    #uuid=models.ForeignKey(Account)
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




class ContactInfo(models.Model):
    id=models.AutoField(primary_key=True)
    #uuid=models.ForeignKey(Account)
    state=models.CharField(max_length=128,default='MP')
    city=models.CharField(max_length=128,default='jbp')
    street=models.CharField(max_length=128,default='gandhi_road')
    alt_contactno=models.IntegerField(default='+91')
    zipcode=models.IntegerField(default=0)
    conactno=models.IntegerField(default='+91')
    emailid=models.CharField(max_length=123,default='abc@gmail.com')
    #zone=models.CharField(max_length=123,default='sdsa')
    address=models.CharField(max_length=123,default='fdsd')
    coordinate=models.IntegerField(default=1)


    def __str__(self):
        return self.state


# Create your models here.

"""
class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

"""
