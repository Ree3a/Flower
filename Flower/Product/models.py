from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField(auto_created=True, primary_key=True)
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name

    class Meta:
        db_table='product_tbl'