from pydantic import BaseModel


class OptionRequest(BaseModel):
    option_id: int

class OptionResponse(BaseModel):
    id: int
    description: str
