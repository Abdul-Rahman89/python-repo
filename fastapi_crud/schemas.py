from pydantic import BaseModel
from typing import Optional

# Base schema with common attributes
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Schema for creating a todo (inherits from TodoBase)
class TodoCreate(TodoBase):
    pass

# Schema for updating a todo (all fields optional)
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Schema for response (includes id)
class Todo(TodoBase):
    id: int

    class Config:
        from_attributes = True  # Enables ORM mode
