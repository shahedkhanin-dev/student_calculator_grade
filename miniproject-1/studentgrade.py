import csv
# ----------------------------------
# Function : Validate marks input
# ----------------------------------
def get_valid_marks(sub_name):
    while True:
        try:
            marks = float(input(f"Enter marks for {sub_name}(0-100):"))
            if 0 <=marks <=100:
                return marks
            else:
                print("Invalid marks! Enter a value Between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
# ----------------------------------
# Function: Calculate grade
# ----------------------------------
def calculate_grade(percentage):
    if percentage >=90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >=50:
        return "D"
    else:
        return "F"
    

# ------------------------------------
# Function: Process a single student
# ------------------------------------
def process_student():
    print("\n--- Enter Student Details ---")
    name = input("Student Name:")


    marks =[]
    for i in range(1,6):
        marks.append(get_valid_marks(f"Subject {i}"))

    total = sum(marks)
    percentage = (total /500) * 100
    grade = calculate_grade(percentage)

    print("\n ===== RESULT =====")
    print(f"Name: {name}")
    print(f"Total Marks: {total}/500")
    print(f"Percentage:{percentage: .25f}%")
    print(f"Grade: {grade}")

    return [name, *marks, total, f"{percentage: .2f}%",grade]


# ------------------------------------
# Main Program
# ------------------------------------
def main():
    print(" ====== ADVANCED STUDENT GRADE CALCULATOR =======")

    # Create CSV file with headers
    with open("student_result.csv","w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name","Sub1","Sub2","Sub3","Sub4","Sub5","Total","Percentage","Grade"])

        while True:
            student_data = process_student()
            writer.writerow(student_data)

            choice = input("\n Do you want to enter another student? (yes/no): ").lower()   
            if choice not in ("yes", "y"):
                break 
    

    print("\n ALl results saved to 'student_results.csv'")
    print("program Ended.")


# ----------------------------------
# RUN PROGRAM
# ----------------------------------
main()