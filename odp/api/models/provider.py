from pydantic import BaseModel, Field

from odp.const import ID_REGEX


class ProviderModel(BaseModel):
    id: str
    key: str
    name: str
    package_count: int
    collection_keys: dict[str, str] = Field(..., title='Collection id:key pairs')
    timestamp: str


class ProviderDetailModel(ProviderModel):
    client_ids: list[str]
    user_ids: list[str]
    user_names: dict[str, str] = Field(..., title='User id:name pairs')


class ProviderModelIn(BaseModel):
    key: str = Field(..., regex=ID_REGEX)
    name: str
    user_ids: list[str]
