gpa_input = input("Enter your GPA (0.0 - 4.0): ")
gpa = float(gpa_input)


if gpa < 0.0 or gpa > 4.0:
    print("Your input is not within the range. Please enter an input between 0.0 and 4.0")
else:
    print()
    print(f"Your GPA: {gpa}")

    if gpa >= 3.5:
        print("Grade: First Class Honours")

    elif gpa >= 3.0:
        print("Grade: Second Class Honours (Upper Division)")

    elif gpa >= 2.0:
        print("Grade: Second Class Honours (Lower Division)")

    elif gpa >= 1.0:
        print("Grade: Third Class Honours")

    else:
        print("Grade: Below Third Class")