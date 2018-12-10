# Open Food Facts Original Dataset
1. The Open food facts dataset is around 1 GB. It has French and US food datatypes.
2. The data can be downloaded from the Kaggle Website from: https://www.kaggle.com/sarapissou/open-food-facts/data
3. This needs a Kaggle username and password.

It is not possible to script the data download using wget or curl as the SSL certificates do not match.

The clean up of this dataset is handled in the preprocess directory which has its own Readme.

# Food and Nutrition information dataset 
1. This dataset is a digest of food and nutrition information from data.gov.
2. The overall size of the dataset is around 40 MB.
3. The digest is around 1.2 MB and can be obtained from https://www.ars.usda.gov/ARSUserFiles/80400525/Data/SR/SR28/dnload/sr28abbr.zip
4. Run the script at ../setup/extract_data_from_data_gov.sh to download and uncompress the dataset.

