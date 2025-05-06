from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Career(models.Model):
    career_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    class Meta:
        db_table = "tbl_career"