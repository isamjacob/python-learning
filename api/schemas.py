
# PYDANTIC SCHEMAS — Data Validation

from pydantic import BaseModel, EmailStr
from typing import Optional


# Schema for CREATING a student
class StudentCreate(BaseModel):
    name  : str
    email : str
    age   : int
    city  : Optional[str] = None   # optional field
    marks : Optional[float] = 0    # optional with default


# Schema for UPDATING a student
class StudentUpdate(BaseModel):
    name  : Optional[str]   = None
    email : Optional[str]   = None
    age   : Optional[int]   = None
    city  : Optional[str]   = None
    marks : Optional[float] = None


# Schema for RESPONSE — what API sends back
class StudentResponse(BaseModel):
    id        : int
    name      : str
    email     : str
    age       : int
    city      : Optional[str]
    marks     : float
    is_active : bool

    class Config:
        from_attributes = True   # allows ORM objects to be serialized