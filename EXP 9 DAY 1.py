import matplotlib.pyplot as plt
month = ["Jan","Feb","Mar","Apr","May","Jun"]
sales = [50,75,45,80,100,68]
plt.plot(month,sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Line Plot")
plt.show()
plt.bar(month,sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Bar Plot")
plt.show()
