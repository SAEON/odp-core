from typing import Any, Optional

from pydantic import BaseModel

from odp.const.db import SubmissionStatus


class SubmissionModelIn(BaseModel):
    user_id: Optional[str]
    data: dict[str, Any]
    status: Optional[SubmissionStatus]
    dataset_file_name: Optional[str]
    collection_id: Optional[str]
    schema_id: Optional[str]


class SubmissionListItemModel(BaseModel):
    id: int
    title: str
    status: str
