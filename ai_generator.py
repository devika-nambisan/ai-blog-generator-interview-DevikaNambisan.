import os
import openai
from seo_fetcher import fetch_seo_metrics

openai.api_key = os.getenv("OPENAI_API_KEY")
USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"

def generate_blog_post(keyword):
    seo_metrics = fetch_seo_metrics(keyword)
    
    if USE_MOCK:
        # Return a mock blog post string (700 words approx can be adjusted)
        blog_post = f"""
# {keyword.capitalize()}: The Ultimate Guide

**Introduction**

Looking for the best {keyword}? You're in the right place! This guide covers everything you need to know.

**Key Benefits**

- Benefit 1 of {keyword}
- Benefit 2 of {keyword}
- Benefit 3 of {keyword}

**SEO Statistics**

- Volume: {seo_metrics['search_volume']}
- Difficulty: {seo_metrics['keyword_difficulty']}
- CPC: ${seo_metrics['avg_cpc']}

**Product Recommendations**

- [Awesome Product 1]({{AFF_LINK_1}})
- [Awesome Product 2]({{AFF_LINK_2}})
- [Awesome Product 3]({{AFF_LINK_3}})

**Conclusion**

Whether you're new or experienced, {keyword} can make your life better!
"""
    else:
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
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        blog_post = response['choices'][0]['message']['content']

    # Replace affiliate link placeholders with dummy URLs
    for i in range(1, 4):
        blog_post = blog_post.replace(f"{{{{AFF_LINK_{i}}}}}", f"https://example.com/affiliate/{keyword}/{i}")

    return blog_post, seo_metrics
