from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from odp.const.db import KeywordStatus


class KeywordModel(BaseModel):
    vocabulary_id: str
    id: int
    key: str
    data: dict
    status: KeywordStatus
    parent_id: Optional[int] = Field(None, title='Parent keyword id')
    parent_key: Optional[str] = Field(None, title='Parent keyword')
    schema_id: Optional[str] = Field(None, title="The keyword's validating schema")


class KeywordHierarchyModel(KeywordModel):
    child_keywords: list[KeywordHierarchyModel]


class KeywordModelIn(BaseModel):
    key: str
    data: dict
    parent_id: Optional[int] = Field(None, title='Parent keyword id')


class KeywordModelAdmin(KeywordModelIn):
    status: KeywordStatus
