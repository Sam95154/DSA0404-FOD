import pandas as pd
isport numpy as np
import matplotlib.pyplot as plt
np.random.seed (42)
days pd.date_range (start='2022-01-01', end='2022-12-31', freq-'D')
temperature = np.random.normal(loc=25, scale-5, size=len (days))
rainfall = np.random.normal (loc=10, scale=5, size=len (days))
weather data pd.DataFrame (('Date': days, 'Temperature': temperature, 'Rainfall': rainfall))
correlation coefficient weather_data['Temperature'].corr (weather_data['Rainfall"])

plt.figure (figsize=(10, 6))
plt.scatter (weather_data['Temperature'], weather_data['Rainfall']; alpha=0.5)
plt.title('Temperature vs. Rainfall')
plt.xlabel('Temperature (°C)")
plt.ylabel("Rainfall (mm) ')
plt.grid(True)
plt.show()
print (f"Correlation Coefficient: (correlation coefficient)")
