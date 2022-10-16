from django.db import models
from django.contrib.auth.models import AbstractUser


class Myuser(AbstractUser):
    email=models.EmailField(max_length = 254,null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)
    first_name=models.CharField(max_length=200,null=True,blank=True)
    last_name=models.CharField(max_length=200,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profile/',null=True,blank=True)
    mobile_number=models.CharField(max_length=200,null=True,blank=True)
    age=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.first_name)
    class Meta:
        managed=True
        db_table='tbl_newuser'