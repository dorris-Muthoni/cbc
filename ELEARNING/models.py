from django.db import models



GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
INTAKE = [
    ('J', 'January Intake'),
    ('A', 'April Intake'),
    ('S', 'September Intake'),
]
# Create your models here.
class Intake(models.Model):  #Intake  form that will be stored as the student's personal details
    fname = models.CharField('First Name', default='Unknown', max_length=20)
    mname = models.CharField('Middle Name', default='Unknown', max_length=20)
    lname = models.CharField('Last Name',default='Unknown', max_length=20)
    dob = models.CharField(max_length=20, default='DEFAULT VALUE', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    phone_number = models.CharField(max_length=20, default='DEFAULT VALUE', blank=True, null=True)
    email = models.CharField(max_length=20, default='DEFAULT VALUE', blank=True, null=True)
    address = models.CharField(max_length=20, default='DEFAULT VALUE', blank=True, null=True)
    city = models.CharField(max_length=20, default='DEFAULT VALUE', blank=True, null=True)
    state = models.CharField(max_length=20, default='DEFAULT VALUE', blank=True, null=True)
    zip_code = models.CharField(max_length=20, default='DEFAULT VALUE', blank=True, null=True)
    
    def __str__(self):
        return self.fname 
    
class Upload(models.Model):
    Birth_Certificate = models.FileField(upload_to='documents/')#birth certificate
    KCPE_Result_Slip = models.FileField(upload_to='documents/')
    Leaving_Certificate = models.FileField(upload_to='documents/')
    Medical_Examination_Form = models.FileField(upload_to='documents/')
    Fee_Payment_Receipt = models.FileField(upload_to='documents/')
    certificate_of_Good_Conduct = models.FileField(upload_to='documents/')
    passport = models.ImageField(upload_to='document/')
    photo_id = models.ImageField(upload_to='document/',) #photocopy id parent
    intake = models.ForeignKey(Intake,choices=INTAKE, default='S', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.intake
       