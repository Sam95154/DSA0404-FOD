import numpy as np
time = np.array([0, 1, 2, 3, 4])  
vertical = np.array([0, 10, 20, 15, 5])  
change_in_height = vertical[-1] - vertical[0]
change_in_time = time[-1] - time[0]
average_velocity = change_in_height / change_in_time
print("Average Velocity:", average_velocity)
