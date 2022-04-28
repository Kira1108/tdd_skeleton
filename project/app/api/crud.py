from app.models.pydantic import SummaryPayloadSchema
from app.models.text_summary import TextSummary


def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    summary.insert()
    return summary.id