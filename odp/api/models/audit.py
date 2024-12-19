from typing import Any, Optional

from pydantic import BaseModel

from odp.const.db import AuditCommand, IdentityCommand


class AuditModel(BaseModel):
    table: str
    tag_id: Optional[str]
    audit_id: int
    client_id: str
    user_id: Optional[str]
    user_name: Optional[str]
    command: AuditCommand
    timestamp: str


class CollectionAuditModel(AuditModel):
    collection_id: str
    collection_key: str
    collection_name: str
    collection_doi_key: Optional[str]
    collection_provider_id: str


class CollectionTagAuditModel(AuditModel):
    collection_tag_id: str
    collection_tag_collection_id: str
    collection_tag_user_id: Optional[str]
    collection_tag_user_name: Optional[str]
    collection_tag_data: dict[str, Any]


class RecordAuditModel(AuditModel):
    record_id: str
    record_doi: Optional[str]
    record_sid: Optional[str]
    record_metadata: dict[str, Any]
    record_collection_id: str
    record_schema_id: str
    record_parent_id: Optional[str]


class RecordTagAuditModel(AuditModel):
    record_tag_id: str
    record_tag_record_id: str
    record_tag_user_id: Optional[str]
    record_tag_user_name: Optional[str]
    record_tag_data: dict[str, Any]


class ProviderAuditModel(AuditModel):
    provider_id: str
    provider_key: str
    provider_name: str
    provider_users: list[str]


class KeywordAuditModel(AuditModel):
    vocabulary_id: str
    keyword_id: int
    key: str
    data: dict[str, Any]
    status: str
    parent_id: Optional[int]


class IdentityAuditModel(BaseModel):
    audit_id: int
    client_id: str
    client_user_id: str | None
    client_user_name: str | None
    command: IdentityCommand
    completed: bool
    error: str | None
    timestamp: str
    user_id: str
    user_email: str
    user_active: bool
    user_roles: list[str]
