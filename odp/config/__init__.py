from odp.config.base import BaseConfig
from odp.config.datacite import DataciteConfig
from odp.config.google import GoogleConfig
from odp.config.hydra import HydraConfig
from odp.config.odp import ODPConfig
from odp.config.orcid import ORCIDConfig
from odp.config.nextcloud import NEXTCloudConfig
from odp.config.redis import RedisConfig


class Config(BaseConfig):
    """ root configuration """

    _subconfig = {
        'ODP': ODPConfig,
        'HYDRA': HydraConfig,
        'DATACITE': DataciteConfig,
        'REDIS': RedisConfig,
        'GOOGLE': GoogleConfig,
        'ORCID': ORCIDConfig,
        'NEXTCLOUD': NEXTCloudConfig,
    }


config: Config = Config()
