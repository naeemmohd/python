from django.db import models
import random, os

def getFormattedMediaFileandExtn(filepath):
        base_path = os.path.basename(filepath)
        fileName, fileExtn = os.path.splitext(base_path)
        return fileName, fileExtn

def getFormattedMediaFileName(instance, filename):
        fileName, fileExtn = getFormattedMediaFileandExtn(filename)
        newfileName= random.randint(10000, 99999)
        print(instance)
        return 'file{0}{1}'.format(newfileName, filename, fileExtn)

# Create your custom models here.
class Student(models.Model):
    
     # define the model fiellds
     fullname = models.CharField(max_length=100)
     age = models.DecimalField(max_digits=10, decimal_places=0)
     balance = models.DecimalField(max_digits=10, decimal_places=2, default=9.99)
     address = models.TextField()
     notes = models.TextField()

     # FileUpload and ImageUpload fields
     fileupload = models.FileField(upload_to=getFormattedMediaFileName, null=True, blank=True)
     imageUpload = models.ImageField(upload_to=getFormattedMediaFileName, null=True, blank=True) 


     # define the string constructor
     def __str__(self):
         return self.fullname