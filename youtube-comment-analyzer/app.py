import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from wordcloud import WordCloud

# Load Data
DATA_PATH = os.path.join(os.getcwd(), "data", "sentiment_analysis.csv")

if not os.path.exists(DATA_PATH):
    st.error("CSV file not found! Please ensure `data/sentiment_analysis.csv` exists.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# Rename columns to expected names if necessary
df.rename(columns={'Cleaned_Comment': 'comment', 'Sentiment_Label': 'sentiment'}, inplace=True)

# Ensure necessary columns exist
if 'sentiment' not in df.columns or 'comment' not in df.columns:
    st.error(f"CSV must contain 'sentiment' and 'comment' columns. Found: {df.columns}")
    st.stop()

if df.empty:
    st.error("The dataset is empty. Please check your CSV file.")
    st.stop()

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Sentiment Distribution", "Word Clouds"])

# Sentiment Distribution
if page == "Sentiment Distribution":
    st.title("Sentiment Distribution")

    # Count sentiment occurrences
    sentiment_counts = df['sentiment'].value_counts()

    if sentiment_counts.empty:
        st.warning("No sentiment data available.")
    else:
        # Pie Chart
        st.subheader("Pie Chart Representation")
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', 
               colors=['green', 'red', 'gray'])
        ax.set_title("Sentiment Distribution")
        st.pyplot(fig)

        # Bar Chart
        st.subheader("Bar Chart Representation")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, 
                    palette=['green', 'red', 'gray'], ax=ax)
        ax.set_title("Sentiment Distribution")
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Count")
        st.pyplot(fig)

# Word Clouds
elif page == "Word Clouds":
    st.title("Word Clouds for Sentiments")

    def generate_wordcloud(text, color_func):
        if text.strip():
            wordcloud = WordCloud(width=800, height=400, background_color="white",
                                  colormap=color_func).generate(text)
            return wordcloud
        return None

    # Filter comments by sentiment
    positive_comments = " ".join(df[df['sentiment'] == 'positive']['comment'])
    negative_comments = " ".join(df[df['sentiment'] == 'negative']['comment'])
    neutral_comments = " ".join(df[df['sentiment'] == 'neutral']['comment'])

    # Word Clouds
    for sentiment, comments, colormap in [("Positive", positive_comments, "Greens"), 
                                          ("Negative", negative_comments, "Reds"),
                                          ("Neutral", neutral_comments, "Blues")]:
        st.subheader(f"{sentiment} Comments Word Cloud")
        wc = generate_wordcloud(comments, colormap)
        if wc:
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.imshow(wc, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning(f"No {sentiment.lower()} comments found.")
