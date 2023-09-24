bangla_marks = float(input("Enter Your Bangla Subject Mark: "))
english_marks = float(input("Enter Your English Subject Mark: "))
math_marks = float(input("Enter Your Math Subject Mark: "))
science_marks = float(input("Enter Your Science Subject Mark: "))

total_marks = bangla_marks + english_marks + math_marks + science_marks
num_subjects = 4

average_marks = total_marks / num_subjects

def calculate_grade_points(mark):
    if mark >= 91 and mark <= 100:
        return "Your average Grade is: A+"
    elif mark >= 81 and mark <= 90:
        return "Your average Grade is: A"
    elif mark >= 71 and mark <= 80:
        return "Your average Grade is: B"
    elif mark >= 61 and mark <= 70:
        return "Your average Grade is: C"
    elif mark >= 41 and mark <= 60:
        return "Your average Grade is: D"
    elif mark >= 0 and mark <= 40:
        return "Your average Grade is: F"
    else:
        return "The average marks you enterd is incorrect"

print(calculate_grade_points(average_marks))
