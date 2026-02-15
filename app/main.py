from app.crew.crew_runner import run_crew
from dotenv import load_dotenv
load_dotenv()   # FIRST LINE

if __name__ == "__main__":
    result = run_crew("ETERNAL.NS", "ETERNAL LIMITED")
    print(result)
