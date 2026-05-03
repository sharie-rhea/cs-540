"""
Name: Sharie Rhea
Date: 04.21.26
Class: CS540
"""

import pandas as pd
from ydata_profiling import ProfileReport

data_files = [
    "data/stars.csv",
    "data/Crime_Data_from_2020_to_Present.csv",
    "data/Provisional_COVID-19_Deaths_by_Sex_and_Age.csv",
    "data/business_data.csv",
    "data/titanic_raw.csv",
    "data/NCHS_-_Leading_Causes_of_Death__United_States.csv",
]
reference_file = data_files[-1]

raw_data = pd.read_csv(reference_file)
# print(raw_data)

print("data.shape")
print(raw_data.shape)
print()

print("data.head() and data.tail()")
print(raw_data.head(6))
print(raw_data.tail(6))
print()

print("data.info()")
print(raw_data.info())
print()

# print(raw_data.columns)
# print(raw_data.dtypes)

print("data.describe()")
print(raw_data.describe())
print()

# generate html report from ydata
stripped = reference_file.removeprefix("data/").removesuffix(".csv")
title = f"Report for {stripped.replace('_', ' ')}"
profile = ProfileReport(raw_data, title=title)
profile.to_file(f"{stripped}_report.html")
