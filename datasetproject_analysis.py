import pandas as ps
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

#load data set

file_path = "data/Datasetprojpowerbi.csv"

data = ps.read_csv(file_path)

missing_value = data.dropna()
#Display first few rows,descriptive statistics, and info
print(f"Data Head:{data.head}")
print(f"Data Describe:{data.describe}")
print(f"Data info:{data.info}")
print(f"missing_value: {missing_value}")

#Descriptive statistics count categorical for the dataset
genre_count = data["Genre"].value_counts()
reports_count = data["Reports"].value_counts()
age_count = data["Age"].value_counts()
gpa_count = data["Gpa"].value_counts()
year_count = data["Year"].value_counts()
count_count = data["Count"].value_counts()
gender_count = data["Gender"].value_counts()
nationality_count = data["Nationality"].value_counts()

#proportion count categorical for dataset
genre_proportion_count = data["Genre"].value_counts(normalize=True)
reports_proportion_count = data["Reports"].value_counts(normalize=True)
age_proportion_count = data["Age"].value_counts(normalize=True)
gpa_proportion_count = data["Gpa"].value_counts(normalize=True)
year_proportion_count = data["Year"].value_counts(normalize=True)
count_proportion_count = data["Count"].value_counts(normalize=True)
gender_proportion_count = data["Gender"].value_counts(normalize=True)
nationality_proportion_count = data["Nationality"].value_counts(normalize=True)

print(f"Genre count:{genre_count}")
print(f"Reports count:{reports_count}")
print(f"Age count:{age_count}")
print(f"Gpa count:{gpa_count}")
print(f"Year count:{year_count}")
print(f"Count count:{count_count} ")
print(f"Gender count:{gender_count}")
print(f"Nationality count:{nationality_count}")
print(f"Genre proportion count:{genre_proportion_count}")
print(f"Reports proportion count:{reports_proportion_count}")
print(f"Age proportion count:{age_proportion_count}")
print(f"Gpa proportion count:{gpa_proportion_count}")
print(f"Year proportion count:{year_proportion_count}")
print(f"Count proportion count:{count_proportion_count}")
print(f"Gender proportion count:{gender_proportion_count}")
print(f"Nationality proportion count:{nationality_proportion_count}")


#constngency statistical table between the Data set
contingency_table = ps.crosstab(data['Genre'], data['Reports'])

chi2_table, pi_square, dof, expected = chi2_contingency(contingency_table)

print(f"contingency-stat-table:{chi2_table}")
print(f"P-Value:{pi_square}")
print(f"Degree of freedom:{dof}")

#Bar chart for the dataset "Genre"
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x="Genre")
plt.title("Distribution of complaint Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.show()

#Bar chart for the dataset "Reports"
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x="Reports")
plt.title("Reports of students experience in each region")
plt.xlabel("Reports")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


