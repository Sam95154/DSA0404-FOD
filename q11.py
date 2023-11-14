import numpy as np

fuel_efficiency = np.array([20, 25, 30, 35, 40])

average_fuel_efficiency = np.mean(fuel_efficiency)

old_model_index = 1
new_model_index = 3

old_model_fuel_efficiency = fuel_efficiency[old_model_index]
new_model_fuel_efficiency = fuel_efficiency[new_model_index]

percentage_improvement = ((new_model_fuel_efficiency - old_model_fuel_efficiency) / old_model_fuel_efficiency) * 100

print("The average fuel efficiency is:", average_fuel_efficiency)
print("The percentage improvement in fuel efficiency between the old model and new model is:", percentage_improvement)

