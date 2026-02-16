from core.client import chat
from core.config import MODEL, TEMPERATURE_ANALYSIS
from utils.retry import retry

SYSTEM = "Selalu jawab dalam Bahasa Indonesia. Jika ada teks Inggris tampilkan teks aslinya."

@retry
def analyze_document(text):

    prompt = f"""
Analyze document and detect harmful clauses.

Output format:

KLAUSUL 1
Teks Asli:
Risiko:
Penjelasan:
Saran Perbaikan:

KLAUSUL 2
...

Document:
{text}
"""

    result = chat(
        [
            {"role":"system","content":SYSTEM},
            {"role":"user","content":prompt}
        ],
        MODEL,
        TEMPERATURE_ANALYSIS
    )

    return result
