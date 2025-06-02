import random

def fetch_seo_metrics(keyword):
    return {
        "search_volume": random.randint(1000, 5000),
        "keyword_difficulty": random.randint(10, 80),
        "avg_cpc": round(random.uniform(0.5, 5.0), 2)
    }

