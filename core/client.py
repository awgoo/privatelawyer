from openai import OpenAI
from core.config import OPENAI_API_KEY
from core.logger import logger

client = OpenAI(api_key=OPENAI_API_KEY)

def chat(messages, model, temperature):

    try:
        res = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )

        usage = res.usage
        logger.info(f"Tokens used: {usage.total_tokens}")

        return res.choices[0].message.content

    except Exception as e:
        logger.error(f"OpenAI Error: {e}")
        raise
