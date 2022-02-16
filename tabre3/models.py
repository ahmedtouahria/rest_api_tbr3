from uuid import *
import uuid
from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator ,MaxValueValidator
# Create your models here.

class Motabari3(models.Model):
    zomra_choice = [
        ('O+', 'O+'),
        ('A+', 'A+'),
        ('AB+', 'AB+'),
        ('B+', 'B+'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),
        ('A-', 'A-'),
        ('B-', 'B-'),  
    ]
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=200,null=False,blank=False)
    age=models.IntegerField(validators=[MinValueValidator(15),MaxValueValidator(80)],error_messages={"age":"Age must be greater than 15"})
    wilaya=models.CharField(max_length=200,null=False,blank=False)
    commun=models.CharField(max_length=200,null=False,blank=False)
    phone=models.CharField(max_length=10,null=False,blank=False)
    zomra = models.CharField(choices=zomra_choice,null=False,blank=False,max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not len(self.phone) == 10:
            raise ValidationError({"phone":"Phone number wrong"})    
        
       
    def __str__(self) -> str:
        return str(self.name) 
       
