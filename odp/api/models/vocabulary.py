from typing import Any

from pydantic import BaseModel

from odp.api.models import KeywordHierarchyModel


class VocabularyModel(BaseModel):
    id: str
    uri: str
    schema_id: str
    schema_uri: str
    static: bool


class VocabularyDetailModel(VocabularyModel):
    schema_: dict[str, Any]
    keywords: list[KeywordHierarchyModel]
