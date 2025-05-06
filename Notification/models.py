from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    noti_datetime = models.DateTimeField(default=None,null=True)
    category = models.CharField(max_length=80)

    class Meta:
        db_table = "tbl_notification"