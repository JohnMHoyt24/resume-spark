"""
FastAPI application with basic endpoints for demonstration.
This module provides a simple API with a root endpoint and an items endpoint.
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Initialize the FastAPI application instance and Groq client
app = FastAPI()
client = Groq(api_key=GROQ_API_KEY)

# Configure CORS middleware to allow frontend access
origins = [
    "http://localhost:8000"
]


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a simple greeting message.
    
    Returns:
        dict: A dictionary containing a welcome message
    """
    return {
        "message": "Hello World",
        "version": "1.0.0"
        }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """
    Retrieve an item by its ID with an optional query parameter.
    
    Args:
        item_id (int): The unique identifier of the item
        q (str | None, optional): An optional query string parameter. Defaults to None.
    
    Returns:
        dict: A dictionary containing the item_id and optionally the query parameter q
    """
    # If a query parameter is provided, include it in the response
    if q:
        return {"item_id": item_id, "q": q}
    # Otherwise, return just the item_id
    return {"item_id": item_id}

@app.post("/api/generate-resume")
async def generate_resume(resume_data: str):
    """
    Generate a resume from the provided data.
    
    Args:
        resume_data (ResumeData): The data required to generate a resume
    
    Returns:
        dict: A dictionary containing the generated resume
    """
    return {"resume": resume_data.model_dump()}