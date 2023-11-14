import numpy as np
house_data = np.genfromtxt('data.csv', delimiter=',')
house_morethan4 = house_data[house_data[:,0]>4]
avg = np.mean(house_morethan4,axis=0)
print("Average Price :",avg[2])
