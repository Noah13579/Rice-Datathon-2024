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

#MultiVitamin Data Split into Sexes
multivitamin_data = finished_data[finished_data["PRODUCT"] == "multivitamin"]
multivitamin_data["SEX"] = multivitamin_data["SEX"].str.lower()
multivit_wom_data = multivitamin_data[multivitamin_data["SEX"] != "male"]
multivit_male_data = multivitamin_data[multivitamin_data["SEX"] != "female"]

#MultiVitamin Data Split into Age Groups
multi_vit_baby = multivitamin_data[multivitamin_data["PATIENT_AGE"] < 5] #8 babies
multi_vit_todd = multivitamin_data[multivitamin_data["PATIENT_AGE"] > 5]
multi_vit_todd = multi_vit_todd[multi_vit_todd["PATIENT_AGE"] < 13] #19 kids
multi_vit_teen = multivitamin_data[multivitamin_data["PATIENT_AGE"] > 12]
multi_vit_teen = multi_vit_teen[multi_vit_teen["PATIENT_AGE"] < 21]
multi_vit_adult = multivitamin_data[multivitamin_data["PATIENT_AGE"] > 20]
multi_vit_adult = multi_vit_adult[multi_vit_adult["PATIENT_AGE"] < 65] #729 adults
multi_vit_sen = multivitamin_data[multivitamin_data["PATIENT_AGE"] > 65] #310 seniors

#Splices SBP data into age groups 
sbp_df_baby = sbp_df_men[sbp_df_men["PATIENT_AGE"] < 5] #no babies
sbp_df_toddler = sbp_df_men[(sbp_df_men["PATIENT_AGE"] >= 5) & (sbp_df_men["PATIENT_AGE"] < 13)] #no toddlers
age_counts = sbp_df_men["PATIENT_AGE"].value_counts()
age_array = []
number_reports = []
for age, reports in age_counts.items():
    age_array.append(age)
    number_reports.append(age_counts[age])
# plt.plot(age_array, number_reports)
# plt.show()

#Data set only containing vitamin products
vtmd_df = finished_data[finished_data["PRODUCT"] == "vitamin d"]
gender_counts = vtmd_df["SEX"].value_counts()
category_counts = vtmd_df["CASE_MEDDRA_PREFERRED_TERMS"].value_counts()


#Data set only containing Vitamin D
vtmd_df = finished_data[finished_data["PRODUCT"] == "vitamin d"]


vtmd_df = vtmd_df[vtmd_df["SEX"]!="Not Reported"]


# Create the bar plot
plt.figure(figsize=(10, 6)) 


sns.barplot(data=vtmd_df, x="PRODUCT", y="PATIENT_AGE", hue="SEX", errorbar=None)

plt.xlabel("Products")
plt.ylabel("Average Age")
plt.title("Average Age by Products and Sex")

# Show the plot
plt.legend(title="Sex", loc="upper right")
plt.show()