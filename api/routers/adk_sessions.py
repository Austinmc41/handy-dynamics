from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from api.dependencies.dependencies import get_adk_session_repository
from api.services.adk_sesssion_service import ADKSessionService
from api.models.schemas.adk_session import ADKSession


router = APIRouter(
    prefix="/adk_sessions",
    tags=["adk_sessions"],
)

@router.get('/', response_model=List[ADKSession])
def get_adk_sessions(repo = Depends(get_adk_session_repository)):
    service = ADKSessionService(repo)
    return service.get_adk_sessions()
