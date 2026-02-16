from core.client import chat
from core.config import MODEL, TEMPERATURE_CREATIVE
from utils.retry import retry

SYSTEM = "Jawab dalam Bahasa Indonesia. Jika ada istilah legal Inggris tampilkan dalam kurung."

@retry
def generate_reply(context):

    prompt = f"""
Write professional reply email.

Tone:
- calm
- firm
- legally safe

Situation:
{context}
"""

    return chat(
        [
            {"role":"system","content":SYSTEM},
            {"role":"user","content":prompt}
        ],
        MODEL,
        TEMPERATURE_CREATIVE
    )

