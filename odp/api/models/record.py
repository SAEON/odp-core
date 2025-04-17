import re
from typing import Any, Optional

from pydantic import BaseModel, Field, root_validator, validator

from odp.api.models.tag import TagInstanceModel
from odp.const import DOI_REGEX, ODPMetadataSchema, SID_REGEX


class RecordModel(BaseModel):
    id: str
    doi: Optional[str]
    sid: Optional[str]
    collection_id: str
    collection_key: str
    collection_name: str
    provider_id: str
    provider_key: str
    provider_name: str
    schema_id: str
    schema_uri: str
    parent_id: Optional[str]
    parent_doi: Optional[str]
    child_dois: dict[str, str] = Field(..., title='Mapping of child DOIs to corresponding IDs')
    metadata: dict[str, Any]
    validity: dict[str, Any]
    timestamp: str
    tags: list[TagInstanceModel]
    published_catalog_ids: list[str]


class RecordModelIn(BaseModel):
    doi: str = Field(None, regex=DOI_REGEX, title="Digital Object Identifier")
    sid: str = Field(None, regex=SID_REGEX, title="Secondary Identifier")
    collection_id: str
    schema_id: str
    metadata: dict[str, Any]

    @validator('sid', always=True)
    def validate_sid(cls, sid, values):
        try:
            if not values['doi'] and not sid:
                raise ValueError("Secondary ID is mandatory if a DOI is not provided")
        except KeyError:
            pass  # ignore: doi validation already failed

        if sid and re.match(DOI_REGEX, sid):
            raise ValueError("The secondary ID cannot be a DOI")

        return sid

    @validator('schema_id')
    def validate_schema_id(cls, schema_id):
        if schema_id not in (ODPMetadataSchema.SAEON_DATACITE4, ODPMetadataSchema.SAEON_ISO19115, ODPMetadataSchema.SAEON_EML):
            raise ValueError("SAEON metadata schema required")

        return schema_id

    @root_validator
    def set_metadata_doi(cls, values):
        """Copy the DOI into the metadata post-validation."""
        try:
            if doi := values['doi']:
                values['metadata']['doi'] = doi
            else:
                values['metadata'].pop('doi', None)
        except KeyError:
            pass  # ignore: doi and/or metadata field validation already failed

        return values
