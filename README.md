📘 Student Grade Calculator — Python Mini Project

A simple yet advanced Python-based Student Grade Calculator that allows entering marks for multiple students, validates inputs, calculates grade & percentage, and exports results to a CSV file.
This project is ideal for beginners who want to understand Python fundamentals like functions, loops, conditionals, file handling, and input validation.

🧠 Features
✔ 1. Input Validation

Accepts marks only between 0 and 100

Rejects invalid or non-numeric inputs with helpful messages

✔ 2. Multiple Students Support

Add as many students as you want

Program continues until you choose to stop

✔ 3. Function-Based Code Structure

Clean, modular, beginner-friendly functions

Easy to update or expand

✔ 4. Automatic Grade Calculation

Grades are given based on percentage:

Percentage	Grade
90–100	A+
80–89	A
70–79	B
60–69	C
50–59	D
Below 50	F
✔ 5. CSV Export

Creates student_results.csv containing:

Student Name

5 Subject Marks

Total Marks

Percentage

Grade

📂 Project Structure
Student-Grade-Calculator/
│
├── grade_calculator.py       # Main project script
├── student_results.csv       # Auto-generated output file
└── README.md                 # Documentation

🖥️ How to Run the Project

Make sure Python 3 is installed

Run the script:

python grade_calculator.py


Enter:

Student name

Marks of 5 subjects

Results will be displayed and automatically saved into
student_results.csv

📌 Example CSV Output
Name	Sub1	Sub2	Sub3	Sub4	Sub5	Total	Percentage	Grade
Rahul	87	90	76	85	92	430	86.00%	A
🚀 Future Improvements (Optional)

Add GUI using Tkinter

Add charts/graphs (matplotlib)

Convert to OOP-based version

Add database storage (SQLite/MySQL)

Build a web-based version using Flask/Django

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss the changes.

📜 License

This project is open-source and free to use.
