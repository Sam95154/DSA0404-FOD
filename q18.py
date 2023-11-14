import numpy as np

def calculate_mean_temperature(data):
    return np.mean(data, axis=0)

def calculate_standard_deviation(data):
    return np.std(data, axis=0)

def calculate_temperature_range(data):
    return np.max(data, axis=0) - np.min(data, axis=0)

def find_most_consistent_city(standard_deviations):
    return np.argmin(standard_deviations)

def find_city_with_highest_range(temperature_ranges):
    return np.argmax(temperature_ranges)

def main():
    # Sample data format: rows represent days, columns represent cities
    # Replace this with your actual dataset
    temperature_data = np.array([
        [25, 30, 35, 28],
        [24, 29, 34, 27],
        # ... additional rows for each day
    ])

    mean_temperatures = calculate_mean_temperature(temperature_data)
    std_deviations = calculate_standard_deviation(temperature_data)
    temperature_ranges = calculate_temperature_range(temperature_data)

    most_consistent_city = find_most_consistent_city(std_deviations)
    city_with_highest_range = find_city_with_highest_range(temperature_ranges)

    print("Mean Temperatures for Each City:", mean_temperatures)
    print("Standard Deviations for Each City:", std_deviations)
    print("Temperature Ranges for Each City:", temperature_ranges)
    print("City with the Most Consistent Temperature:", most_consistent_city)
    print("City with the Highest Temperature Range:", city_with_highest_range)

if __name__ == "__main__":
    main()
