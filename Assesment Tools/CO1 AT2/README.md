# Data Wrangling - Practical Assignment

## Subject
Query Processing and Performance Tuning

## Questions

| # | Title | Input | Output |
|---|-------|-------|--------|
| 1 | Student Admission Data Cleaning | `student_admissions.csv` | `cleaned_students.csv` |
| 2 | Employee Data Integration | `employees.csv` + `departments.json` | `employee_report.csv` |
| 3 | Hospital Patient Data Validation | `patient_records.csv` | `validated_patients.csv` |

## Files

```
├── README.md
├── Data_Wrangling_Practical_Report.docx   # Combined report (all 3 questions)
├── Q1_Student_Data_Cleaning.py
├── Q2_Employee_Data_Integration.py
└── Q3_Hospital_Data_Validation.py
```

## How to Run

1. Open [Google Colab](https://colab.research.google.com/)
2. Copy the contents of any `.py` file into a new notebook cell
3. Run the cell — all input files are generated automatically, no manual uploads needed

## Libraries Used

- `pandas` — data manipulation
- `json` — JSON file handling
- `xml.etree.ElementTree` — (available if needed)

## Notes

- All programs are self-contained and generate their own sample input data
- Each program prints step-by-step progress and a summary to the console
- Output CSV files are saved in the working directory
