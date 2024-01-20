import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FDAdata = pd.read_csv('./CAERS_ProductBased.csv')
occurrence_data = FDAdata["PRODUCT"].value_counts()
print(occurrence_data)
#Removes rows that contain EXEMPTION 4 in PRODUCTS column
cleaned_data = FDAdata[FDAdata["PRODUCT"] != "EXEMPTION 4"]
print(cleaned_data.shape)
for product in occurrence_data.keys():
    if int(occurrence_data[product]) == 1:
        cleaned_data = FDAdata[FDAdata["PRODUCT"] != product]
print(cleaned_data.shape)
