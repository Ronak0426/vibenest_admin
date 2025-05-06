from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MyPhotos(models.Model):
    photo_id = models.AutoField(primary_key=True)
    photo_url = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)



    class Meta:
        db_table = "tbl_myphotos"