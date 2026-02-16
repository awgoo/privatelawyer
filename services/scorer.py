from core.client import chat
from core.config import MODEL, TEMPERATURE_ANALYSIS
from utils.retry import retry

SYSTEM = "Jawab dalam Bahasa Indonesia. Kutip teks Inggris dari fakta jika relevan."

@retry
def score_case(facts):

    prompt = f"""
Evaluate legal strength.

Return:

Score: Weak / Medium / Strong

Alasan:
- poin
- poin

Facts:
{facts}
"""

    return chat(
        [
            {"role":"system","content":SYSTEM},
            {"role":"user","content":prompt}
        ],
        MODEL,
        TEMPERATURE_ANALYSIS
    )

