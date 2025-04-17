from enum import Enum

# SAEON's DOI prefix
DOI_PREFIX = 10.15493

# object IDs
ID_REGEX = r'^\w[-.\w]*\w$'

# adapted from https://www.crossref.org/blog/dois-and-matching-regular-expressions
DOI_REGEX = r'^10\.\d{4,}(\.\d+)*/[-._;()/:a-zA-Z0-9]+$'

# the suffix part of the DOI regex suffices for secondary IDs
SID_REGEX = r'^[-._;()/:a-zA-Z0-9]+$'

SAEON_EMAIL_DOMAINS = ['saeon.ac.za', 'saeon.nrf.ac.za']


class ODPScope(str, Enum):
    CATALOG_READ = 'odp.catalog:read'
    CATALOG_SEARCH = 'odp.catalog:search'
    CLIENT_ADMIN = 'odp.client:admin'
    CLIENT_READ = 'odp.client:read'
    COLLECTION_ADMIN = 'odp.collection:admin'
    COLLECTION_READ = 'odp.collection:read'
    COLLECTION_PUBLISH = 'odp.collection:publish'
    COLLECTION_FREEZE = 'odp.collection:freeze'
    COLLECTION_INFRASTRUCTURE = 'odp.collection:infrastructure'
    COLLECTION_PROJECT = 'odp.collection:project'
    COLLECTION_NOSEARCH = 'odp.collection:nosearch'
    COLLECTION_HARVESTED = 'odp.collection:harvested'
    PROVIDER_ADMIN = 'odp.provider:admin'
    PROVIDER_READ = 'odp.provider:read'
    RECORD_ADMIN = 'odp.record:admin'
    RECORD_READ = 'odp.record:read'
    RECORD_WRITE = 'odp.record:write'
    RECORD_QC = 'odp.record:qc'
    RECORD_EMBARGO = 'odp.record:embargo'
    RECORD_MIGRATE = 'odp.record:migrate'
    RECORD_NOSEARCH = 'odp.record:nosearch'
    RECORD_RETRACT = 'odp.record:retract'
    RECORD_NOTE = 'odp.record:note'
    RECORD_SDG = 'odp.record:sdg'
    ROLE_ADMIN = 'odp.role:admin'
    ROLE_READ = 'odp.role:read'
    SCHEMA_READ = 'odp.schema:read'
    SCOPE_READ = 'odp.scope:read'
    TAG_READ = 'odp.tag:read'
    TOKEN_READ = 'odp.token:read'
    USER_ADMIN = 'odp.user:admin'
    USER_READ = 'odp.user:read'
    VOCABULARY_INFRASTRUCTURE = 'odp.vocabulary:infrastructure'
    VOCABULARY_PROJECT = 'odp.vocabulary:project'
    VOCABULARY_SDG = 'odp.vocabulary:sdg'
    VOCABULARY_READ = 'odp.vocabulary:read'


class ODPSystemRole(str, Enum):
    ODP_ADMIN = 'ODP.Admin'
    SAEON_STAFF = 'SAEON.Staff'
    DEFAULT = 'Default'


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
    SAEON_EML = 'SAEON.EML'


class ODPTagSchema(str, Enum):
    GENERIC = 'Tag.Generic'
    KEYWORD = 'Tag.Keyword'
    COLLECTION_INFRASTRUCTURE = 'Tag.Collection.Infrastructure'
    COLLECTION_PROJECT = 'Tag.Collection.Project'
    RECORD_QC = 'Tag.Record.QC'
    RECORD_EMBARGO = 'Tag.Record.Embargo'
    RECORD_MIGRATED = 'Tag.Record.Migrated'


class ODPCatalog(str, Enum):
    SAEON = 'SAEON'
    DATACITE = 'DataCite'
    MIMS = 'MIMS'


class ODPVocabulary(str, Enum):
    INFRASTRUCTURE = 'Infrastructure'
    PROJECT = 'Project'
    SDG = 'SDG'


class ODPVocabularySchema(str, Enum):
    INFRASTRUCTURE = 'Vocabulary.Infrastructure'
    PROJECT = 'Vocabulary.Project'
    SDG = 'Vocabulary.SDG'
