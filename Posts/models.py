from django.db import models
from django.contrib.auth.models import User
from Category.models import Category

# Create your models here.
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)
    posttype = models.CharField(max_length=100,default=None)
    text = models.CharField(max_length=100,default=None)
    video_url = models.CharField(max_length=50,default=None)
    img1 = models.CharField(max_length=100,default=None)
    img2 = models.CharField(max_length=100,default=None)
    img3 = models.CharField(max_length=100,default=None)
    category_id = models.ForeignKey(Category,db_column="category_id",on_delete=models.CASCADE,default=None)
    # islock = models.CharField(max_length=15,default=None,null=True)
    post_date_time = models.DateTimeField(default=None,null=True)
    isdisabled = models.CharField(max_length=15,default=None)
    # isprivate = models.CharField(max_length=15,default=None)
    type = models.CharField(max_length=15,default=None)
    class Meta:
        db_table = "tbl_post"