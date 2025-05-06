from django.db import models
from django.contrib.auth.models import User
from Category.models import Category

# Create your models here.
class PostUserCat(models.Model):
    userpostcat_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,db_column="id",on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,db_column="category_id",on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_postusercat"