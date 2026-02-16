import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4.1-mini"
TEMPERATURE_ANALYSIS = 0
TEMPERATURE_CREATIVE = 0.7
MAX_RETRIES = 3
