import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FDAdata = pd.read_csv('./CAERS_ProductBased.csv')
print(FDAdata.shape)
FDAdata_SEX_rem = FDAdata.dropna(subset = ["SEX"])
print(FDAdata_SEX_rem)
Wo_Products = FDAdata_SEX_rem[FDAdata_SEX_rem["SEX"] == "Female"]
print(Wo_Products)