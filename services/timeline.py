from core.client import chat
from core.config import MODEL, TEMPERATURE_ANALYSIS
from utils.retry import retry

SYSTEM = "Gunakan Bahasa Indonesia. Kutip teks Inggris asli jika ada."

@retry
def build_timeline(text):

    prompt = f"""
Extract chronological events.

Format:
Tanggal — Peristiwa — Bukti

{text}
"""

    return chat(
        [
            {"role":"system","content":SYSTEM},
            {"role":"user","content":prompt}
        ],
        MODEL,
        TEMPERATURE_ANALYSIS
    )

