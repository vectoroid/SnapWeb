"""
WebSnap

- filename: ./models/base.py
"""
# imports[python_lib]
from aiohttp import ClientError
from contextlib import asynccontextmanager
from uuid import UUID, uuid4

# imports[third_party]
from fastapi import HTTPException
from pydantic import BaseModel, Field

# imports[app]
from ..config import get_settings
from ..db import deta


@asynccontextmanager
async def async_db(dbname: str):
    async_detabase_client = deta.AsyncBase(dbname)
    
    try:
        yield async_detabase_client
    except ClientError:
        HTTPException(status_code=503, detail="Database connection error occurred.")
    finally:
        await async_detabase_client.close()
        
        
class DetaBase(BaseModel):
    """
    Base class for all models:
    - Inherits from `pydantic.BaseModel` for validation
    - Adds 
    """
    id: UUID = Field(default_factory=uuid4)
    