from django.db import models
from django.contrib.auth.models import User
from Groups.models import UserGroups

# Create your models here.
class GroupChat(models.Model):
    grpchat_id = models.AutoField(primary_key=True)
    groups_id = models.ForeignKey(UserGroups,db_column="groups_id",on_delete=models.CASCADE)
    groups_message = models.TextField()
    sender_id = models.ForeignKey(User, db_column="id", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_groupchat"
