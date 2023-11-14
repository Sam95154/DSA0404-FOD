import pandas as pd
import matplotlib.pyplot as plt

# Generate sample data
data = {
    'Name': ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7', 'Player8', 'Player9', 'Player10'],
    'Age': [25, 28, 23, 30, 22, 26, 29, 31, 27, 24],
    'Position': ['Forward', 'Midfielder', 'Forward', 'Defender', 'Goalkeeper', 'Midfielder', 'Forward', 'Defender', 'Midfielder', 'Forward'],
    'GoalsScored': [20, 15, 18, 5, 0, 12, 22, 3, 17, 19],
    'WeeklySalary': [10000, 12000, 8000, 15000, 5000, 11000, 18000, 9000, 13000, 16000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('soccer_players.csv', index=False)

# Read the data from the CSV file into a pandas DataFrame
df = pd.read_csv('soccer_players.csv')

# Find the top 5 players with the highest number of goals scored
top_goals_players = df.nlargest(5, 'GoalsScored')

# Find the top 5 players with the highest salaries
top_salary_players = df.nlargest(5, 'WeeklySalary')

# Calculate the average age of players
average_age = df['Age'].mean()

# Display the names of players above the average age
above_average_age_players = df[df['Age'] > average_age]['Name']

# Visualize the distribution of players based on their positions using a bar chart
position_counts = df['Position'].value_counts()
position_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Players by Position')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.show()

# Display the results
print("Top 5 Players with the Highest Number of Goals Scored:")
print(top_goals_players[['Name', 'GoalsScored']])
print("\nTop 5 Players with the Highest Salaries:")
print(top_salary_players[['Name', 'WeeklySalary']])
print(f"\nAverage Age of Players: {average_age:.2f}")
print("\nPlayers Above Average Age:")
print(above_average_age_players)
