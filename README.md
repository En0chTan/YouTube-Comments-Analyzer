# YouTube Comments Analyzer

This is a YouTube Comment Sentiment Analyzer built with Streamlit, Python, and NLP techniques. The app fetches YouTube comments, processes them, and visualizes sentiment distributions using charts and word clouds.

## Features
<ul>
    <li>Fetch YouTube Comments using YouTube Data API</li>
    <li>Sentiment Analysis (Positive, Negative, Neutral) with NLP</li>
    <li>Data Visualization (Pie & Bar Charts)</li>
    <li>Word Cloud Generation for Sentiment Categories</li>
    <li>Streamlit Web UI for easy interaction</li>
</ul>


## Installation & Setup
1️1. Clone the Repository
```sh
git clone https://github.com/yourusername/youtube-comment-analyzer.git
cd youtube-comment-analyzer
```

2️. Create a Virtual Environment (Optional)
```sh
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3️. Install Dependencies
```sh
pip install -r requirements.txt
```

4️. Add YouTube API Key
<br></br>
I. Create a .streamlit/secrets.toml file
<br></br>
II. Add the following content:
    ```sh
    [youtube]
    api_key = "YOUR_YOUTUBE_API_KEY"
    ```
<br></br>

5️. Run the App Locally
```sh
streamlit run app.py
```
