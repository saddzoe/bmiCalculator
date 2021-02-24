# bmiCalculator
# This is a bmi calculator
height = float(input("How tall are you in feet and inches: "))
weight = float(input("How much do you weight in pounds: :))
height = height/100
bmi = weight/(height * weight)
print("Your Body Mass Index is: ",bmi)
if(bmi > 0):
	if(bmi <= 16):
		print("You are really underweight")
	elif(bmi <= 18.5):
		print("You are underweight")
	elif(bmi <= 25):
		print("You are Healthy")
	elif(bmi <= 30):
		print("You are overweight")
	else: print("You are severely overweight")
else:("Enter valid details")
                     
