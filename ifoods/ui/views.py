from django.shortcuts import render
from .models import *

import logging,datetime
# Get an instance of a logger
logger = logging.getLogger('django')

# Create your views here.




def index(request):
    restaurants = menu_item_list.objects.values_list('restaurant_name', flat=True).distinct().order_by('restaurant_name')
    #restaurants = list(restaurants)
    return render(request, 'ui/home.html',{'restaurants':restaurants})


def search(request):
    radioSelection = request.GET['radioSelection']
    restaurant = request.GET['restaurant']
    #logger.error('data lenradioSelection:' + str(radioSelection))
    #logger.error('data restaurant:' + str(restaurant))

    data = menu_item_list.objects.filter(restaurant_name=restaurant).order_by('-score')

    data.name = restaurant
    data.header = restaurant
    logger.error('data len:' + str(len(data)))
    numberofRows = str(len(data))
    logger.error('numberofRows:'+numberofRows)

    if numberofRows == "0":
       data.header = "No Result Found For " + restaurant

    return render(request, 'ui/result.html',{'data':data})
