# AI Blog Generator

This app generates a blog post using OpenAI based on a keyword. Includes SEO metrics and placeholder affiliate links.

## Setup

1. Clone the repo.
2. Create a '.env' file with your OpenAI key (all you must do is replace it and in your terminal use the two lines to do the change):
   - touch .env
   - open .env
   - Change the OpenAI key to yours

## Please find below the steps for set up on your MAC Terminal, or you could alternatively use VS Code if you are using Windows

1. ```bash
2. git clone https://github.com/devika-nambisan/ai-blog-generator-interview-DevikaNambisan..git
3. cd ai-blog-generator-interview-DevikaNambisan.
4. python3 -m venv venv
5. source venv/bin/activate
6. pip install -r requirements.txt
7. venv/bin/python/ -m flask run (for the local running, and then u can use the browser to see)
8. python app.py (if step 7 does not work, attempt this to run the app)

Notes on the Use of Mock

- SEO metrics are mocked using a simple random generator in `seo_fetcher.py`.
- OpenAI calls in `ai_generator.py` are mocked by default (`USE_MOCK=True`) to avoid API quota issues
- To enable real OpenAI API calls, set `USE_MOCK=False` and provide your own API key in `.env`.

What an example local host call on browser looks like: http://127.0.0.1:5000/generate?keyword=wireless%20earbuds
