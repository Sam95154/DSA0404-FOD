import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load your transaction data (replace 'your_data.csv' with your actual file path or data source)
data = pd.read_csv('your_data.csv')

# Extract relevant features (e.g., total amount spent and number of items purchased)
features = data[['TotalAmountSpent', 'NumberOfItemsPurchased']]

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Determine the optimal number of clusters using the Elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(features_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow method results
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')  # Within-Cluster Sum of Squares
plt.show()

# Based on the Elbow method, choose the optimal number of clusters
optimal_clusters = 3

# Apply K-Means clustering
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
clusters = kmeans.fit_predict(features_scaled)

# Add the cluster labels to the original data
data['Cluster'] = clusters

# Visualize the clusters using a scatter plot
plt.scatter(data['TotalAmountSpent'], data['NumberOfItemsPurchased'], c=data['Cluster'], cmap='viridis', alpha=0.7)
plt.title('K-Means Clustering of Customers')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.show()
