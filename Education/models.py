from django.db import models
from django.contrib.auth.models import User
from Colleges.models import Colleges
from Degrees.models import Degrees

# Create your models here.
class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)
    colleges_id = models.ForeignKey(Colleges,db_column="colleges_id",on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    degree_id = models.ForeignKey(Degrees,db_column="degree_id",on_delete=models.CASCADE)
    description = models.CharField(max_length=250,default=None)

    class Meta:
        db_table = "tbl_education"