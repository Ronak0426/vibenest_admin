from django.db import models
from Posts.models import Posts
from django.contrib.auth.models import User

# Create your models here.
class Likes(models.Model):
    lid = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Posts,db_column="post_id",on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


    class Meta:
        db_table = "tbl_like/dislike"