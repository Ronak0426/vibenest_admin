from django.db import models
from States.models import States

# Create your models here.
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    state_id = models.ForeignKey(States,db_column="state_id",on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_city"