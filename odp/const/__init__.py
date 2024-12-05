from enum import Enum

from odp.const.scope import ODPScope

# SAEON's DOI prefix
DOI_PREFIX = 10.15493

# object IDs
ID_REGEX = r'^\w[-.\w]*\w$'

# adapted from https://www.crossref.org/blog/dois-and-matching-regular-expressions
DOI_REGEX = r'^10\.\d{4,}(\.\d+)*/[-._;()/:a-zA-Z0-9]+$'

# the suffix part of the DOI regex suffices for secondary IDs
SID_REGEX = r'^[-._;()/:a-zA-Z0-9]+$'

# an ROR ID, from https://ror.readme.io/docs/identifier
ROR_REGEX = r'^https://ror\.org/0[a-hj-km-np-tv-z|0-9]{6}[0-9]{2}$'

SAEON_EMAIL_DOMAINS = ['saeon.ac.za', 'saeon.nrf.ac.za']


class ODPSystemRole(str, Enum):
    ODP_ADMIN = 'ODP.Admin'
    SAEON_STAFF = 'SAEON.Staff'
    DEFAULT = 'Default'


class ODPPackageTag(str, Enum):
    DOI = 'Package.DOI'
    CONTRIBUTOR = 'Package.Contributor'
    GEOLOCATION = 'Package.GeoLocation'
    DATERANGE = 'Package.DateRange'
    DATERANGEINC = 'Package.DateRangeInc'
    SDG = 'Package.SDG'


class ODPCollectionTag(str, Enum):
    PUBLISHED = 'Collection.Published'
    FROZEN = 'Collection.Frozen'
    INFRASTRUCTURE = 'Collection.Infrastructure'
    PROJECT = 'Collection.Project'
    NOTSEARCHABLE = 'Collection.NotSearchable'
    HARVESTED = 'Collection.Harvested'


class ODPRecordTag(str, Enum):
    QC = 'Record.QC'
    EMBARGO = 'Record.Embargo'
    MIGRATED = 'Record.Migrated'
    NOTSEARCHABLE = 'Record.NotSearchable'
    RETRACTED = 'Record.Retracted'
    NOTE = 'Record.Note'
    SDG = 'Record.SDG'


class ODPMetadataSchema(str, Enum):
    SAEON_DATACITE4 = 'SAEON.DataCite4'
    SAEON_ISO19115 = 'SAEON.ISO19115'
    DATACITE_4_3 = 'DataCite.4.3'
    SCHEMAORG_DATASET = 'SchemaOrg.Dataset'
    RIS_CITATION = 'RIS.Citation'


class ODPTagSchema(str, Enum):
    DOI = 'Tag.DOI'
    GENERIC = 'Tag.Generic'
    KEYWORD = 'Tag.Keyword'
    CONTRIBUTOR = 'Tag.Contributor'
    GEOLOCATION = 'Tag.GeoLocation'
    DATERANGE = 'Tag.DateRange'
    DATERANGEINC = 'Tag.DateRangeInc'
    COLLECTION_INFRASTRUCTURE = 'Tag.Collection.Infrastructure'
    COLLECTION_PROJECT = 'Tag.Collection.Project'
    RECORD_QC = 'Tag.Record.QC'
    RECORD_EMBARGO = 'Tag.Record.Embargo'
    RECORD_MIGRATED = 'Tag.Record.Migrated'


class ODPCatalog(str, Enum):
    SAEON = 'SAEON'
    DATACITE = 'DataCite'
    MIMS = 'MIMS'


class ODPKeyword(str, Enum):
    INSTITUTION = 'Institution'


class ODPKeywordSchema(str, Enum):
    INSTITUTION = 'Keyword.Institution'


class ODPVocabulary(str, Enum):
    INFRASTRUCTURE = 'Infrastructure'
    PROJECT = 'Project'
    SDG = 'SDG'


class ODPVocabularySchema(str, Enum):
    INFRASTRUCTURE = 'Vocabulary.Infrastructure'
    PROJECT = 'Vocabulary.Project'
    SDG = 'Vocabulary.SDG'


class ODPDateRangeIncType(str, Enum):
    CURRENT_DATE = 'current_date'
    TOMORROW = 'tomorrow'
