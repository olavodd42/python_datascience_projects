# Add your code here
 
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_age(age)
  analyze_num_of_children(num_of_children)
  return estimated_cost
 
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

def analyze_age(age_status):
  if age_status >= 60:
    print("Your age is an issue.")
  elif age_status >= 40:
    print("Your age maybe is an issue.")
  elif age_status >= 20:
    print("Your age probably isn't an issue.")
  else:
    print("Your age isn't an issue.")

def analyze_num_of_children(status_num_of_children):
  if status_num_of_children > 2:
    print("You have a problem with too many children")
  else:
    print("You doesn't have a problem with too many children")

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

olavo_insurance_cost = estimate_insurance_cost(name = 'Olavo', age = 22, sex = 1, num_of_children = 0, smoker = 0)