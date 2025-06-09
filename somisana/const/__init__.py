from enum import Enum


class SOMISANAScope(str, Enum):
    """Auth Scopes."""
    PRODUCT_ADMIN = 'somisana.product:admin'
    RESOURCE_ADMIN = 'somisana.resource:admin'
    RESOURCE_READ = 'somisana.resource:read'
    DATASET_ADMIN = 'somisana.dataset:admin'
    DATASET_READ = 'somisana.dataset:read'
    PRODUCT_READ = 'somisana.product:read'


class ResourceType(str, Enum):
    """Resource type."""
    DOCUMENT = 'document'
    COVER_IMAGE = 'cover_image'
    THUMBNAIL = 'thumbnail'
    DATA_ACCESS_URL = 'data_access_url'


class ResourceReferenceType(str, Enum):
    """Resource reference type."""
    LINK = 'link'
    PATH = 'path'


class EntityType(str, Enum):
    """Somisana entity type"""
    PRODUCT = 'product'
    DATASET = 'dataset'
