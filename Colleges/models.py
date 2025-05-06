from django.db import models

# Create your models here.
class Colleges(models.Model):
    colleges_id = models.AutoField(primary_key=True)
    colleges_name = models.CharField(max_length=100)
    colleges_logo = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_colleges"