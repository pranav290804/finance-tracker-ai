import os
import pandas as pd
import cohere
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def ask_cohere(df, question):
    csv_data = df.to_csv(index=False)

    prompt = f"""
You are a smart financial assistant.
Here is my bank transaction data:

{csv_data}

Answer this question:
{question}
"""

    response = co.chat(
        model="command-r-plus",
        message=prompt,
    )

    return response.text
