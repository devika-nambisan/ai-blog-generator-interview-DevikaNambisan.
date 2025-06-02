from flask import Flask, request, jsonify
from dotenv import load_dotenv
from ai_generator import generate_blog_post
import os
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

load_dotenv()

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

# Daily scheduled blog generation for fixed keyword
def daily_generate():
    keyword = "wireless earbuds"
    post, metrics = generate_blog_post(keyword)
    filename = f"blog_posts/{keyword.replace(' ', '_')}_{datetime.now().date()}.md"
    
    # Make sure the blog_posts directory exists
    import os as os_module
    os_module.makedirs("blog_posts", exist_ok=True)

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
    daily_generate() #For Demo Only
    app.run(debug=True)
