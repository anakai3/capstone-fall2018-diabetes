# Open Food Facts #

This folder handles the loading of the file open food facts to Redshift table openfoodfacts
The next step of the application gets the receipe list, parses it and calculates the nutritional value and stores it 
to the table grocery_list

## Load the clean Data into Redshift. ##

* For loading the data since its huge we use the gzip format
* We put a manifest file load.manifest on S3 and use the manifest to load the data
* Load the clean data into Redhsift using the load_open_food.py 

 $ python load_open_food.py

## Run the application ##

* Execute the file process_grocery_list.py as follows
 process_grocery_list.py <path_to_grocery_list_files>
 $ process_grocery_list.py ../input/week1.txt ../input/week2.txt ../input/week3.txt
 
* The files are parsed and the grocery list is read
* The total nutritional values are calculated 
* Output is stored in the table grocery_list to be read by Tableau.