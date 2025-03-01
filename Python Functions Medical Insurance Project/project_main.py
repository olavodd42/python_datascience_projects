# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = f"The estimated insurance cost for {name} is {round(estimated_cost, 2)} dollars."
  return estimated_cost, output_message

def diff_insurance_cost(cost1, cost2):
  diff = abs(cost1 - cost2)
  print(f"The difference in insurance cost is {round(diff, 2)} dollars.")

# Estimate Maria's insurance cost
maria_insurance_cost, message = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria")
print(message)

# Estimate Omar's insurance cost 
omar_insurance_cost, message = calculate_insurance_cost(35, 1, 22.2, 0, 1, "Omar")
print(message)

# Estimate my insurance cost
olavo_insurance_cost, message = calculate_insurance_cost(28, 1, 24.0, 0, 0, "Olavo")
print(message)

diff_insurance_cost(maria_insurance_cost, olavo_insurance_cost)