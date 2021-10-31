w = float (input("Your Weight(kg): "))
h = float (input("Your Height(m): "))
BMI = (w/(h**2))
if BMI < 18.5 :
    print("Underweight") 
if BMI >= 18.5 and BMI < 25 :
    print("Normal")
if BMI >= 25 and BMI < 30  :
    print("Overweight")
if BMI >= 30 and BMI < 35:
    print("Obese")
if BMI >= 35 :
    print("Extremely obese")