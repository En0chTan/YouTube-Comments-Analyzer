import pandas as pd
import re
import os

def clean_comment(comment):
    """Cleans a YouTube comment while keeping emojis."""
    """Removes mentions, hashtags, links, and extra spaces."""
    comment = comment.lower()  # convert to lowercase
    comment = re.sub(r"@\w+", "", comment)  # remove @mentions
    comment = re.sub(r"#\w+", "", comment)  # remove hashtags
    comment = re.sub(r"http\S+|www\S+", "", comment)  # remove links
    comment = re.sub(r"\s+", " ", comment).strip()  # remove extra spaces
    return comment

# Load raw comments
input_file = "data/comments.csv"
output_file = "data/cleaned_comments.csv"

if os.path.exists(input_file):
    df = pd.read_csv(input_file)
    
    # Apply cleaning function
    df["Cleaned_Comment"] = df["Comment"].apply(clean_comment)

    # Save cleaned comments
    df[["Cleaned_Comment"]].to_csv(output_file, index=False)
    print("✅ Cleaned comments saved to data/cleaned_comments.csv!")
else:
    print("❌ Error: data/comments.csv not found. Run fetch_comments.py first.")
