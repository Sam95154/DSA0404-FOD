import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import string

# Load the dataset from a CSV file
df = pd.read_csv('data.csv')

# Preprocess the text data
stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return words

df['feedback'] = df['feedback'].apply(lambda x: preprocess_text(x))

# Calculate the frequency distribution of words
word_counts = Counter([word for words in df['feedback'] for word in words])

# Get user input for N
N = int(input("Enter the value of N: "))

# Display the top N most frequent words and their corresponding frequencies
top_N_words = word_counts.most_common(N)
for word, count in top_N_words:
    print(f"{word}: {count}")

# Plot a bar graph to visualize the top N most frequent words and their frequencies
plt.bar([word[0] for word in top_N_words], [word[1] for word in top_N_words])
plt.xticks(rotation=90)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title(f"Top {N} Most Frequent Words")
plt.show()
