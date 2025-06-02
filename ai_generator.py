import openai
import os
from seo_fetcher import fetch_seo_metrics

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(keyword):
    seo_metrics = fetch_seo_metrics(keyword)
    
    prompt = f"""
Write a 700-word blog post for the keyword "{keyword}" with this structure:
- Introduction (with keyword)
- Key benefits
- SEO statistics: Volume: {seo_metrics['search_volume']}, Difficulty: {seo_metrics['keyword_difficulty']}, CPC: ${seo_metrics['avg_cpc']}
- Product Recommendations with affiliate links (use placeholders like {{AFF_LINK_1}})
- Conclusion

Include markdown headers, bullet points, and bold text. Write in a friendly, engaging tone.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    blog_post = response['choices'][0]['message']['content']
    
    # Replace placeholders
    for i in range(1, 4):
        blog_post = blog_post.replace(f"{{{{AFF_LINK_{i}}}}}", f"https://example.com/affiliate/{keyword}/{i}")
    
    return blog_post, seo_metrics

