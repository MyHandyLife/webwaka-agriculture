"""
WebWaka Agriculture Shared Models

Base models and mixins with African optimizations for all agricultural modules.
Includes offline synchronization, multi-language support, and cultural adaptations.
"""

import uuid
from datetime import datetime
from typing import Optional, Dict, Any, List
from sqlalchemy import Column, String, DateTime, Boolean, Text, JSON, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_mixin
from geoalchemy2 import Geometry

from app.core.database import Base


@declarative_mixin
class TimestampMixin:
    """Mixin for timestamp fields with African timezone support."""
    
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="Creation timestamp in UTC"
    )
    
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
        index=True,
        comment="Last update timestamp in UTC"
    )


@declarative_mixin
class SoftDeleteMixin:
    """Mixin for soft delete functionality."""
    
    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False,
        index=True,
        comment="Soft delete flag"
    )
    
    deleted_at = Column(
        DateTime,
        nullable=True,
        comment="Deletion timestamp"
    )


@declarative_mixin
class AfricanOptimizationMixin:
    """Mixin for African-specific optimizations."""
    
    # Offline synchronization
    sync_status = Column(
        String(20),
        default="synced",
        nullable=False,
        comment="Synchronization status: synced, pending, conflict"
    )
    
    last_sync_at = Column(
        DateTime,
        nullable=True,
        comment="Last synchronization timestamp"
    )
    
    offline_id = Column(
        String(50),
        nullable=True,
        comment="Offline unique identifier for sync resolution"
    )
    
    # Multi-language support
    language_code = Column(
        String(5),
        default="en",
        nullable=False,
        comment="Language code (ISO 639-1)"
    )
    
    # Cultural context
    cultural_context = Column(
        JSON,
        nullable=True,
        comment="Cultural context and traditional practices"
    )
    
    # Mobile optimization
    mobile_optimized = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Mobile optimization flag"
    )
    
    # Data sovereignty
    data_residency_country = Column(
        String(2),
        nullable=True,
        comment="Country code for data residency (ISO 3166-1 alpha-2)"
    )


@declarative_mixin
class GeospatialMixin:
    """Mixin for geospatial data with African coordinate systems."""
    
    # Location data
    latitude = Column(
        Float,
        nullable=True,
        comment="Latitude in decimal degrees"
    )
    
    longitude = Column(
        Float,
        nullable=True,
        comment="Longitude in decimal degrees"
    )
    
    # PostGIS geometry field
    geometry = Column(
        Geometry('POINT', srid=4326),
        nullable=True,
        comment="PostGIS geometry field"
    )
    
    # Location accuracy
    location_accuracy = Column(
        Float,
        nullable=True,
        comment="Location accuracy in meters"
    )
    
    # Administrative boundaries
    country_code = Column(
        String(2),
        nullable=True,
        comment="Country code (ISO 3166-1 alpha-2)"
    )
    
    region = Column(
        String(100),
        nullable=True,
        comment="Administrative region/state"
    )
    
    district = Column(
        String(100),
        nullable=True,
        comment="Administrative district"
    )
    
    village = Column(
        String(100),
        nullable=True,
        comment="Village or local area"
    )


@declarative_mixin
class MultiLanguageMixin:
    """Mixin for multi-language content support."""
    
    # Multi-language content storage
    content_translations = Column(
        JSON,
        nullable=True,
        comment="Content translations in multiple languages"
    )
    
    @declared_attr
    def get_translated_content(cls, field_name: str, language_code: str = "en") -> str:
        """Get translated content for specific field and language."""
        if cls.content_translations and field_name in cls.content_translations:
            translations = cls.content_translations[field_name]
            return translations.get(language_code, translations.get("en", ""))
        return ""
    
    @declared_attr
    def set_translated_content(cls, field_name: str, content: str, language_code: str = "en"):
        """Set translated content for specific field and language."""
        if not cls.content_translations:
            cls.content_translations = {}
        
        if field_name not in cls.content_translations:
            cls.content_translations[field_name] = {}
        
        cls.content_translations[field_name][language_code] = content


