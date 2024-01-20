import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FDAdata = pd.read_csv('./CAERS_ProductBased.csv')
print(FDAdata.shape)
FDAdata_SEX_rem = FDAdata.dropna(subset = ["SEX"])
print(FDAdata_SEX_rem)
women_data = FDAdata_SEX_rem[FDAdata_SEX_rem["SEX"] == "Female"]
print(women_data)