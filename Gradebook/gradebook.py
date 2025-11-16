# ---------------------------------------------------------
# GradeBook Analyzer
# Name: Eshtha
# Date: 14-11-2025
# Roll Number: 2501730450
# ---------------------------------------------------------

import csv

# ---------------- TASK 3: STATISTICAL FUNCTIONS ---------------- #

def calculate_average(marks_dict):
    total = sum(marks_dict.values())
    count = len(marks_dict)
    return total / count

def calculate_median(marks_dict):
    values = sorted(marks_dict.values())
    n = len(values)
    mid = n // 2

    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())


# ---------------- TASK 4: ASSIGN GRADES ---------------- #

def assign_grades(marks_dict):
    grades = {}

    for name, score in marks_dict.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"

    return grades


# ---------------- TASK 5: PASS / FAIL LIST ---------------- #

def pass_fail_lists(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed


# ---------------- TASK 2: INPUT METHODS ---------------- #

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter student name: ")
        score = int(input("Enter marks: "))
        marks[name] = score

    return marks


def csv_input():
    marks = {}
    file_name = input("Enter CSV file name: ")

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            score = int(row[1])
            marks[name] = score

    return marks


# ---------------- TASK 6: PRINT TABLE ---------------- #

def print_result_table(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("---------------------------------------")

    for name in marks_dict:
        print(f"{name}\t\t{marks_dict[name]}\t{grades_dict[name]}")

    print()


# ----------------------------- MAIN CLI LOOP ----------------------------- #

print("------------------------------------------------")
print("      Welcome to the GradeBook Analyzer!")
print("------------------------------------------------")

while True:
    print("\nChoose Input Method:")
    print("1. Manual Entry")
    print("2. CSV File Input")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        marks = manual_input()

    elif choice == "2":
        marks = csv_input()

    elif choice == "3":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
        continue

    # Task 3: Analysis
    avg = calculate_average(marks)
    median = calculate_median(marks)
    max_score = find_max_score(marks)
    min_score = find_min_score(marks)

    print("\n--- STATISTICAL ANALYSIS ---")
    print("Average Marks:", avg)
    print("Median Marks:", median)
    print("Highest Marks:", max_score)
    print("Lowest Marks:", min_score)

    # Task 4: Grades
    grades = assign_grades(marks)

    # Grade distribution
    print("\n--- GRADE DISTRIBUTION ---")
    for grade in ["A", "B", "C", "D", "F"]:
        count = list(grades.values()).count(grade)
        print(f"{grade}: {count} students")

    # Task 5: Pass/Fail
    passed, failed = pass_fail_lists(marks)
    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

    # Task 6: Table
    print_result_table(marks, grades)

    print("Analysis complete. Do you want to run again? (yes/no)")
    again = input().lower()

    if again != "yes":
        print("Thank you for using GradeBook Analyzer!")
        break
