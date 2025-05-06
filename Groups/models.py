from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserGroups(models.Model):
    groups_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=35)
    group_logo = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_groups"