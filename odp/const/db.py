from enum import Enum


class DBEnum(str, Enum):
    def __repr__(self):
        return repr(self.value)


class ArchiveType(DBEnum):
    filestore = 'filestore'
    website = 'website'


class KeywordStatus(DBEnum):
    proposed = 'proposed'
    approved = 'approved'
    rejected = 'rejected'
    obsolete = 'obsolete'


class PackageStatus(DBEnum):
    editing = 'editing'
    submitted = 'submitted'
    in_review = 'in_review'
    archived = 'archived'
    delete_pending = 'delete_pending'


class ResourceStatus(DBEnum):
    active = 'active'
    delete_pending = 'delete_pending'


class ArchiveResourceStatus(DBEnum):
    pending = 'pending'
    valid = 'valid'
    missing = 'missing'
    corrupt = 'corrupt'


class HashAlgorithm(DBEnum):
    md5 = 'md5'
    sha256 = 'sha256'


class SchemaType(DBEnum):
    metadata = 'metadata'
    tag = 'tag'
    keyword = 'keyword'
    vocabulary = 'vocabulary'  # deprecated


class ScopeType(DBEnum):
    odp = 'odp'
    oauth = 'oauth'
    client = 'client'


class TagType(DBEnum):
    package = 'package'
    collection = 'collection'
    record = 'record'


class TagCardinality(DBEnum):
    one = 'one'  # one tag instance per object
    user = 'user'  # one tag instance per user per object
    multi = 'multi'  # multiple tag instances per user per object


class AuditCommand(DBEnum):
    insert = 'insert'
    update = 'update'
    delete = 'delete'


class PackageCommand(DBEnum):
    insert = 'insert'
    update = 'update'
    delete = 'delete'
    submit = 'submit'
    cancel = 'cancel'


class IdentityCommand(DBEnum):
    # operations performed by the user
    signup = 'signup'
    login = 'login'
    verify_email = 'verify_email'
    change_password = 'change_password'
    # operations performed by an admin/system
    create = 'create'
    edit = 'edit'
    delete = 'delete'
