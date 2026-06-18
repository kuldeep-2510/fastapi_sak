from pydantic import BaseModel
from typing import Any

class ResponseModel(BaseModel):
    success: bool
    status_code: int
    message: str
    data: Any = None