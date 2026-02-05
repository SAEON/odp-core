from typing import Any

from pydantic import BaseModel


class SubmissionModelIn(BaseModel):
    user_id: str
    data: dict[str, Any]


class SubmissionListItemModel(BaseModel):
    id: int
    title: str
    status: str
