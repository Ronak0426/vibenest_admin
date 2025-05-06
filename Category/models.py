from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_image = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_category"