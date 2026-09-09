import pandas as pd

# ==========================================
# 1. LOAD RAW DATA
# ==========================================

df = pd.read_csv("raw_data/train.csv")

print("Original dataset shape:", df.shape)


# ==========================================
# 2. REMOVE DUPLICATES
# ==========================================

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

print("Duplicates removed:", duplicates_before)


# ==========================================
# 3. HANDLE MISSING AGE VALUES
# ==========================================

age_missing_before = df["Age"].isnull().sum()

df["Age"] = df["Age"].fillna(df["Age"].median())

print("Missing Age values filled:", age_missing_before)


# ==========================================
# 4. HANDLE MISSING EMBARKED VALUES
# ==========================================

embarked_missing_before = df["Embarked"].isnull().sum()

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("Missing Embarked values filled:", embarked_missing_before)


# ==========================================
# 5. HANDLE CABIN
# ==========================================

cabin_missing_before = df["Cabin"].isnull().sum()

df["Cabin"] = df["Cabin"].fillna("Unknown")

print("Missing Cabin values replaced:", cabin_missing_before)


# ==========================================
# 6. STANDARDIZE TEXT
# ==========================================

df["Sex"] = df["Sex"].str.strip().str.lower()

df["Embarked"] = df["Embarked"].str.strip().str.upper()


# ==========================================
# 7. CHECK DATA TYPES
# ==========================================

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")


# ==========================================
# 8. FINAL DATA QUALITY CHECK
# ==========================================

print("\n===== AFTER CLEANING =====")

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)


# ==========================================
# 9. SAVE CLEANED DATASET
# ==========================================

df.to_csv(
    "cleaned_data/cleaned_titanic.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
# ==========================================
# 10. CREATE CHANGE LOG
# ==========================================

change_log = pd.DataFrame({
    "Issue": [
        "Missing values",
        "Missing values",
        "Missing values",
        "Duplicate records",
        "Inconsistent text formatting",
        "Data type validation"
    ],

    "Column": [
        "Age",
        "Embarked",
        "Cabin",
        "All columns",
        "Sex and Embarked",
        "Age and Fare"
    ],

    "Action Taken": [
        "Filled missing values with median",
        "Filled missing values with mode",
        "Replaced missing values with 'Unknown'",
        "Removed duplicate rows",
        "Standardized whitespace and text casing",
        "Converted columns to numeric data types"
    ],

    "Reason": [
        "Median is less affected by extreme values",
        "Mode is appropriate for categorical data",
        "Preserves records without deleting rows",
        "Prevents duplicate observations",
        "Creates consistent categorical values",
        "Ensures reliable numerical analysis"
    ]
})

change_log.to_excel(
    "reports/change_log.xlsx",
    index=False
)

print("Change log saved successfully!")