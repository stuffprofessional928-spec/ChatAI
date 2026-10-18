from fastapi import APIRouter
from aiservice.aiservice import get_response_from_ai
from aiservice.airequestmodel import create_airequest
from userservice.userrequest import UserRequest, ImageRequest
from aiservice.imageservice import create_image
from starlette import status


router = APIRouter()

@router.get('/', status_code= status.HTTP_200_OK)
async def get_backend_response():
    return {"backend": "working"}

@router.post('/chatAI/v1/', status_code=status.HTTP_200_OK)
async def get_ai_response(user_request: UserRequest):
    json = create_airequest(user_message=user_request.user_message, image= user_request.image, model= user_request.model_name)
    return get_response_from_ai(json)


@router.post('/chatAI/v1/image', status_code=status.HTTP_200_OK)
async def create_image_from_text(image_request: ImageRequest):
    
    data = {
        "model": image_request.model,
        "prompt": image_request.prompt,
        "aspect_ration": image_request.aspect_ratio,
        "resolution": image_request.resolution,
        "output": image_request.output
    }
    print("request ========= ", image_request.model_dump())
    return create_image(data)