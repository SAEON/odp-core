from pydantic import AnyHttpUrl

from odp.config import BaseConfig


class ORCIDConfig(BaseConfig):
    class Config:
        env_prefix = 'ORCID_'

    BASE_URL: AnyHttpUrl
    CLIENT_ID: str
    CLIENT_SECRET: str
