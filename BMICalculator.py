#BMICalculator

print("Welcome to BMI Calculator")
print()
name = input("Enter your name: ")
weight = float(input("Enter your weight in (kgs): "))
height = float(input("Enter your height in (meters): "))
#Calculate BMI
bmi = weight/(height*height)
print()
print(name, "your bmi is", bmi)
