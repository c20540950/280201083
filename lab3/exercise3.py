gpa = float(input("What is your GPA? "))
num_of_lect = int(input("How many Lectures have you attended? "))

if gpa >= 2 and num_of_lect >= 47:
  print("GRATUATED!")
elif gpa >= 2 and num_of_lect < 47:
  print("Not enought number of lectures!")
elif gpa < 2 and num_of_lect >= 47:
  print("Not enough GPA!")
else:
  print("Not enought number of lectures or GPA!")
