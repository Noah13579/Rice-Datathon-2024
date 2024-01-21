import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

#reads data file and removes rows with EXEMPTION 4 in PRODUCT column
FDAdata = pd.read_csv('./CAERS_ProductBased.csv')
cleaned_data = FDAdata[FDAdata["PRODUCT"] != "EXEMPTION 4"]

#transforms columns into lowercase
cleaned_data.loc[:, "PRODUCT"] = cleaned_data["PRODUCT"].str.lower()
cleaned_data.loc[:, 'DESCRIPTION'] = cleaned_data["DESCRIPTION"].str.lower()
cleaned_data.loc[:, 'CASE_MEDDRA_PREFERRED_TERMS'] = cleaned_data["CASE_MEDDRA_PREFERRED_TERMS"].str.lower()
cleaned_data.loc[:, 'CASE_OUTCOME'] = cleaned_data["CASE_OUTCOME"].str.lower()
cleaned_data.loc[:, 'SEX'] = cleaned_data["SEX"].str.lower()

#Noah

#combining supplements
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data["PRODUCT"].replace("(.*fish oil.*)|(.*omega 3.*)|(.*omega-3.*)", "fish oil", regex = True)
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace(".*prevagen.*", "prevagen", regex = True)
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace('(.*co q-10.*)|(.*coq10.*)', "coq-10", regex = True)
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace('.*hydroxycut.*', "hydroxycut", regex = True)
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace('.*probiotics*.*', "probiotic", regex = True)
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace('.*beta prostate.*', 'beta prostate', regex = True)




# supp_products = cleaned_data[cleaned_data["PRODUCT"].str.contains("(fish oil)|(omega-3)|(omega3)|(Prevagen)|(Co q-10)|(coq10)|(Hydroxycut)|(probiotics*)|(beta prostate)", case=False, na=False, regex = True)]
# supp_deaths = supp_products[supp_products["CASE_OUTCOME"].str.contains("deaths*", case=False, na=False, regex = True)]
#print(supp_deaths)











#

#Aden
#combinining vitamin B products
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace("(.*vitamin b.*)|(.*vitamin b6.*)|(.*b complex.*)|(.*b12.*)|(.*b-12.*)|(.*vitamin b complex.*)", "vitamin b", regex = True)
#Combining vitamin D products
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace("(.*vit-d.*)|(.*vitamin d.*)|(.*vitamin d3.*)|(.*d3.*)", "vitamin d", regex = True)
#Combining vitamin C products
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace("(.*vitamin c.*)|(.*emergen-c.*)", "vitamin c", regex = True)
#Combining Vitamin A
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace("(.*vitamin a.*)", "vitamin a", regex = True)
#Combining Multivitamins
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace("(.*multivitamin.*)|(.*multi vitamin.*)|(.*multi-vitamin.*)|(.*one a day.*)|(.*prenatal vitamins.*)", "multi vitamin", regex = True)
#Combining Centrum
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace("(.*centrum.*)", "centrum vitamins", regex = True)
















#

#Angel

#combining quorn products 
#occ_df = cleaned_data[cleaned_data["PRODUCT"].str.contains("quorn", case=False, na=False)]
#print("Here")
#print(occ_df['PRODUCT'].value_counts())
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace(".*quorn.*", "quorn product", regex = True)
#print("Here")
#print(f'count is {cleaned_data["PRODUCT"].value_counts()["quorn product"]}')
#combining peanut buttters
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace("(.*peanut\sbutter.*)|(.*peanutbutter.*)", "peanut butter", regex = True)

#combining chobanis
cleaned_data.loc[:, 'PRODUCT'] = cleaned_data['PRODUCT'].replace('.*chobani.*', 'chobani', regex = True)



#print(cleaned_data['PRODUCT'].value_counts()["centrum vitamins"])













occurrence_data = cleaned_data["PRODUCT"].value_counts()

# with open("unique_prod.csv", 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(['PRODUCT','NO. of OCCURRENCES'])
#     for product, count in occurrence_data.items():
#         csvwriter.writerow([product, count])

#Surface cleaned dataset from which our other datasets are derived
keep_data = occurrence_data[occurrence_data > 500].index
finished_data = cleaned_data[cleaned_data["PRODUCT"].isin(keep_data)]

occurrence_data_2 = finished_data["PRODUCT"].value_counts()
#print(occurrence_data_2)

death_data = cleaned_data[cleaned_data["CASE_OUTCOME"].str.contains("death", case = False, regex = True)]
occurrence_data_3 = death_data["PRODUCT"].value_counts()
kratom_death = death_data[death_data["PRODUCT"].str.contains('kratom')]
print(kratom_death)
occurrence_death = kratom_death['PATIENT_AGE'].value_counts()
print(occurrence_death)
kratom_death_baby = kratom_death[kratom_death["PATIENT_AGE"] < 5]
kratom_death_todd = kratom_death[kratom_death["PATIENT_AGE"] > 5]
kratom_death_todd = kratom_death[kratom_death["PATIENT_AGE"] < 13]
kratom_death_teen = kratom_death[kratom_death["PATIENT_AGE"] > 12]
kratom_death_teen = kratom_death[kratom_death["PATIENT_AGE"] < 21]
kratom_death_adult_y = kratom_death[kratom_death["PATIENT_AGE"] > 20]
kratom_death_adult_y = kratom_death[kratom_death["PATIENT_AGE"] < 40]
kratom_death_adult_o = kratom_death[kratom_death["PATIENT_AGE"] > 39]
kratom_death_adult_o = kratom_death[kratom_death["PATIENT_AGE"] < 65]
kratom_death_sen = kratom_death[kratom_death["PATIENT_AGE"] > 65]
counts = [
    kratom_death_baby.shape[0] +
    kratom_death_todd.shape[0] +
    kratom_death_teen.shape[0],
    kratom_death_adult_y.shape[0],
    kratom_death_adult_o.shape[0],
    kratom_death_sen.shape[0]
]
labels = ['0-20', '21-40', '41-64','65+']
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Kratom Deaths by Age Group')
plt.show()

