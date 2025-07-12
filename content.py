import feedparser
from flask import Flask, render_template_string

app = Flask(__name__)

# List of RSS feed URLs
RSS_FEEDS = {
    'BBC': 'http://feeds.bbci.co.uk/news/rss.xml',
    'CNN': 'http://rss.cnn.com/rss/edition.rss',
    'Reuters': 'http://feeds.reuters.com/reuters/topNews'
}

# HTML template for displaying articles
HTML_TEMPLATE = """
<!doctype html>
<html>
<head><title>News Aggregator</title></head>
<body>
    <h1>📰 News Aggregator</h1>
    {% for source, articles in news.items() %}
        <h2>{{ source }}</h2>
        <ul>
        {% for article in articles %}
            <li><a href="{{ article.link }}">{{ article.title }}</a></li>
        {% endfor %}
        </ul>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def home():
    news = {}
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        news[source] = feed.entries[:5]  # Get top 5 articles
    return render_template_string(HTML_TEMPLATE, news=news)

if __name__ == '__main__':
    app.run(debug=True)



