from pydantic import BaseModel, Field
from typing import Optional



class UserRequest(BaseModel):
    model_name: str = Field(min_length=3)
    user_message: str 
    image: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "model_name":"Which llm you want to use",
                "user_message":"Hi how are you",
                "image":"image url"
            }
        }
    }