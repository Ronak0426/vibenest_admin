from django.db import models
from Posts.models import Posts
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comments = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE,default=None)
    post_id = models.ForeignKey(Posts,db_column="post_id",on_delete=models.CASCADE,default=None)
    comment_datetime = models.DateTimeField(default=now,null=True)


    class Meta:
        db_table = "tbl_comments"