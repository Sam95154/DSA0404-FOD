import matplotlib.pyplot as plt
month = ["Jan","Feb","Mar","Apr","May","Jun"]
temp = [21,27,25,30,27,28]
rain = [15,9,12,5,9,10]
plt.plot(month,temp)
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.title("Line Plot")
plt.show()
plt.scatter(month,rain)
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.title("Scatter Plot")
plt.show()
