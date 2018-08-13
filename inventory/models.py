from django.db import models

class Inventory (models.Model):
    partNum = models.CharField(max_length=25)  
    partDesc = models.CharField(max_length=50)  
    lineLoc = models.CharField(max_length=25)  
    lineQuantity = models.CharField(max_length=5)
    lineMakeup = models.CharField(max_length=5)
    sysQuantity = models.CharField(max_length=5)
    comments = models.CharField(max_length=100)
    class Meta:  
        db_table = "inventory"  
		
	