from django.db import models
from django.contrib.auth.models import User
from City.models import City

# Create your models here.
class ExtraInfo(models.Model):
    extra_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)
    issequre = models.CharField(max_length=15)
    timing = models.TextField(null=True)
    timechange_date = models.DateField(null=True)
    birthdate = models.DateField(default=None,null=True)
    city_id = models.ForeignKey(City,db_column="city_id",on_delete=models.CASCADE,default=None)
    aboutme = models.CharField(max_length=500,default=None,null=True)
    gender = models.CharField(max_length=10,default=None)
    coverphoto = models.CharField(max_length=50,default=None,null=True)
    profile = models.CharField(max_length=50,default=None,null=True)
    is_online = models.CharField(max_length=5,default=None,null=True)
    

    class Meta:
        db_table = "tbl_extrainfo"