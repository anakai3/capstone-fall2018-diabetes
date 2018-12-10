# Dataset Cleaning done for Open Food Facts

## Dataset Challenges
* Data is in Tab Separated Format as fields themselves contain comma. 
* Data contains some non-ASCII characters. 
* Data is missing for some columns.
* Serving Sizes are different.
* The country column has sometimes multiple countries in the same field like “United Kingdom, Thailand”.
* The unit of measurements of each ingredient is not clear like joules or kilojoules hence some data transformation may be required.
* OpenFoodFacts.tsv file size is 900+MB, so processing and loading to Redshift has to be managed accordingly.

## Steps to clean the data
* Python libraries to clean the data from openfoodfacts.tsv : numpy, pandas
* Python code to clean the OpenFoodFacts.tsv
* Drop less useful columns
* Ignore nulls
* Extract serving_size into gram value
* 63 columns reduced to 31
* Handle non-ASCII characters
* Save clean data in CSV 