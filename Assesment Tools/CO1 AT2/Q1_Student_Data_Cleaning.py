# ============================================================
# Question 1: Student Admission Data Cleaning
# ============================================================
# This program reads a CSV file containing student admission
# records, cleans the data by removing duplicates, filling
# missing values, fixing formatting issues, and saves the
# cleaned dataset to a new CSV file.
# ============================================================

# Step 1: Import required libraries
import pandas as pd

# Step 2: Create sample student admission CSV file
sample_data = """Student_ID,Student_Name,Department,Phone_Number,Admission_Year
101,  Arun Kumar  ,computer science,9876543210,2024
102,Priya Sharma,  COMPUTER SCIENCE  ,9876543211,2024
103,Rahul Verma,Electronics,9876543212,2024
101,  Arun Kumar  ,computer science,9876543210,2024
104,Sneha Patil,mechanical,9876543213,2024
105,Deepak Joshi,ELECTRONICS,,2024
106,Anita Desai,Computer Science,9876543215,2024
107,Kiran Rao,  mechanical  ,,2024
108,Vijay Singh,civil engineering,9876543217,2024
103,Rahul Verma,Electronics,9876543212,2024
109,Meena Iyer,CIVIL ENGINEERING,9876543218,2024
110,Suresh Nair,electronics,,2024
"""

# Write the sample data to a CSV file
with open("student_admissions.csv", "w") as file:
    file.write(sample_data)

print("=" * 60)
print("  Student Admission Data Cleaning Program")
print("=" * 60)

# Step 3: Read the CSV file
print("\n--- Step 1: Reading the CSV file ---")
df = pd.read_csv("student_admissions.csv")
print(f"Total records loaded: {len(df)}")
print("\nOriginal Dataset:")
print(df.to_string(index=False))

# Step 4: Check for duplicate records
print("\n--- Step 2: Checking for duplicate records ---")
duplicate_count = df.duplicated().sum()
print(f"Duplicate records found: {duplicate_count}")

# Step 5: Remove duplicate records
df = df.drop_duplicates()
print(f"Records after removing duplicates: {len(df)}")

# Step 6: Remove extra spaces from student names
print("\n--- Step 3: Cleaning student names ---")
df["Student_Name"] = df["Student_Name"].str.strip()
print("Extra spaces removed from student names.")

# Step 7: Standardize department names (Title Case)
print("\n--- Step 4: Standardizing department names ---")
df["Department"] = df["Department"].str.strip().str.title()
print("Department names standardized to Title Case.")

# Step 8: Fill missing phone numbers with "Not Available"
print("\n--- Step 5: Handling missing phone numbers ---")
missing_phone = df["Phone_Number"].isna().sum()
print(f"Missing phone numbers found: {missing_phone}")
df["Phone_Number"] = df["Phone_Number"].fillna("Not Available")
print("Missing phone numbers filled with 'Not Available'.")

# Step 9: Display the cleaned dataset
print("\n--- Step 6: Cleaned Dataset ---")
print(df.to_string(index=False))

# Step 10: Save the cleaned dataset to a new CSV file
output_file = "cleaned_students.csv"
df.to_csv(output_file, index=False)
print(f"\nCleaned dataset saved to '{output_file}'")

# Step 11: Display summary
print("\n--- Summary ---")
print(f"Original record count : {len(pd.read_csv('student_admissions.csv'))}")
print(f"Duplicates removed    : {duplicate_count}")
print(f"Missing values filled : {missing_phone}")
print(f"Final record count    : {len(df)}")
print("\nProgram executed successfully!")
