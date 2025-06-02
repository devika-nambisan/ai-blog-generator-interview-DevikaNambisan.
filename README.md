# AI Blog Generator

This app generates a blog post using OpenAI based on a keyword. Includes SEO metrics and placeholder affiliate links.

## Setup

1. Clone the repo.
2. Create a `.env` file with your OpenAI key:

## Please find below the steps for set up on your MAC Terminal or you could alterantively use VS Code if you are using Windows

```bash
git clone https://github.com/devika-nambisan/ai-blog-generator-interview-DevikaNambisan..git
cd ai-blog-generator-interview-DevikaNambisan.
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py OR venv/bin/python/ -m flask run (for the local running and then u can use the browser to see) 



## Notes on Mocking

- SEO metrics are mocked using a simple random generator in `seo_fetcher.py`.
- OpenAI calls in `ai_generator.py` are mocked by default (`USE_MOCK=True`) to avoid API quota issues and facilitate offline development.
- To enable real OpenAI API calls, set `USE_MOCK=False` and provide your own API key in `.env`.

what an example local host call on broswer looks like: http://127.0.0.1:5000/generate?keyword=wireless%20earbuds
