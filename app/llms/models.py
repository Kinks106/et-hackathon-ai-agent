from crewai import LLM

groq_llama_70b = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
     max_tokens=2000,
)

mistral = LLM(
    model="mistral/mistral-small-2506"
)
