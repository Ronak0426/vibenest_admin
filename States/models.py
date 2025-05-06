from django.db import models

# Create your models here.
class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=100)
    state_image = models.CharField(max_length=100,default=None)

    class Meta:
        db_table = "tbl_state"