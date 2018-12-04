from django.db import models

# Create your models here.
# menu_item_id,restaurant_id,restaurant_name,item,amount,unit,energy_kcal,protein,fiber,fat,sugar,carbohydrates,cholesterol
class menu_item_list(models.Model):
    menu_item_id = models.DecimalField(max_digits=12,decimal_places=5,primary_key=True)
    restaurant_id = models.CharField(max_length=800)
    restaurant_name= models.CharField(max_length=800)
    item = models.CharField(max_length=800)
    food_type = models.CharField(max_length=80)
    food_url = models.CharField(max_length=800)
    calcium= models.DecimalField(max_digits=12,decimal_places=5)
    amount = models.DecimalField(max_digits=12,decimal_places=5)
    unit= models.CharField(max_length=50)
    number_of_units= models.DecimalField(max_digits=12,decimal_places=5)
    energy_kcal= models.DecimalField(max_digits=12,decimal_places=5)
    protein= models.DecimalField(max_digits=12,decimal_places=5)
    fiber= models.DecimalField(max_digits=12,decimal_places=5)
    fat= models.DecimalField(max_digits=12,decimal_places=5)
    sugar= models.DecimalField(max_digits=12,decimal_places=5)
    carbohydrates= models.DecimalField(max_digits=12,decimal_places=5)
    cholesterol= models.DecimalField(max_digits=12,decimal_places=5)
    iron= models.DecimalField(max_digits=12,decimal_places=5)
    measurement_description= models.CharField(max_length=80)
    monounsaturated_fat= models.DecimalField(max_digits=12,decimal_places=5)
    polyunsaturated_fat= models.DecimalField(max_digits=12,decimal_places=5)
    potassium= models.DecimalField(max_digits=12,decimal_places=5)
    saturated_fat= models.DecimalField(max_digits=12,decimal_places=5)
    serving_description= models.CharField(max_length=80)
    serving_id= models.DecimalField(max_digits=22,decimal_places=5)
    serving_url= models.CharField(max_length=800)
    sodium= models.DecimalField(max_digits=12,decimal_places=5)
    trans_fat= models.DecimalField(max_digits=12,decimal_places=5)
    vitamin_a= models.DecimalField(max_digits=12,decimal_places=5)
    vitamin_c= models.DecimalField(max_digits=12,decimal_places=5)
    serving_description_size= models.CharField(max_length=20)
    serving_description_unit= models.CharField(max_length=800)
    score= models.DecimalField(max_digits=12,decimal_places=5)

    class Meta:
        # This model is not managed by Django
        managed = False
        db_table = 'restaurant_menu_list'

    def __str__(self):
        return self.item
