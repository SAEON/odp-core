from pydantic import AnyHttpUrl

from odp.config import BaseConfig


class NEXTCloudConfig(BaseConfig):
    class Config:
        env_prefix = 'NEXTCLOUD_'

    URL: AnyHttpUrl
    USER: str
    PASSWORD: str
