'''
把service和model层链接起来
'''
from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()

@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    """Request 的schema现在是一个url, response的schema现在是一个id"""
    summary_id = crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object