#Data set only containing SBP product
# sbp_df = finished_data[finished_data["PRODUCT"] == "super beta prostate"] #shape = (1036, 13)
# #Drop rows without anything in PATIENT_AGE
# sbp_df = sbp_df.dropna(subset = "PATIENT_AGE") 

# #Data set only containing SBP product reported by men (only one woman reported)
# sbp_df_men = sbp_df[sbp_df["SEX"] == "Male"] #shape = (510, 13)


# #MultiVitamin Data Split into Sexes
# multivitamin_data = finished_data[finished_data["PRODUCT"] == "multivitamin"]
# multivit_wom_data = multivitamin_data[multivitamin_data["SEX"] != "male"]
# multivit_male_data = multivitamin_data[multivitamin_data["SEX"] != "female"]

# #MultiVitamin Data Split into Age Groups
# multi_vit_baby = multivitamin_data[multivitamin_data["PATIENT_AGE"] < 5] #8 babies
# multi_vit_todd = multivitamin_data[multivitamin_data["PATIENT_AGE"] > 5]
# multi_vit_todd = multi_vit_todd[multi_vit_todd["PATIENT_AGE"] < 13] #19 kids
# multi_vit_teen = multivitamin_data[multivitamin_data["PATIENT_AGE"] > 12]
# multi_vit_teen = multi_vit_teen[multi_vit_teen["PATIENT_AGE"] < 21]
# multi_vit_adult = multivitamin_data[multivitamin_data["PATIENT_AGE"] > 20]
# multi_vit_adult = multi_vit_adult[multi_vit_adult["PATIENT_AGE"] < 65] #729 adults
# multi_vit_sen = multivitamin_data[multivitamin_data["PATIENT_AGE"] > 65] #310 seniors

# #Splices SBP data into age groups 
# sbp_df_baby = sbp_df_men[sbp_df_men["PATIENT_AGE"] < 5] #no babies
# sbp_df_toddler = sbp_df_men[(sbp_df_men["PATIENT_AGE"] >= 5) & (sbp_df_men["PATIENT_AGE"] < 13)] #no toddlers
# age_counts = sbp_df_men["PATIENT_AGE"].value_counts()
# age_array = []
# number_reports = []
# for age, reports in age_counts.items():
#     age_array.append(age)
#     number_reports.append(age_counts[age])
# plt.scatter(age_array, number_reports)
# #plt.show()

# #Data set only containing vitamin products
# vtmd_df = finished_data[finished_data["PRODUCT"] == "vitamin d"]
# gender_counts = vtmd_df["SEX"].value_counts()
# category_counts = vtmd_df["CASE_MEDDRA_PREFERRED_TERMS"].value_counts()


# #Data set only containing Vitamin D
# description_counts = finished_data["DESCRIPTION"].value_counts()
# #print(description_counts)
# vtmd_df = finished_data[finished_data["PRODUCT"] == "vitamin d"]


# vtmd_df = vtmd_df[vtmd_df["SEX"]!="Not Reported"]


# # Create the bar plot
# plt.figure(figsize=(10, 6)) 


# # for product in vtmd_df["PRODUCT"]:
# #     if product == "CENTRUM SILVER MEN'S 50+(MULTIMINERALS, MULTIVITAMINS) TABLET":
# #         product = "MEN'S 50+(MULTIMINERALS, MULTIVITAMINS) TABLET"
# vtmd_df['PRODUCT'] = vtmd_df['PRODUCT'].replace(['centrum silver women\'s 50+ (multiminerals, multivitamins) tablet'], 'centrum women multivit/min')


# multivitamin_women = vtmd_df[vtmd_df['PRODUCT'] == "centrum women multivit/min"] #shape = (618,13)
# multivitamin = vtmd_df[vtmd_df["PRODUCT"] == "multivitamin"]
# vitamin_c = vtmd_df[vtmd_df["PRODUCT"] == "vitamin c"]
# vitamin_d3 = vtmd_df[vtmd_df["PRODUCT"] == "vitamin d3"]

# multivitamin_women_men = multivitamin_women[multivitamin_women["SEX"] == "male"] #shape = (,13)
# womens_multivit_counts = multivitamin_women["SEX"].value_counts()

# multivitamin_men = multivitamin[multivitamin["SEX"] == "male"] #shape = (, 13)
# vitamin_c_men = vitamin_c[vitamin_c["SEX"] == "male"] #shape = (, 13)
# vitamin_c_women = vitamin_c[vitamin_c["SEX"] == "female"] #shape = (720, 13)
# vitamin_d3_men = vitamin_d3[vitamin_d3["SEX"] == "male"] #shape = (, 13)

# sns.barplot(data=vtmd_df, x="PRODUCT", y="PATIENT_AGE", hue="SEX", errorbar=None)

# plt.figure(figsize=(16, 8))

# occurrence_data_3 = vtmd_df["PRODUCT"].value_counts()

# sns.barplot(data=vtmd_df, x="PRODUCT", y="PATIENT_AGE", hue="SEX", errorbar=None, width=0.4, dodge=0.1)
# plt.xlabel("Products")
# plt.ylabel("Average Age")
# plt.title("Average Age by Products and Sex")

# # Show the plot
# # plt.legend(title="Sex", loc="upper right")
# # plt.show()
# plt.legend(title="Sex", loc="upper right")
# #plt.show()
