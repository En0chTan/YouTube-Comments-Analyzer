# YouTube-Comments-Analyzer

This is a YouTube Comment Sentiment Analyzer built with Streamlit, Python, and NLP techniques. The app fetches YouTube comments, processes them, and visualizes sentiment distributions using charts and word clouds.

## Features
<ul>
    ✅ Fetch YouTube Comments using YouTube Data API
    ✅ Sentiment Analysis (Positive, Negative, Neutral) with NLP
    ✅ Data Visualization (Pie & Bar Charts)
    ✅ Word Cloud Generation for Sentiment Categories
    ✅ Streamlit Web UI for easy interaction
</ul>


## Installation & Setup
1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/youtube-comment-analyzer.git
cd youtube-comment-analyzer
```

2️⃣ Create a Virtual Environment (Optional)
```sh
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

4️⃣ Add YouTube API Key
1. Create a .streamlit/secrets.toml file
2. Add the following content:
    ```sh
    [youtube]
    api_key = "YOUR_YOUTUBE_API_KEY"
    ```

5️⃣ Run the App Locally
```sh
streamlit run app.py
```
