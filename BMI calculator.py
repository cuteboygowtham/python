def bmi(newweight, newheight):
    new_bmi = newweight / (pow(newheight/100, 2))
    return new_bmi


a = float(input("enter ur weight in kg's : \n"))
b = float(input("enter ur height in centimeters : \n"))
results = bmi(a, b)
print("BMI =", results)
