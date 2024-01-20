import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FDAdata = pd.read_csv('./CAERS_ProductBased.csv')
FDAdata_SEX_rem = FDAdata.dropna(subset = ["SEX"])
cleaned_data = FDAdata_SEX_rem[FDAdata_SEX_rem["PRODUCT"] != "EXEMPTION 4"]
cleaned_data["PRODUCT"] = cleaned_data["PRODUCT"].str.lower()
cleaned_data["DESCRIPTION"] = cleaned_data["DESCRIPTION"].str.lower()
cleaned_data["CASE_MEDDRA_PREFERRED_TERMS"] = cleaned_data["CASE_MEDDRA_PREFERRED_TERMS"].str.lower()
cleaned_data["CASE_OUTCOME"] = cleaned_data["CASE_OUTCOME"].str.lower()


occurrence_data = cleaned_data["PRODUCT"].value_counts()
keep_data = occurrence_data[occurrence_data > 400].index
finished_data = cleaned_data[cleaned_data["PRODUCT"].isin(keep_data)]

occurrence_data_2 = finished_data["PRODUCT"].value_counts()

#Data set only containing SBP product reported by men (only one woman reported)
sbp_df = finished_data[finished_data["PRODUCT"] == "super beta prostate"] #shape = (1036, 13)
sbp_df = sbp_df.dropna(subset = "PATIENT_AGE") #shape = (511, 13)
sbp_df_men = sbp_df[sbp_df["SEX"] == "Male"] #shape = (510, 13)

#Data set only containing SBP product
sbp_df = finished_data[finished_data["PRODUCT"] == "super beta prostate"]
sbp_df = sbp_df.dropna(subset = "PATIENT_AGE")

#multivitamin data
multivitamin_data = finished_data[finished_data["PRODUCT"] == "multivitamin"]
multivitamin_data["SEX"] = multivitamin_data["SEX"].str.lower()
multivit_wom_data = multivitamin_data[multivitamin_data["SEX"] != "male"]
multivit_male_data = multivitamin_data[multivitamin_data["SEX"] != "female"]

#Splices SBP data into age groups 
sbp_df_baby = sbp_df_men[sbp_df_men["PATIENT_AGE"] < 5] #no babies
sbp_df_toddler = sbp_df_men[(sbp_df_men["PATIENT_AGE"] >= 5) & (sbp_df_men["PATIENT_AGE"] < 13)] #no toddlers
print(sbp_df_men.shape)
age_counts = sbp_df_men["PATIENT_AGE"].value_counts()
print(age_counts)

#Data set only containing Vitamin D
vtmd_df = finished_data[finished_data["PRODUCT"] == "vitamin d"]
#print(vtmd_df.shape)
gender_counts = vtmd_df["SEX"].value_counts()
category_counts = vtmd_df["CASE_MEDDRA_PREFERRED_TERMS"].value_counts()
age_counts = vtmd_df["PATIENT_AGE"].value_counts()
age_categories = {"<5":0, "<13":0, "<21":0, "<65":0, "65+":0}
# for key, value in age_counts.items():
#     if int(key) < 5:
#         age_categories["<5"] += int(value)
#     elif int(key) < 13:
#         age_categories["<13"] += int(value)
#     elif int(key) < 21:
#         age_categories["<21"] += int(value)
#     elif int(key) < 65:
#         age_categories["<65"] += int(value)
#     else:
#         age_categories["65+"] += int(value)

ages = []
occurences = []
for age, amount in age_counts.items():
    ages.append(age)
    occurences.append(amount)
# print(gender_counts)
# print(category_counts)
# print(age_categories)
        
plt.scatter(ages, occurences)
plt.show()