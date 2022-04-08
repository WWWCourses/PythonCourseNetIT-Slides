def get_user_data():
	user_data = {}

	user_data["name"] = input("Enter your name, please:")
	user_data["height"] = int(input("I need to know your height in centimetres:"))
	user_data["height"] = cm_to_meters(user_data["height"])
	user_data["weight"] = int(input("And your weight in kilograms:"))

	return user_data

def cm_to_meters(cm):
	return cm/100

def calc_BMI(w,h):
	return (w / (h*h))

def calc_BMI_category(bmi):
	if bmi <= 18.5:
		return "Underweight"
	elif bmi>18.5 and bmi<=24.9:
		return "Normal"
	elif bmi>25 and bmi<=29.9:
		return "Overweight"
	else:
		return "Obesity"

def print_results(bmi_category):
		print("You are ", bmi_category)


user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)

