"""
Pydantic models for PDF generation API endpoints.

These models provide request/response validation for PDF generation endpoints,
supporting both DataCite and ISO19115 metadata formats.
"""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class PDFGenerationRequest(BaseModel):
    """Request model for PDF generation endpoint.

    This model accepts metadata in either DataCite4 or ISO19115 format
    and validates the structure before passing to the PDF generator.

    Attributes:
        metadata_format: Schema format identifier.
            - "auto": Auto-detect schema (default)
            - "datacite4": DataCite4 format
            - "iso19115": ISO19115 format
        metadata: Metadata dictionary (DataCite4 or ISO19115 structure)
        keywords: Optional list of keywords
        temporal_start: Optional ISO 8601 start date
        temporal_end: Optional ISO 8601 end date
    """

    metadata_format: str = Field(
        default="auto",
        description="Schema format: auto, datacite4, iso19115",
        examples=["auto", "datacite4", "iso19115"],
    )
    metadata: Dict[str, Any] = Field(
        ...,
        description="Metadata dict (DataCite4 or ISO19115 structure)",
        examples=[
            {
                "titles": [{"title": "Example Dataset"}],
                "doi": "10.15493/example",
                "publisher": "SAEON",
                "publicationYear": 2024,
            }
        ],
    )
    keywords: Optional[List[str]] = Field(
        default=None,
        description="Keywords associated with the record",
        examples=[["ocean", "climate", "data"]],
    )
    temporal_start: Optional[str] = Field(
        default=None,
        description="Temporal extent start date (ISO 8601 format)",
        examples=["2020-01-01T00:00:00Z"],
    )
    temporal_end: Optional[str] = Field(
        default=None,
        description="Temporal extent end date (ISO 8601 format)",
        examples=["2023-12-31T23:59:59Z"],
    )

    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "examples": [
                {
                    "metadata_format": "datacite4",
                    "metadata": {
                        "titles": [{"title": "Marine Dataset"}],
                        "doi": "10.15493/marine",
                        "publisher": "SAEON",
                        "publicationYear": 2024,
                        "creators": [
                            {
                                "name": "Dr. John Smith",
                                "affiliation": [
                                    {"affiliation": "University, email: john@example.com"}
                                ],
                            }
                        ],
                        "descriptions": [
                            {
                                "description": "Dataset description",
                                "descriptionType": "Abstract",
                            }
                        ],
                    },
                    "keywords": ["ocean", "data"],
                    "temporal_start": "2020-01-01T00:00:00Z",
                    "temporal_end": "2023-12-31T23:59:59Z",
                }
            ]
        }


class PDFBinaryResponse:
    """Response model for PDF endpoints.

    Note: This is not a Pydantic model, as the response is binary PDF data.
    The response is handled directly as application/pdf content type.
    """

    pass


class PDFGenerationErrorResponse(BaseModel):
    """Error response model for PDF generation failures.

    Attributes:
        error: Error message
        detail: Detailed error information
        status_code: HTTP status code
    """

    error: str = Field(
        ...,
        description="Error message",
        examples=["PDF generation failed", "Invalid metadata schema"],
    )
    detail: Optional[str] = Field(
        default=None,
        description="Detailed error information",
        examples=["Could not detect metadata schema"],
    )
    status_code: int = Field(
        ...,
        description="HTTP status code",
        examples=[400, 422, 500],
    )

    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "examples": [
                {
                    "error": "Invalid metadata schema",
                    "detail": "Could not detect metadata schema. Ensure metadata matches DataCite4 or ISO19115 format.",
                    "status_code": 422,
                },
                {
                    "error": "PDF generation failed",
                    "detail": "ReportLab error: invalid PDF structure",
                    "status_code": 500,
                },
            ]
        }


class MetadataFormatRequest(BaseModel):
    """Alternative request model for MIMS compatibility.

    This model wraps metadata in an array format for backward compatibility
    with existing MIMS UI endpoints.

    Attributes:
        metadata: Metadata dict (DataCite4 or ISO19115 structure)
        keywords: Optional list of keywords
        temporal_start: Optional ISO 8601 start date
        temporal_end: Optional ISO 8601 end date
    """

    metadata: Dict[str, Any] = Field(
        ...,
        description="Metadata dict (DataCite4 or ISO19115 structure)",
    )
    keywords: Optional[List[str]] = Field(
        default=None,
        description="Keywords associated with the record",
    )
    temporal_start: Optional[str] = Field(
        default=None,
        description="Temporal extent start date (ISO 8601 format)",
    )
    temporal_end: Optional[str] = Field(
        default=None,
        description="Temporal extent end date (ISO 8601 format)",
    )
