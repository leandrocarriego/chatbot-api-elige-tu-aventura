from typing import List, Optional
from pydantic import BaseModel

from .Option import OptionResponse


class NodeResponse(BaseModel):
    description: str
    options: Optional[List[OptionResponse]]
