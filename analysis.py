import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("hospital_cleaned.csv")

# -----------------------------
# Basic Information
# -----------------------------
print(df.head())

print(df.info())

print(df.isnull().sum())

print("Total Patients:", len(df))

# -----------------------------
# Gender Analysis
# -----------------------------
print("\nGender Distribution:")
print(df['Gender'].value_counts())

# -----------------------------
# Medical Condition Analysis
# -----------------------------
print("\nMedical Condition Count:")
print(df['Medical Condition'].value_counts())

# -----------------------------
# Billing Amount Analysis
# -----------------------------
df['Billing Amount'] = (
    df['Billing Amount']
    .astype(str)
    .str.replace(',', '')
    .astype(float)
)

print("\nAverage Billing Amount:")
print(df['Billing Amount'].mean())

# =====================================================
# VISUALIZATIONS
# =====================================================

# -----------------------------
# 1. Gender Distribution Chart
# -----------------------------
sns.countplot(x='Gender', data=df)

plt.title("Gender Distribution")

plt.xlabel("Gender")

plt.ylabel("Count")

plt.show()

# -----------------------------
# 2. Medical Condition Chart
# -----------------------------
df['Medical Condition'].value_counts().plot(kind='bar')

plt.title("Medical Condition Analysis")

plt.xlabel("Medical Condition")

plt.ylabel("Count")

plt.show()

# -----------------------------
# 3. Age Distribution Histogram
# -----------------------------
plt.hist(df['Age'], bins=15)

plt.title("Age Distribution")

plt.xlabel("Age")

plt.ylabel("Count")

plt.show()

# -----------------------------
# 4. Admission Type Analysis
# -----------------------------
sns.countplot(x='Admission Type', data=df)

plt.title("Admission Type Analysis")

plt.xlabel("Admission Type")

plt.ylabel("Count")

plt.show()

# -----------------------------
# 5. Billing Amount Distribution
# -----------------------------
plt.hist(df['Billing Amount'], bins=20)

plt.title("Billing Amount Distribution")

plt.xlabel("Billing Amount")

plt.ylabel("Count")

plt.show()