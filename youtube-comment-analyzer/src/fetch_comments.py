from googleapiclient.discovery import build
import pandas as pd
import re
import os
import streamlit as st
from dotenv import load_dotenv  # Import dotenv

# Load API Key
if "youtube" in st.secrets:  # If running on Streamlit Cloud
    API_KEY = st.secrets["youtube"]["API_KEY"]
else:  
    load_dotenv()  # Else load from .env locally
    API_KEY = os.getenv("YOUTUBE_API_KEY")  

if not API_KEY:
    raise ValueError("❌ API Key not found! Please check your .env file or Streamlit Secrets.")

# Extract VIDEO_ID from URL
def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

YOUTUBE_URL = "https://youtu.be/7ARBJQn6QkM?si=6bazwm9w_vKXrORK"
VIDEO_ID = extract_video_id(YOUTUBE_URL)
print("Extracted VIDEO_ID:", VIDEO_ID)

# Connect to YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_comments(video_id, max_comments=100):
    """Fetch comments from a YouTube video."""
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=min(max_comments, 100)
    )
    response = request.execute()

    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return pd.DataFrame(comments, columns=["Comment"])

# Fetch and Save Comments
df = get_comments(VIDEO_ID)
df.to_csv("data/comments.csv", index=False)

print("✅ Comments fetched and saved to data/comments.csv!")
