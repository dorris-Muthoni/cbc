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
    fname = models.CharField
    mname = models.CharField
    lname = models.CharField
    dob = models.DateField
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    phone_number = models.CharField
    email = models.EmailField
    address = models.CharField
    city = models.CharField
    state = models.CharField
    zip_code = models.CharField
    
    def __str__(self):
        return self.fname 
    
class Upload(models.Model):
    Birth_Certificate = models.FileField(upload_to='documents/')#birth certificate
    KCPE_Result_Slip = models.FileField(upload_to='documents/')
    Leaving_Certificate = models.FileField(upload_to='documents/')
    Medical_Examination_Form = models.FileField(upload_to='documents/')
    Fee_Payment_Receipt = models.FileField(upload_to='documents/')
    certificate_of_Good_Conduct = models.FileField(upload_to='documents/')
    passport = models.ImageField(default='', blank=True)
    photo_id = models.ImageField(default='', blank=True) #photocopy id parent
    intake = models.ForeignKey(Intake,choices=INTAKE, default='S', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.intake
       