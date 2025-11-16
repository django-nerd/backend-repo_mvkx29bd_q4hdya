"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List

# Example schemas (you can keep these for testing/admin tools)

class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Construction business specific schemas

class Lead(BaseModel):
    """
    Leads collected from the website contact form
    Collection name: "lead"
    """
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, description="Contact phone number")
    service: Optional[str] = Field(None, description="Requested service")
    message: Optional[str] = Field(None, max_length=2000)
    source: str = Field("website", description="Lead source")

class Project(BaseModel):
    """
    Portfolio projects displayed on the website
    Collection name: "project"
    """
    title: str = Field(..., min_length=2, max_length=120)
    description: str = Field(..., max_length=2000)
    category: str = Field(..., description="e.g., Residential, Commercial, Renovation")
    location: Optional[str] = None
    images: Optional[List[HttpUrl]] = Field(default=None, description="Image URLs")
    featured: bool = Field(False, description="Featured on homepage")
