from fastapi import FastAPI, HTTPException
from movie import get_movie_recommendation
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 50

# adding headers to responses for Cross-Origin Response Blocked error
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/movies")
async def generate_snippet_api(prompt: str):    
    validate_input_length(prompt)
    snippet = get_movie_recommendation(prompt)
    return {"snippet": snippet, "keywords": []}

def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.",
        )