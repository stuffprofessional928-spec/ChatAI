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
    
    
    
class ImageRequest(BaseModel):
    model: str = Field(min_length=3, default="black-forest-labs/flux-3-image-klein")
    prompt: str 
    image: str
    aspect_ratio: str
    resolution: str
    dimensions: str
    quality: str
    output: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "model":"Which llm you want to use",
                "prompt":"Hi how are you",
                "image":"image url",
                "aspect_ratio": "16:9",
                "resolution":"1K",
                "dimensions": "1024x1024",
                "quality": "standard",
                "output": "png"
            }
        }
    }