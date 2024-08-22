from typing import Optional

from pydantic import BaseModel

from odp.const.db import ArchiveAdapter


class ArchiveModel(BaseModel):
    id: str
    url: str
    adapter: ArchiveAdapter
    scope_id: str
    resource_count: int


class ArchiveResourceModel(BaseModel):
    archive_id: str
    resource_id: str
    path: str
    title: str
    description: Optional[str]
    filename: Optional[str]
    mimetype: Optional[str]
    size: Optional[int]
    md5: Optional[str]
    timestamp: str
    provider_id: str
    provider_key: str
