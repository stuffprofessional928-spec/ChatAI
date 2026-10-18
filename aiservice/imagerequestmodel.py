from typing import Annotated, Literal
from pydantic import BaseModel, Field


class ImageRequest(BaseModel):
    model: str
    