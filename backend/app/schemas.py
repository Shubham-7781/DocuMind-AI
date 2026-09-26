from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


# --- Auth ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: str
    email: EmailStr
    full_name: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


# --- Documents ---
class DocumentOut(BaseModel):
    id: str
    filename: str
    extension: str
    size_bytes: int
    status: str
    error_message: Optional[str] = None
    num_chunks: int
    num_pages: int
    created_at: datetime

    class Config:
        from_attributes = True


# --- Chat ---
class ChatSessionCreate(BaseModel):
    title: Optional[str] = "New chat"
    document_ids: Optional[List[str]] = None


class ChatSessionUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=120)


class ChatSessionScopeUpdate(BaseModel):
    # Empty list / null = scope cleared (search across all documents again).
    document_ids: Optional[List[str]] = None


class ChatSessionOut(BaseModel):
    id: str
    title: str
    document_ids: List[str] = []
    created_at: datetime

    class Config:
        from_attributes = True


class SourceRef(BaseModel):
    source: str
    page: int
    snippet: str
    document_id: Optional[str] = None


class ChatMessageOut(BaseModel):
    id: str
    role: str
    content: str
    sources: List[SourceRef] = []
    latency_ms: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True


class ChatRequest(BaseModel):
    session_id: str
    question: str = Field(min_length=1, max_length=4000)
