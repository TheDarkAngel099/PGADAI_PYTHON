def get_grade(marks):
    if marks >= 75:
        return "DISTINCTION"
    elif marks >= 60:
        return "FIRST CLASS"
    elif marks >= 50:
        return "SECOND CLASS"
    elif marks >= 40:
        return "PASS CLASS"
    else:
        return "FAIL"


marks = int(input("Enter your marks (0–100): "))
if 0<= marks <= 100:
    print("Your grade is:", get_grade(marks))
else:
    print("Enter marks between 0 - 100")
