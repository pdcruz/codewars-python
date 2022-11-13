# Write function bmi that calculates body mass index (bmi = weight / height2).
# 
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"


# OUTSTANDING solution showing a slick algorithm
# Uses the sum of boolean expressions converted to (0, 1) as an array index
def calculate_bmi_solution(weight, height):
    bmi = weight / (height ** 2)
    return ["Underweight", "Normal", "Overweight", "Obese"][(bmi > 18.5) + (bmi > 25) + (bmi > 30)]