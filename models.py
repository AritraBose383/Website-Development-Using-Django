from django.db import models


# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES=[('M','Male'),('W','Woman'),('O','Others')]
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True)
    email_id=models.EmailField(max_length=255)
    phn_num=models.CharField(max_length=13)
    employee_gender=models.CharField(choices=GENDER_CHOICES,max_length=1)
    employee_address=models.TextField()
    employee_job=models.ManyToManyField('AvailableJobs',blank=True)
    D_o_B=models.DateField()

class AvailableJobs(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

