import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the CSV file
df = pd.read_csv("data/sentiment_analysis.csv")

# Rename columns to match expected names (CASE-SENSITIVE FIX)
df.rename(columns={'Cleaned_Comment': 'comment', 'Sentiment_Label': 'sentiment'}, inplace=True)

# Ensure necessary columns exist
if 'sentiment' not in df.columns or 'comment' not in df.columns:
    raise ValueError(f"CSV must contain 'sentiment' and 'comment' columns. Found: {df.columns}")

# Count sentiment occurrences for pie chart
sentiment_counts = df['sentiment'].value_counts()

# **1. Pie Chart for Sentiment Distribution**
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['green', 'red', 'gray'])
plt.title("Sentiment Distribution")
plt.show()

# **2. Bar Chart for Sentiment Distribution**
plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=['green', 'red', 'gray'])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# **3. Extract Trending Keywords**
positive_comments = " ".join(df[df['sentiment'] == 'positive']['comment'])
negative_comments = " ".join(df[df['sentiment'] == 'negative']['comment'])

# Generate word clouds
def generate_wordcloud(text, title, color):
    wordcloud = WordCloud(width=800, height=400, background_color="white", colormap=color).generate(text)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.show()

generate_wordcloud(positive_comments, "Positive Comments Word Cloud", "Greens")
generate_wordcloud(negative_comments, "Negative Comments Word Cloud", "Reds")
