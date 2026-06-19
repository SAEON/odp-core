from typing import Any, List, Optional

from pydantic import BaseModel, EmailStr, Field


class UserData(BaseModel):
    name: str = Field(..., description="Full name of the user", min_length=1)
    email: str = Field(..., description="Email address of the user", min_length=1)
    organisation: str = Field(..., description="Organization or institution name", min_length=1)


class DownloadAuditCreateModel(BaseModel):
    client_id: str = Field(default='unknown')
    user_id: Optional[str] = None
    download_url: Optional[str] = None
    file_size: Optional[int] = None
    success: bool = True
    download_type: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    organisation: Optional[str] = None
    doi: Optional[str] = None
    record_id: Optional[str] = None
    record_ids: Optional[List[str]] = None
    catalog_url: Optional[str] = None


class DownloadAuditResponse(BaseModel):
    status: str = Field(..., description="Result of the audit log operation")
    audit_id: int = Field(..., description="ID of the created audit record")


class DownloadAuditModel(BaseModel):
    id: int = Field(..., description="Audit record ID")
    timestamp: str = Field(..., description="ISO 8601 timestamp of the download")
    name: Optional[str] = Field(default=None, description="Name of the user who downloaded")
    email: Optional[EmailStr] = Field(default=None, description="Email of the user who downloaded")
    organisation: Optional[str] = Field(default=None, description="Organisation of the user")
    download_type: Optional[str] = Field(default=None, description="Type of download: single_record or zip_bundle")
    success: bool = Field(..., description="Whether the download succeeded")
    ip_address: Optional[str] = Field(default=None, description="IP address of the requester")
    doi: Optional[str] = Field(default=None, description="DOI of the downloaded record (single_record type)")
    record_ids: list[str] = Field(default=[], description="List of record IDs included in the download")


class OrganisationStats(BaseModel):
    name: str = Field(..., description="Organisation name")
    downloads: int = Field(..., description="Total downloads by this organisation")
    unique_users: int = Field(..., description="Number of unique users from this organisation")


class TopRecordStats(BaseModel):
    doi: Optional[str] = Field(default=None, description="DOI of the record")
    record_id: Optional[str] = Field(default=None, description="Record ID")
    downloads: int = Field(..., description="Total download count for this record")
    unique_users: int = Field(..., description="Number of unique users who downloaded this record")


class DailyDownloadStats(BaseModel):
    date: Optional[str] = Field(default=None, description="Date (YYYY-MM-DD)")
    downloads: int = Field(..., description="Total downloads on this date")
    successful: int = Field(..., description="Successful downloads on this date")
    failed: int = Field(..., description="Failed downloads on this date")


class BundledRecordDataset(BaseModel):
    zip_path: str = Field(..., description="Path or filename of the generated ZIP")
    total_size: int = Field(..., description="Total size of the ZIP in bytes")
    record_count: int = Field(..., description="Number of records successfully included")
    failed_count: int = Field(..., description="Number of records that failed to include")
    processed: list[str] = Field(..., description="List of successfully processed record IDs")
    failed: list[dict[str, Any]] = Field(..., description="List of failed records with error details")


class DownloadStatsModel(BaseModel):
    total_downloads: int = Field(..., description="Total number of download events")
    unique_users: int = Field(..., description="Number of unique users (by email)")
    total_data_volume: int = Field(..., description="Total data volume downloaded in bytes")
    successful_downloads: int = Field(..., description="Number of successful downloads")
    failed_downloads: int = Field(..., description="Number of failed downloads")
    downloads_by_type: dict[str, int] = Field(..., description="Download counts grouped by type")
    organisations: list[OrganisationStats] = Field(..., description="Per-organisation download stats")
    top_records: list[TopRecordStats] = Field(..., description="Most downloaded records")
    daily_downloads: list[DailyDownloadStats] = Field(..., description="Daily download breakdown")
