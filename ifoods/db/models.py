from django.db import models

# Create your models here.
# menu_item_id,restaurant_id,restaurant_name,item,amount,unit,energy_kcal,protein,fiber,fat,sugar,carbohydrates,cholesterol
#class menu_item_list(models.Model):
#    menu_item_id = models.CharField(max_length=800)
#    restaurant_id = models.DecimalField(max_digits=12,decimal_places=5)
#    restaurant_name= models.CharField(max_length=800)
#    item = models.CharField(max_length=800)
#    amount = models.DecimalField(max_digits=12,decimal_places=5)
#    unit= models.CharField(max_length=50)
#    energy_kcal= models.DecimalField(max_digits=12,decimal_places=5)
#    protein= models.DecimalField(max_digits=12,decimal_places=5)
#    fiber= models.DecimalField(max_digits=12,decimal_places=5)
#    fat= models.DecimalField(max_digits=12,decimal_places=5)
#    sugar= models.DecimalField(max_digits=12,decimal_places=5)
#    carbohydrates= models.DecimalField(max_digits=12,decimal_places=5)
#    cholesterol= models.DecimalField(max_digits=12,decimal_places=5)
#
#    class Meta:
#        # This model is not managed by Django
#        managed = False
#        db_table = 'menu_item_list'
#
#    def __str__(self):
#        return self.item