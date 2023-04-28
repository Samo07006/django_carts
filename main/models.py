from django.db import models

class Product(models.Model):
    name = models.CharField('Pr name',max_length=250)
    price = models.PositiveIntegerField('Pr price')
    img = models.ImageField('Pr img',upload_to='images')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    cart_prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField("Product count",blank=True,default=1)

    def __str__(self):
        return self.cart_prod.name