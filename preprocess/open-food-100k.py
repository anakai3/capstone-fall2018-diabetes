import numpy as np
import pandas as pd



# ### User-defined functions
def remove_na_rows(df, cols=None):
    """
    remove row with NaN in any column
    """
    if cols is None:
        cols = df.columns
    return df[np.logical_not(np.any(df[cols].isnull().values, axis=1))]

def trans_country_name(x):
    """
    translate country name to code (2-char)
    """
    try:
        country_name = x.split(',')[0]
        if country_name in dictCountryName2Code:
            return dictCountryName2Code[country_name]
    except:
        return None

def parse_additives(x):
    """
    parse additives column values into a list
    """
    try:
        dict = {}
        for item in x.split(']'): 
            token = item.split('->')[0].replace("[", "").strip() 
            if token: dict[token] = 1
        return [len(dict.keys()),  sorted(dict.keys())]
    except:
        return None

def trans_serving_size(x):
    """
    pick up gram value from serving_size column
    """
    try:
        serving_g = float((x.split('(')[0]).replace("g", "").strip())
        return serving_g
    except:
        return 0.0

food = pd.read_excel("data/open_food_full.xlsx")

columns_to_keep = ['code','product_name','created_datetime','brands','energy_100g','fat_100g','saturated-fat_100g','trans-fat_100g','cholesterol_100g','carbohydrates_100g','sugars_100g','fiber_100g','proteins_100g','salt_100g','sodium_100g','vitamin-a_100g','vitamin-c_100g','calcium_100g','iron_100g','ingredients_text','countries','countries_en','serving_size','additives','nutrition_grade_fr','nutrition-score-fr_100g','url']

food = food[columns_to_keep]

columns_numeric_all = ['energy_100g','fat_100g','saturated-fat_100g','trans-fat_100g','cholesterol_100g','carbohydrates_100g','sugars_100g','omega-3-fat_100g','omega-6-fat_100g','fiber_100g','proteins_100g','salt_100g','sodium_100g','alcohol_100g','vitamin-a_100g','vitamin-c_100g','potassium_100g','chloride_100g','calcium_100g','phosphorus_100g','iron_100g','magnesium_100g','zinc_100g','copper_100g','manganese_100g','fluoride_100g','nutrition-score-fr_100g','nutrition-score-uk_100g']

columns_numeric = set(columns_numeric_all) & set(columns_to_keep)

columns_categoric = set(columns_to_keep) - set(columns_numeric)

# turn off
if False:
    for col in columns_numeric:
        if not col in ['nutrition-score-fr_100g', 'nutrition-score-uk_100g']:
            food[col] = food[col].fillna(0)

    for col in columns_categoric:
        if col in ['nutrition_grade_fr', 'nutrition_grade_uk']:
            food[col] = food[col].fillna('-')
        else:        
            food[col] = food[col].fillna('')


# list column names: categoric vs numeric
columns_categoric, columns_numeric

# standardize country
country_lov = pd.read_excel("data/country_cd.xlsx")

dictCountryCode2Name = {}
dictCountryName2Code = {}
for i in country_lov.index:
    dictCountryCode2Name[country_lov.ix[i,'GEOGRAPHY_CODE']] = country_lov.ix[i,'GEOGRAPHY_NAME']
    dictCountryName2Code[country_lov.ix[i,'GEOGRAPHY_NAME']] = country_lov.ix[i,'GEOGRAPHY_CODE']    


# add Country_Code column - pick 1st country from list
food['countries_en'] = food['countries_en'].fillna('')
food['country_code'] = food['countries_en'].apply(str).apply(lambda x: trans_country_name(x))

# add country_code to columns_categoric set
columns_categoric.add('country_code')

# verify bad country
food[food['country_code'] != food['countries']][['country_code', 'countries']].head(20)

food['ingredients_text'].head()  # leave as is


# ### Extract serving_size into gram value

# add serving_size in gram column
food['serving_size'].head(10)

food['serving_size'] = food['serving_size'].fillna('')
food['serving_size_gram'] = food['serving_size'].apply(lambda x: trans_serving_size(x))

# add serving_size_gram 
columns_numeric.add('serving_size_gram')

food[['serving_size_gram', 'serving_size']].head()


# ### Parse additives

food['additives'] = food['additives'].fillna('')
food['additive_list'] = food['additives'].apply(lambda x: parse_additives(x))

# add additive_list 
columns_categoric.add('additive_list')


food["creation_date"] = food["created_datetime"].apply(str).apply(lambda x: x[:x.find("T")])

def extract_year(x):
    try:
        return int(x[:x.find("-")])
    except:
        return None
    
food["year_added"] = food["created_datetime"].dropna().apply(str).apply(extract_year)


# add creation_date 
columns_categoric.add('creation_date')
columns_numeric.add('year_added')


food[['created_datetime', 'creation_date', 'year_added']].head()


# Save the dataframe as a csv

food.to_csv("open_food_clean.csv", encoding="utf-8")



