import os
import openai

USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(keyword):
    # Mock SEO metrics for consistent mock behavior or import from seo_fetcher.py if you want dynamic ones
    from seo_fetcher import fetch_seo_metrics
    seo_metrics = fetch_seo_metrics(keyword)

    if USE_MOCK:
        # Return a fake blog post with placeholders, no OpenAI call
        blog_post = f"""
# {keyword} - The Ultimate Guide

**Introduction**  
Discover the amazing benefits of {keyword} in this comprehensive guide.

**Key Benefits**  
- Benefit 1 of {keyword}  
- Benefit 2 of {keyword}  
- Benefit 3 of {keyword}

**SEO Statistics**  
- Search Volume: {seo_metrics['search_volume']}  
- Difficulty: {seo_metrics['keyword_difficulty']}  
- Average CPC: ${seo_metrics['avg_cpc']}

**Product Recommendations**  
- [Product 1]({{AFF_LINK_1}})  
- [Product 2]({{AFF_LINK_2}})  
- [Product 3]({{AFF_LINK_3}})

**Conclusion**  
{keyword} can improve your life in many ways. Try it today!
"""
