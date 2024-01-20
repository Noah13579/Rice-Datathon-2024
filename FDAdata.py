import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FDAdata = pd.read_csv('./CAERS_ProductBased.csv')
#print(FDAdata.shape)
FDAdata_SEX_rem = FDAdata.dropna(subset = ["SEX"])
#print(FDAdata_SEX_rem)
women_data = FDAdata_SEX_rem[FDAdata_SEX_rem["SEX"] == "Female"]
#print(women_data)
occurrence_data = FDAdata["PRODUCT"].value_counts()
##print(occurrence_data)
#Removes rows that contain EXEMPTION 4 in PRODUCTS column
cleaned_data = FDAdata[FDAdata["PRODUCT"] != "EXEMPTION 4"]
#print(cleaned_data.shape)
keep_data = occurrence_data[occurrence_data > 475].index
finished_data = cleaned_data[cleaned_data["PRODUCT"].isin(keep_data)]

occurrence_data_2 = finished_data["PRODUCT"].value_counts()
#lowercases all products 
finished_data["PRODUCT"] = finished_data["PRODUCT"].str.lower()
#Data set only containing SBP product
sbp_df = finished_data.dropna(subset = ["SUPER BETA PROSTATE"])
print(sbp_df.shape)
print(finished_data.shape)
#print(occurrence_data_2)