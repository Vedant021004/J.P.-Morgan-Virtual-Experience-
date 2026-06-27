import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("Delinquency_prediction_dataset.xlsx")

print(df.head())
print(df.tail())
print(df.sample(5))

print(df.shape)
print(df.columns)
print(df.info())
print(df.dtypes)

print(df.describe())
print(df.describe(include="all"))

print(df.isnull().sum())
print((df.isnull().sum()/len(df))*100)

print(df.duplicated().sum())
print(df.nunique())

numeric_cols = df.select_dtypes(include=np.number)
categorical_cols = df.select_dtypes(include="object")

print(numeric_cols.columns)
print(categorical_cols.columns)

for col in numeric_cols.columns:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols.columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print(df.isnull().sum())

print(df.corr(numeric_only=True))

target = "Delinquent_Account"

print(df[target].value_counts())
print(df[target].value_counts(normalize=True) * 100)

print(df.corr(numeric_only=True)[target].sort_values(ascending=False))

Q1 = df["Income"].quantile(0.25)
Q3 = df["Income"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Income"] < lower) | (df["Income"] > upper)]

print(outliers)
print(len(outliers))

print(df.groupby(target)["Income"].mean())
print(df.groupby(target)["Credit_Score"].mean())
print(df.groupby(target)["Missed_Payments"].mean())

plt.figure(figsize=(8,5))
plt.hist(df["Income"], bins=20)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Credit_Score"], bins=20)
plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,5))
plt.boxplot(df["Income"])
plt.title("Income Boxplot")
plt.show()

plt.figure(figsize=(8,5))
plt.boxplot(df["Credit_Score"])
plt.title("Credit Score Boxplot")
plt.show()

plt.figure(figsize=(8,5))
df[target].value_counts().plot(kind="bar")
plt.title("Delinquent Account Distribution")
plt.xlabel("Delinquent Account")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["Income"], df["Credit_Score"])
plt.title("Income vs Credit Score")
plt.xlabel("Income")
plt.ylabel("Credit Score")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["Credit_Utilization"], df["Missed_Payments"])
plt.title("Credit Utilization vs Missed Payments")
plt.xlabel("Credit Utilization")
plt.ylabel("Missed Payments")
plt.show()

corr = df.corr(numeric_only=True)

plt.figure(figsize=(12,8))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

df.to_excel("clean_dataset.xlsx", index=False)
