from fastapi import APIRouter
from aiservice.aiservice import get_response_from_ai
from aiservice.airequestmodel import create_airequest
from userservice.userrequest import UserRequest
from starlette import status


router = APIRouter()

@router.get('/', status_code= status.HTTP_200_OK)
async def get_backend_response():
    return {"backend": "working"}

@router.post('/chatAI/v1/', status_code=status.HTTP_200_OK)
async def get_ai_response(user_request: UserRequest):
    json = create_airequest(user_message=user_request.user_message, image= user_request.image, model= user_request.model_name)
    return get_response_from_ai(json)