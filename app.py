from flask import Flask, request, jsonify
from dotenv import load_dotenv
from ai_generator import generate_blog_post
from seo_fetcher import fetch_seo_metrics
import os
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

load_dotenv()
print("OPENAI_API_KEY is:", os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.start()

# Daily job with a fixed keyword
def daily_generate():
    keyword = "wireless earbuds"
    post, metrics = generate_blog_post(keyword)
    filename = f"blog_posts/{keyword.replace(' ', '_')}_{datetime.now().date()}.md"
    with open(filename, "w") as f:
        f.write(post)
    print(f"[{datetime.now()}] Blog saved to {filename}")

scheduler.add_job(daily_generate, 'interval', days=1)

@app.route('/')
def home():
    return "Welcome to the AI Blog Generator! Use /generate?keyword=your_keyword to get a blog post."

@app.route('/generate')
def generate():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Please provide a keyword"}), 400
    post, metrics = generate_blog_post(keyword)
    return jsonify({
        "keyword": keyword,
        "seo_metrics": metrics,
        "blog_post": post
    })

if __name__ == '__main__':
    app.run(debug=True)
