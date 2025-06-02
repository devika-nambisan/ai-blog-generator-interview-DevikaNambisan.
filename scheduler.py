from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from ai_generator import generate_blog_post
import os

def daily_generate():
    keyword = "wireless earbuds"
    post, metrics = generate_blog_post(keyword)
    
    # Ensure the blog_posts directory exists
    os.makedirs("blog_posts", exist_ok=True)
    
    filename = f"blog_posts/{keyword.replace(' ', '_')}_{datetime.now().date()}.md"
    with open(filename, "w") as f:
        f.write(post)
    
    print(f"[{datetime.now()}] Blog saved to {filename}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_generate, 'interval', days=1)
    scheduler.start()

