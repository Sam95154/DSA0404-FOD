from collections import Counter

# Load the customer reviews dataset
reviews = ["This product is amazing! I love it!", "I'm not impressed with this product.", "The product is okay, but not great."]

# Tokenize the reviews into words
words = " ".join(reviews).split()

# Calculate the frequency distribution of words
word_counts = Counter(words)

# Print the 10 most common words and their frequencies
print(word_counts.most_common(10))
