import csv

# Create an empty dictionary to store students
students = {}

# Read student data from the CSV file
with open("student_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        major = row["Major"]
        gpa = float(row["GPA"])

        # Check whether the GPA is valid
        if 0.0 <= gpa <= 4.0:
            students[name] = {
                "major": major,
                "gpa": gpa
            }
        else:
            print("Invalid GPA for", name)

# Calculate the average GPA
total_gpa = 0

for name in students:
    total_gpa = total_gpa + students[name]["gpa"]

if len(students) > 0:
    average_gpa = total_gpa / len(students)

    print("Number of students:", len(students))
    print("Average GPA:", round(average_gpa, 2))

    # Print all students above average
    print("\nStudents above average GPA:")

    for name in students:
        if students[name]["gpa"] > average_gpa:
            print(
                name,
                "- Major:", students[name]["major"],
                "- GPA:", students[name]["gpa"]
            )

    # Predict scholarship eligibility
    print("\nScholarship predictions:")

    for name in students:
        major = students[name]["major"]
        gpa = students[name]["gpa"]

        if major == "Biology" and gpa >= 2.75:
            scholarship = "Yes"
        elif major == "Math" and gpa >= 3.50:
            scholarship = "Yes"
        else:
            scholarship = "No"

        print(
            name,
            "- Major:", major,
            "- GPA:", gpa,
            "- Scholarship:", scholarship
        )
else:
    print("No valid student records were found.")
