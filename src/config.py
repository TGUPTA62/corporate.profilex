import os
from dotenv import load_dotenv

# Load .env file from project root by default
load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not SERPAPI_API_KEY or not OPENAI_API_KEY:
    raise ValueError("API keys not found in environment variables")
