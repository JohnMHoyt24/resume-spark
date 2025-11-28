"""
FastAPI application with basic endpoints for demonstration.
This module provides a simple API with a root endpoint and an items endpoint.
"""
from fastapi import FastAPI

# Initialize the FastAPI application instance
app = FastAPI()

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