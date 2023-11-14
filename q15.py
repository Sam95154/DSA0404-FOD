import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generate random data for the control group and treatment group
control_data = np.random.normal(loc=10, scale=2, size=100)
treatment_data = np.random.normal(loc=12, scale=2, size=100)

# Plot histograms for each group
plt.hist(control_data, alpha=0.5, label='Control Group')
plt.hist(treatment_data, alpha=0.5, label='Treatment Group')
plt.legend(loc='upper right')

# Perform t-test
t_statistic, p_value = stats.ttest_ind(control_data, treatment_data)
print('t-statistic:', t_statistic)
print('p-value:', p_value)

plt.show()
