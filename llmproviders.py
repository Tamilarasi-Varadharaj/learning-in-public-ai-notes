import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

import warnings
warnings.filterwarnings("ignore")
load_dotenv()

with open("config.json","r") as f:
    CONFIG = json.load(f)

# OpenAI Function    
def run_openai(message):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=CONFIG["openai"]["model"],
        messages=message,
        temperature=CONFIG["openai"]["temperature"],
        max_tokens=CONFIG["openai"]["max_tokens"]
    )
    return response.choices[0].message.content

#Gemini Function
def run_gemini(message):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    response = genai.chat.create(
        model=CONFIG["gemini"]["model"],
        messages=message,
        temperature=CONFIG["gemini"]["temperature"],
        max_output_tokens=CONFIG["gemini"]["max_tokens"]
    )
    return response.last.strip()

def run_llm(history):
    provider = CONFIG["provider"]
    if provider == "openai":
        return run_openai(history)
    elif provider == "gemini":  
        conversation_text = "\n".join(f"{m['role']}: {m['content']}" for m in history)
        return run_gemini(conversation_text)
    else :
        raise ValueError(f"Unsupported provider: {provider}")
    