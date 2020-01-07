from django.db import models

# Create your custom models here.
class Student(models.Model):
    
     # define the model fiellds
     fullname = models.CharField(max_length=100)
     age = models.DecimalField(max_digits=10, decimal_places=0)
     balance = models.DecimalField(max_digits=10, decimal_places=2, default=9.99)
     address = models.TextField()
     notes = models.TextField()

     # define the string constructor
     def __str__(self):
         return self.fullname