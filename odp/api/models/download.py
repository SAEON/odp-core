from pydantic import BaseModel, EmailStr
from typing import List, Optional

class DownloadAuditModel(BaseModel):
    id: int
    timestamp: str
    name: Optional[str]
    email: Optional[EmailStr]
    organisation: Optional[str]
    download_type: Optional[str]
    success: bool
    ip_address: Optional[str]
    doi: Optional[str]
    record_ids: List[str] = []

class OrganisationStats(BaseModel):
    name: str
    downloads: int

class TopRecordStats(BaseModel):
    doi: Optional[str]
    record_id: Optional[str]
    downloads: int
    unique_users: int

class DailyDownloadStats(BaseModel):
    date: Optional[str]
    downloads: int
    successful: int
    failed: int

class DownloadStatsModel(BaseModel):
    total_downloads: int
    unique_users: int
    total_data_volume: int
    successful_downloads: int
    failed_downloads: int
    downloads_by_type: dict[str, int]
    organisations: List[OrganisationStats]
    top_records: List[TopRecordStats]
    daily_downloads: List[DailyDownloadStats]