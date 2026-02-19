name = input("Enter student's name: ")
score = input("Enter last exam score: ")

score = float(score)

adjusted_score = score + 50
final_score = adjusted_score  / 4

print("Student name:", name, "Result:", final_score)