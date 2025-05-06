from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SocialTime(models.Model):
    truck_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE,default=None)
    start_datetime = models.DateTimeField(default=None)
    end_datetime = models.DateTimeField(default=None,null=True)
    social_date = models.DateField(default=None)
    type = models.CharField(max_length=30,default=None)

    class Meta:
        db_table = "tbl_socialtime"