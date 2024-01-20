import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FDAdata = pd.read_csv('./CAERS_ProductBased.csv')
print(FDAdata.shape)
FDAdata_SEX_rem = FDAdata.dropna(subset = ["SEX"])
print(FDAdata_SEX_rem)
women_data = FDAdata_SEX_rem[FDAdata_SEX_rem["SEX"] == "Female"]
print(women_data)
occurrence_data = FDAdata["PRODUCT"].value_counts()
print(occurrence_data)
#Removes rows that contain EXEMPTION 4 in PRODUCTS column
cleaned_data = FDAdata[FDAdata["PRODUCT"] != "EXEMPTION 4"]
print(cleaned_data.shape)
keep_data = occurrence_data[occurrence_data > 2].index
finished_data = cleaned_data[cleaned_data["PRODUCT"].isin(keep_data)]
print(finished_data.shape)