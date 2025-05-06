from django.db import models

# Create your models here.
class Degrees(models.Model):
    degree_id = models.AutoField(primary_key=True)
    degree_name = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_degree"