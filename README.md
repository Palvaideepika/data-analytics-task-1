# Data Analytics Task 1 – Data Cleaning and Preprocessing

## Project Overview

This project focuses on cleaning and preprocessing the Titanic dataset.

The objective is to identify and fix common data quality issues such as missing values, duplicate records, inconsistent text formatting, and incorrect data types so that the dataset is ready for reliable analysis.

## Tools Used

- Python
- Pandas
- Excel
- GitHub
- GitHub Actions

## Dataset

Dataset used: Titanic Dataset

The raw Titanic dataset was used for data cleaning and preprocessing.

The original raw dataset is not included in the public repository. It can be downloaded separately and placed inside the `raw_data` folder as:

`train.csv`

## Data Quality Issues Found

The following issues were identified:

- Missing values in the `Age` column
- Missing values in the `Embarked` column
- Missing values in the `Cabin` column
- Duplicate records were checked
- Inconsistent text formatting
- Numeric data types were validated

## Data Cleaning Approach

### Age

Missing Age values were replaced using the median Age.

### Embarked

Missing Embarked values were replaced using the mode.

### Cabin

Missing Cabin values were replaced with `Unknown`.

### Duplicate Records

Duplicate rows were checked and removed where present.

### Text Standardization

The `Sex` column was standardized to lowercase.

The `Embarked` column was standardized to uppercase.

### Data Type Validation

The `Age` and `Fare` columns were converted to numeric data types.

## Validation Results

After cleaning:

- Rows: 891
- Columns: 12
- Missing values: 0
- Duplicate rows: 0
- Age data type: numeric
- Fare data type: numeric

The cleaned dataset was exported as:

`cleaned_data/cleaned_titanic.csv`

## Project Structure

```text
Data_Analytics_Task_1/
│
├── cleaned_data/
│   └── cleaned_titanic.csv
│
├── reports/
│   ├── change_log.xlsx
│   └── data_quality_report.txt
│
├── deployment/
│   └── deployment.yml
│
├── rollback/
│   └── rollback_evidence.txt
│
├── main.py
├── requirements.txt
└── README.md
