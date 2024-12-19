from enum import Enum
from functools import cached_property
from typing import Optional


class ODPScope(str, Enum):
    ARCHIVE_READ = 'odp.archive:read'
    ARCHIVE_SAEON_REPOSITORY = 'odp.archive:saeon_repository'
    ARCHIVE_SAEON_OBSERVATIONS = 'odp.archive:saeon_observations'
    ARCHIVE_MIMS = 'odp.archive:mims'
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
    KEYWORD_ADMIN = 'odp.keyword:admin'
    KEYWORD_READ_ALL = 'odp.keyword:read_all'
    KEYWORD_READ = 'odp.keyword:read'
    KEYWORD_SUGGEST = 'odp.keyword:suggest'
    PACKAGE_ADMIN = 'odp.package:admin'
    PACKAGE_READ_ALL = 'odp.package:read_all'
    PACKAGE_READ = 'odp.package:read'
    PACKAGE_WRITE = 'odp.package:write'
    PACKAGE_DOI = 'odp.package:doi'
    PACKAGE_SDG = 'odp.package:sdg'
    PROVIDER_ADMIN = 'odp.provider:admin'
    PROVIDER_READ_ALL = 'odp.provider:read_all'
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
    RESOURCE_ADMIN = 'odp.resource:admin'
    RESOURCE_READ_ALL = 'odp.resource:read_all'
    RESOURCE_READ = 'odp.resource:read'
    RESOURCE_WRITE = 'odp.resource:write'
    ROLE_ADMIN = 'odp.role:admin'
    ROLE_READ = 'odp.role:read'
    SCHEMA_READ = 'odp.schema:read'
    SCOPE_READ = 'odp.scope:read'
    TAG_READ = 'odp.tag:read'
    TOKEN_READ = 'odp.token:read'
    USER_ADMIN = 'odp.user:admin'
    USER_READ = 'odp.user:read'
    VOCABULARY_READ = 'odp.vocabulary:read'

    @cached_property
    def constrainable_by(self) -> Optional[str]:
        """A scope's usage (via a client or role) may be constrained to a particular
        object or subset of objects rather than applying to all relevant objects.

        For example, record scopes may be constrained to apply only to records belonging
        to a specific subset of collections, rather than to all records.

        This property indicates the entity type of any such constraining subset.
        """
        if (
                self.value.startswith('odp.collection:') or
                self.value.startswith('odp.record:')
        ):
            return 'collection'

        if (
                self.value.startswith('odp.provider:') or
                self.value.startswith('odp.package:') or
                self.value.startswith('odp.resource:')
        ) and not (
                self.value.endswith(':admin') or
                self.value.endswith(':read_all')
        ):
            return 'provider'
