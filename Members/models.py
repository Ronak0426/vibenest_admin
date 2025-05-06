from django.db import models
from django.contrib.auth.models import User
from Groups.models import UserGroups

# Create your models here.
class Members(models.Model):
    member_id = models.AutoField(primary_key=True,default=None)
    groups_id = models.ForeignKey(UserGroups,db_column="groups_id",on_delete=models.CASCADE,default=None)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE,default=None)
    f_datetime = models.DateTimeField(default=None)
    status = models.CharField(max_length=30,default=None)

class Meta:
    db_table = "tbl_members"