import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os

# Download VADER if not already installed
nltk.download("vader_lexicon")

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(comment):
    """Returns sentiment score and label (Positive, Neutral, Negative)"""
    score = sia.polarity_scores(comment)["compound"]
    if score >= 0.05:
        return score, "Positive"
    elif score <= -0.05:
        return score, "Negative"
    else:
        return score, "Neutral"

# Load cleaned comments
input_file = "data/cleaned_comments.csv"
output_file = "data/sentiment_analysis.csv"

if os.path.exists(input_file):
    df = pd.read_csv(input_file)

    # Apply sentiment analysis
    df[["Sentiment_Score", "Sentiment_Label"]] = df["Cleaned_Comment"].apply(
        lambda x: pd.Series(analyze_sentiment(x))
    )

    # Save the results
    df.to_csv(output_file, index=False)
    print("✅ Sentiment analysis completed and saved to data/sentiment_analysis.csv!")
else:
    print("❌ Error: data/cleaned_comments.csv not found. Run clean_comments.py first.")
