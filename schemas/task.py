from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel
from datetime import date

class Task(BaseModel):
    id: Optional[int]
    name: str
    description: str
    date: date

class UpdateTask(BaseModel):
    name: Optional[str]
    description: Optional[str]
    date: Optional[date]