# ============================================================
# Question 2: Employee Data Integration
# ============================================================
# This program reads employee details from a CSV file and
# department information from a JSON file, merges them using
# Department ID, identifies missing department info, and
# saves the consolidated dataset as a CSV file.
# ============================================================

# Step 1: Import required libraries
import pandas as pd
import json

# Step 2: Create sample employee CSV file
employee_data = """Employee_ID,Employee_Name,Department_ID,Designation,Salary
E001,Amit Shah,D101,Software Engineer,55000
E002,Neha Gupta,D102,Data Analyst,48000
E003,Ravi Patel,D103,Mechanical Engineer,50000
E004,Sonal Mehta,D101,Team Lead,72000
E005,Vikram Jain,D104,Civil Engineer,47000
E006,Pooja Reddy,D102,Senior Analyst,60000
E007,Arjun Das,D105,Intern,20000
E008,Kavita Nair,D106,HR Executive,45000
E009,Manoj Kumar,D103,Junior Engineer,38000
E010,Divya Sharma,D107,Marketing Head,68000
"""

with open("employees.csv", "w") as file:
    file.write(employee_data)

# Step 3: Create sample department JSON file
department_data = [
    {"Department_ID": "D101", "Department_Name": "Computer Science", "Location": "Building A"},
    {"Department_ID": "D102", "Department_Name": "Data Science", "Location": "Building B"},
    {"Department_ID": "D103", "Department_Name": "Mechanical", "Location": "Building C"},
    {"Department_ID": "D104", "Department_Name": "Civil", "Location": "Building D"},
    {"Department_ID": "D105", "Department_Name": "Research", "Location": "Building E"}
]

with open("departments.json", "w") as file:
    json.dump(department_data, file, indent=4)

print("=" * 60)
print("  Employee Data Integration Program")
print("=" * 60)

# Step 4: Read the employee CSV file
print("\n--- Step 1: Reading Employee CSV file ---")
emp_df = pd.read_csv("employees.csv")
print(f"Total employees loaded: {len(emp_df)}")
print("\nEmployee Data:")
print(emp_df.to_string(index=False))

# Step 5: Read the department JSON file
print("\n--- Step 2: Reading Department JSON file ---")
with open("departments.json", "r") as file:
    dept_list = json.load(file)

dept_df = pd.DataFrame(dept_list)
print(f"Total departments loaded: {len(dept_df)}")
print("\nDepartment Data:")
print(dept_df.to_string(index=False))

# Step 6: Merge both datasets using Department_ID (left join)
print("\n--- Step 3: Merging datasets on Department_ID ---")
merged_df = pd.merge(emp_df, dept_df, on="Department_ID", how="left")
print(f"Total records after merge: {len(merged_df)}")

# Step 7: Identify employees with missing department information
print("\n--- Step 4: Identifying missing department info ---")
missing_dept = merged_df[merged_df["Department_Name"].isna()]
if len(missing_dept) > 0:
    print(f"Employees with missing department info: {len(missing_dept)}")
    print(missing_dept[["Employee_ID", "Employee_Name", "Department_ID"]].to_string(index=False))
else:
    print("No employees with missing department information.")

# Step 8: Fill missing department details
merged_df["Department_Name"] = merged_df["Department_Name"].fillna("Unknown")
merged_df["Location"] = merged_df["Location"].fillna("Not Assigned")

# Step 9: Display the merged dataset
print("\n--- Step 5: Merged Dataset ---")
print(merged_df.to_string(index=False))

# Step 10: Save the consolidated dataset
output_file = "employee_report.csv"
merged_df.to_csv(output_file, index=False)
print(f"\nConsolidated dataset saved to '{output_file}'")

# Step 11: Display summary
print("\n--- Summary ---")
print(f"Total employees          : {len(emp_df)}")
print(f"Total departments        : {len(dept_df)}")
print(f"Matched records          : {len(merged_df) - len(missing_dept)}")
print(f"Unmatched records        : {len(missing_dept)}")
print(f"Final merged records     : {len(merged_df)}")
print("\nProgram executed successfully!")
