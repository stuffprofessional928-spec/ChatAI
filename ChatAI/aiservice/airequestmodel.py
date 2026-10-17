from typing import Annotated, Literal
from pydantic import BaseModel, Field




class TextPart(BaseModel):
    type: Literal["text"] = "text"
    text: str
    
class ImagePart(BaseModel):
    type: Literal["image_url"] = "image_url"
    image_url: ImageURL


class ImageURL(BaseModel):
    url: str


# Pydantic picks the right class by reading the "type" field
ContentPart = Annotated[TextPart | ImagePart, Field(discriminator="type")]


class ChatRequest(BaseModel):
    model: str
    messages: list[Message]
    
class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: list[ContentPart]
    
    
def create_airequest(user_message: str = "", image: str = "", model: str = "meta-llama/llama-4-maverick" ):
    if user_message != "" and image != "":
        return ChatRequest(
        model=model,  # replace with a vision-capable model name
        messages=[
        Message(
            role="user",
            content=[
                TextPart(text=f"{user_message}"),
                ImagePart(
                    image_url=ImageURL(
                        url=f"{image}"
                        )
                    ),
                 ],
            )
        ],
    )
    elif user_message != "" and image == "":
        return ChatRequest(
        model=model,  # replace with a vision-capable model name
        messages=[
        Message(
            role="user",
            content=[
                TextPart(text=f"{user_message}")
                 ],
            )
        ],
    )
    elif user_message == "" and image != "":
        return ChatRequest(
                model=model,  # replace with a vision-capable model name
                messages=[
                Message(
                    role="user",
                    content=[
                        ImagePart(
                            image_url=ImageURL( url=f"{image}")) 
                         ],
                    )
                ],
            )
    else :
        return ChatRequest(
                        model=model,  # replace with a vision-capable model name
                        messages=[
                        Message(
                            role="user",
                            content=[
                                TextPart(text=""), 
                                 ],
                            )
                        ],
                    )
