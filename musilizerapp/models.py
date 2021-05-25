from django.db import models
from django.conf import settings
import os.path


# Add this method to your model

# Create your models here.
class Entry(models.Model):
    unique_number = models.IntegerField()
    set_to_expire = models.CharField(max_length=1,default='n')
    file_name = models.CharField(max_length=100,default='UN-NAMED')
    audio_file = models.CharField(max_length=100,default='sadface.mp3')

    def __str__(self):
        return self.file_name