class BaseModel(Base, TimestampMixin, SoftDeleteMixin, AfricanOptimizationMixin):
    """Base model with all common functionality."""
    
    __abstract__ = True
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Primary key UUID"
    )
    
    # Metadata for African context
    metadata_info = Column(
        JSON,
        nullable=True,
        comment="Additional metadata for African context"
    )
    
    def to_dict(self, include_relationships: bool = False) -> Dict[str, Any]:
        """Convert model to dictionary with African optimizations."""
        result = {}
        
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            
            # Handle UUID serialization
            if isinstance(value, uuid.UUID):
                value = str(value)
            
            # Handle datetime serialization
            elif isinstance(value, datetime):
                value = value.isoformat()
            
            result[column.name] = value
        
        # Add African context
        result["african_context"] = {
            "country_code": getattr(self, "country_code", None),
            "region": getattr(self, "region", None),
            "language_code": self.language_code,
            "cultural_context": self.cultural_context
        }
        
        return result
    
    def get_sync_data(self) -> Dict[str, Any]:
        """Get data for offline synchronization."""
        return {
            "id": str(self.id),
            "sync_status": self.sync_status,
            "last_sync_at": self.last_sync_at.isoformat() if self.last_sync_at else None,
            "offline_id": self.offline_id,
            "data": self.to_dict()
        }
    
    def mark_for_sync(self):
        """Mark record for synchronization."""
        self.sync_status = "pending"
        self.updated_at = datetime.utcnow()
    
    def mark_synced(self):
        """Mark record as synchronized."""
        self.sync_status = "synced"
        self.last_sync_at = datetime.utcnow()
    
    def mark_conflict(self):
        """Mark record as having sync conflict."""
        self.sync_status = "conflict"


class AfricanReferenceData(BaseModel):
    """Reference data for African agricultural context."""
    
    __tablename__ = "african_reference_data"
    
    # Reference type (crops, varieties, practices, etc.)
    reference_type = Column(
        String(50),
        nullable=False,
        index=True,
        comment="Type of reference data"
    )
    
    # Reference code (unique within type)
    reference_code = Column(
        String(50),
        nullable=False,
        index=True,
        comment="Unique code within reference type"
    )
    
    # Multi-language names
    names = Column(
        JSON,
        nullable=False,
        comment="Names in multiple languages"
    )
    
    # Descriptions
    descriptions = Column(
        JSON,
        nullable=True,
        comment="Descriptions in multiple languages"
    )
    
    # African-specific attributes
    african_attributes = Column(
        JSON,
        nullable=True,
        comment="African-specific attributes and characteristics"
    )
    
    # Regional applicability
    applicable_regions = Column(
        JSON,
        nullable=True,
        comment="List of African regions where this applies"
    )
    
    # Seasonal information
    seasonal_data = Column(
        JSON,
        nullable=True,
        comment="Seasonal information for African climates"
    )
    
    # Traditional knowledge
    traditional_knowledge = Column(
        JSON,
        nullable=True,
        comment="Traditional knowledge and practices"
    )
    
    # Active status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Active status flag"
    )


class CommunityKnowledge(BaseModel):
    """Community knowledge and traditional practices."""
    
    __tablename__ = "community_knowledge"
    
    # Knowledge title
    title = Column(
        String(200),
        nullable=False,
        comment="Knowledge title"
    )
    
    # Knowledge content
    content = Column(
        Text,
        nullable=False,
        comment="Knowledge content"
    )
    
    # Knowledge category
    category = Column(
        String(50),
        nullable=False,
        index=True,
        comment="Knowledge category"
    )
    
    # Source community
    source_community = Column(
        String(100),
        nullable=True,
        comment="Source community or ethnic group"
    )
    
    # Verification status
    verification_status = Column(
        String(20),
        default="pending",
        nullable=False,
        comment="Verification status by experts"
    )
    
    # Effectiveness rating
    effectiveness_rating = Column(
        Float,
        nullable=True,
        comment="Community effectiveness rating (1-5)"
    )
    
    # Usage count
    usage_count = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Number of times this knowledge was accessed"
    )


class SyncLog(BaseModel):
    """Synchronization log for offline operations."""
    
    __tablename__ = "sync_logs"
    
    # User who performed sync
    user_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
        comment="User who performed synchronization"
    )
    
    # Sync operation type
    operation_type = Column(
        String(20),
        nullable=False,
        comment="Type of sync operation: upload, download, conflict_resolution"
    )
    
    # Sync status
    status = Column(
        String(20),
        nullable=False,
        comment="Sync status: success, failed, partial"
    )
    
    # Records affected
    records_affected = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Number of records affected"
    )
    
    # Conflicts encountered
    conflicts_count = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Number of conflicts encountered"
    )
    
    # Sync details
    sync_details = Column(
        JSON,
        nullable=True,
        comment="Detailed sync information"
    )
    
    # Error information
    error_info = Column(
        JSON,
        nullable=True,
        comment="Error information if sync failed"
    )
    
    # Sync duration
    duration_seconds = Column(
        Float,
        nullable=True,
        comment="Sync duration in seconds"
    )


# Export all shared models and mixins
__all__ = [
    "BaseModel",
    "TimestampMixin",
    "SoftDeleteMixin", 
    "AfricanOptimizationMixin",
    "GeospatialMixin",
    "MultiLanguageMixin",
    "AfricanReferenceData",
    "CommunityKnowledge",
    "SyncLog"
]

