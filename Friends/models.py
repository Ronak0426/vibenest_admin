from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Friends(models.Model):
    friends_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_id' )
    friend_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='friend_id' )
    status = models.CharField(max_length=30)
    f_datetime = models.DateTimeField()

class Meta:
    db_table = "tbl_friends"