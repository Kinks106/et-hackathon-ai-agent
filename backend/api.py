from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.crew.crew_runner import run_crew
import uvicorn
import os

# Initialize FastAPI app
app = FastAPI(title="Eternal AI Agent API", version="1.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    ticker: str

@app.post("/analyze")
async def analyze_stock(request: AnalysisRequest):
    try:
        # Basic validation (could be expanded)
        if not request.ticker:
            raise HTTPException(status_code=400, detail="Ticker symbol is required")
        
        # Run the crew
        # Note: run_crew is synchronous, which might block the event loop.
        # For production, this should be run in a separate thread or background task.
        company_name = request.ticker  # Simplified for now, can extract/lookup name if needed
        result = run_crew(request.ticker, company_name)
        
        return {"result": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("backend.api:app", host="0.0.0.0", port=8000, reload=True)
