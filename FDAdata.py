import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FDAdata = pd.read_csv('./CAERS_ProductBased.csv')
FDAdata_SEX_rem = FDAdata.dropna(subset = ["SEX"])
cleaned_data = FDAdata_SEX_rem[FDAdata_SEX_rem["PRODUCT"] != "EXEMPTION 4"]
cleaned_data["PRODUCT"] = cleaned_data["PRODUCT"].str.lower()
occurrence_data = cleaned_data["PRODUCT"].value_counts()
keep_data = occurrence_data[occurrence_data > 400].index
finished_data = cleaned_data[cleaned_data["PRODUCT"].isin(keep_data)]
#print(occurrence_data)

#lowercases all products 

occurrence_data_2 = finished_data["PRODUCT"].value_counts()
#print(occurrence_data_2)
#print(finished_data.shape)

#Data set only containing SBP product
sbp_df = finished_data[finished_data["PRODUCT"] == "super beta prostate"]
#print(sbp_df.shape)
sbp_df = sbp_df.dropna(subset = "PATIENT_AGE")
#print(sbp_df.shape)

#Data set only containing Vitamin D
vtmd_df = finished_data[finished_data["PRODUCT"] == "vitamin d"]
print(vtmd_df.shape)
gender_counts = vtmd_df["SEX"].value_counts()
category_counts = vtmd_df["CASE_MEDDRA_PREFERRED_TERMS"].value_counts()
print(gender_counts)
print(category_counts)
