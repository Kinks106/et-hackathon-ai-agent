from crewai import LLM
import os

groq_llama_70b = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=4000,
    api_key=os.getenv("GROQ_API_KEY")
)

groq_llama_8b = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0,
    max_tokens=4000,
    api_key=os.getenv("GROQ_API_KEY")
)

mistral = LLM(
    model="mistral/mistral-small-2506"
)
