# ============================================================
# Question 3: Hospital Patient Data Validation
# ============================================================
# This program reads a CSV file containing patient records,
# detects and removes duplicates, replaces missing values,
# corrects invalid ages, and saves the validated dataset
# to a new CSV file.
# ============================================================

# Step 1: Import required libraries
import pandas as pd

# Step 2: Create sample patient CSV file
patient_data = """Patient_ID,Patient_Name,Age,Blood_Group,Contact_Number
P001,Rajesh Kumar,45,B+,9876543001
P002,Sunita Devi,32,A-,9876543002
P003,Mohammed Ali,-5,O+,9876543003
P001,Rajesh Kumar,45,B+,9876543001
P004,Lakshmi Rao,,AB+,9876543004
P005,John Peter,28,B-,
P006,Ananya Mishra,150,A+,9876543006
P007,Suresh Babu,55,,9876543007
P008,Fatima Khan,38,O-,9876543008
P003,Mohammed Ali,-5,O+,9876543003
P009,Ganesh Iyer,67,A+,
P010,Rita Fernandez,0,B+,9876543010
P011,Harpreet Singh,42,AB-,9876543011
P012,Deepa Nair,,O+,9876543012
P013,Venkat Reddy,200,B+,9876543013
"""

with open("patient_records.csv", "w") as file:
    file.write(patient_data)

print("=" * 60)
print("  Hospital Patient Data Validation Program")
print("=" * 60)

# Step 3: Read the CSV file
print("\n--- Step 1: Reading the CSV file ---")
df = pd.read_csv("patient_records.csv")
print(f"Total records loaded: {len(df)}")
print("\nOriginal Dataset:")
print(df.to_string(index=False))

# Step 4: Detect duplicate Patient IDs
print("\n--- Step 2: Detecting duplicate Patient IDs ---")
duplicate_ids = df[df.duplicated(subset="Patient_ID", keep=False)]
unique_dup_ids = duplicate_ids["Patient_ID"].unique()
print(f"Duplicate Patient IDs found: {list(unique_dup_ids)}")
print(f"Total duplicate records: {df.duplicated(subset='Patient_ID').sum()}")

# Step 5: Remove duplicate records
df = df.drop_duplicates(subset="Patient_ID", keep="first")
print(f"Records after removing duplicates: {len(df)}")

# Step 6: Replace missing values
print("\n--- Step 3: Handling missing values ---")
missing_age = df["Age"].isna().sum()
missing_blood = df["Blood_Group"].isna().sum()
missing_contact = df["Contact_Number"].isna().sum()

print(f"Missing ages          : {missing_age}")
print(f"Missing blood groups  : {missing_blood}")
print(f"Missing contact numbers: {missing_contact}")

# Fill missing ages with median age of valid records
valid_ages = df["Age"].dropna()
valid_ages = valid_ages[(valid_ages > 0) & (valid_ages <= 120)]
median_age = int(valid_ages.median())
df["Age"] = df["Age"].fillna(median_age)
print(f"\nMissing ages filled with median value: {median_age}")

# Fill missing blood groups with "Unknown"
df["Blood_Group"] = df["Blood_Group"].fillna("Unknown")
print("Missing blood groups filled with 'Unknown'.")

# Fill missing contact numbers with "Not Available"
df["Contact_Number"] = df["Contact_Number"].fillna("Not Available")
print("Missing contact numbers filled with 'Not Available'.")

# Step 7: Correct invalid ages
print("\n--- Step 4: Correcting invalid ages ---")
invalid_ages = df[(df["Age"] <= 0) | (df["Age"] > 120)]
print(f"Records with invalid ages: {len(invalid_ages)}")
if len(invalid_ages) > 0:
    print(invalid_ages[["Patient_ID", "Patient_Name", "Age"]].to_string(index=False))

# Replace invalid ages with median age
df.loc[(df["Age"] <= 0) | (df["Age"] > 120), "Age"] = median_age
print(f"Invalid ages replaced with median value: {median_age}")

# Convert age to integer
df["Age"] = df["Age"].astype(int)

# Step 8: Display the validated dataset
print("\n--- Step 5: Validated Dataset ---")
print(df.to_string(index=False))

# Step 9: Save the validated dataset
output_file = "validated_patients.csv"
df.to_csv(output_file, index=False)
print(f"\nValidated dataset saved to '{output_file}'")

# Step 10: Display summary
print("\n--- Summary ---")
print(f"Original record count   : {len(pd.read_csv('patient_records.csv'))}")
print(f"Duplicates removed      : {len(pd.read_csv('patient_records.csv')) - len(df) + (len(invalid_ages))}")
print(f"Missing values filled   : {missing_age + missing_blood + missing_contact}")
print(f"Invalid ages corrected  : {len(invalid_ages)}")
print(f"Final record count      : {len(df)}")
print("\nProgram executed successfully!")
