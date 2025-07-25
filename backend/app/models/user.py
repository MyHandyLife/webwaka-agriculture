"""
WebWaka Agriculture User Management Models

User Management Tissue - 8 Modules:
1. User Registration & Authentication
2. Profile Management  
3. Role-Based Access Control
4. Community Integration
5. Farmer Verification
6. Extension Agent Management
7. Cooperative Management
8. Government Official Access

African optimizations: Multi-language support, cultural integration,
mobile-first design, and community-based authentication.
"""

import uuid
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from sqlalchemy import (
    Column, String, Boolean, DateTime, Date, Text, JSON, Integer, 
    Float, ForeignKey, Table, UniqueConstraint, Index
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from passlib.context import CryptContext

from app.models.shared import BaseModel, GeospatialMixin, MultiLanguageMixin
from app.core.database import Base

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Association tables for many-to-many relationships
user_roles = Table(
    'user_roles',
    Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
    Column('role_id', UUID(as_uuid=True), ForeignKey('user_roles_table.id'), primary_key=True),
    Column('assigned_at', DateTime, default=datetime.utcnow),
    Column('assigned_by', UUID(as_uuid=True), ForeignKey('users.id')),
    comment="User role assignments"
)

user_communities = Table(
    'user_communities',
    Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
    Column('community_id', UUID(as_uuid=True), ForeignKey('communities.id'), primary_key=True),
    Column('joined_at', DateTime, default=datetime.utcnow),
    Column('membership_type', String(20), default='member'),
    Column('is_active', Boolean, default=True),
    comment="User community memberships"
)

user_cooperatives = Table(
    'user_cooperatives',
    Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
    Column('cooperative_id', UUID(as_uuid=True), ForeignKey('cooperatives.id'), primary_key=True),
    Column('joined_at', DateTime, default=datetime.utcnow),
    Column('membership_number', String(50)),
    Column('membership_status', String(20), default='active'),
    Column('shares_owned', Integer, default=0),
    comment="User cooperative memberships"
)


class User(BaseModel, GeospatialMixin):
    """
    Module 1: User Registration & Authentication
    
    Core user model with African optimizations including mobile-first authentication,
    multi-language support, and cultural context integration.
    """
    
    __tablename__ = "users"
    
    # Basic user information
    username = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
        comment="Unique username"
    )
    
    email = Column(
        String(255),
        unique=True,
        nullable=True,  # Optional for rural users
        index=True,
        comment="Email address (optional for rural users)"
    )
    
    phone_number = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
        comment="Phone number (primary identifier for African users)"
    )
    
    # Password and authentication
    hashed_password = Column(
        String(255),
        nullable=False,
        comment="Hashed password"
    )
    
    # Personal information
    first_name = Column(
        String(100),
        nullable=False,
        comment="First name"
    )
    
    last_name = Column(
        String(100),
        nullable=False,
        comment="Last name"
    )
    
    middle_name = Column(
        String(100),
        nullable=True,
        comment="Middle name"
    )
    
    # African-specific names
    traditional_name = Column(
        String(100),
        nullable=True,
        comment="Traditional or local name"
    )
    
    # Demographics
    date_of_birth = Column(
        Date,
        nullable=True,
        comment="Date of birth"
    )
    
    gender = Column(
        String(10),
        nullable=True,
        comment="Gender"
    )
    
    # Contact information
    alternative_phone = Column(
        String(20),
        nullable=True,
        comment="Alternative phone number"
    )
    
    # Address information
    address_line1 = Column(
        String(255),
        nullable=True,
        comment="Address line 1"
    )
    
    address_line2 = Column(
        String(255),
        nullable=True,
        comment="Address line 2"
    )
    
    city = Column(
        String(100),
        nullable=True,
        comment="City"
    )
    
    state_province = Column(
        String(100),
        nullable=True,
        comment="State or province"
    )
    
    postal_code = Column(
        String(20),
        nullable=True,
        comment="Postal code"
    )
    
    # Account status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Account active status"
    )
    
    is_verified = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Account verification status"
    )
    
    email_verified = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Email verification status"
    )
    
    phone_verified = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Phone verification status"
    )
    
    # Authentication tracking
    last_login = Column(
        DateTime,
        nullable=True,
        comment="Last login timestamp"
    )
    
    login_count = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Total login count"
    )
    
    failed_login_attempts = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Failed login attempts"
    )
    
    account_locked_until = Column(
        DateTime,
        nullable=True,
        comment="Account lock expiration"
    )
    
    # African-specific fields
    ethnic_group = Column(
        String(100),
        nullable=True,
        comment="Ethnic group or tribe"
    )
    
    primary_language = Column(
        String(5),
        default="en",
        nullable=False,
        comment="Primary language code"
    )
    
    secondary_languages = Column(
        JSON,
        nullable=True,
        comment="List of secondary language codes"
    )
    
    # Education level
    education_level = Column(
        String(50),
        nullable=True,
        comment="Education level"
    )
    
    literacy_level = Column(
        String(20),
        nullable=True,
        comment="Literacy level: high, medium, low, none"
    )
    
    # Technology access
    device_type = Column(
        String(20),
        default="smartphone",
        nullable=False,
        comment="Primary device type: smartphone, feature_phone, tablet"
    )
    
    internet_access = Column(
        String(20),
        nullable=True,
        comment="Internet access type: wifi, mobile_data, none"
    )
    
    # Preferences
    preferred_communication = Column(
        String(20),
        default="sms",
        nullable=False,
        comment="Preferred communication method: sms, call, email, app"
    )
    
    timezone = Column(
        String(50),
        nullable=True,
        comment="User timezone"
    )
    
    # Profile completion
    profile_completion_percentage = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Profile completion percentage"
    )
    
    # Relationships
    roles = relationship(
        "UserRole",
        secondary=user_roles,
        back_populates="users",
        lazy="select"
    )
    
    communities = relationship(
        "Community",
        secondary=user_communities,
        back_populates="members",
        lazy="select"
    )
    
    cooperatives = relationship(
        "Cooperative",
        secondary=user_cooperatives,
        back_populates="members",
        lazy="select"
    )
    
    # Indexes for African optimization
    __table_args__ = (
        Index('idx_user_phone_country', 'phone_number', 'country_code'),
        Index('idx_user_location', 'country_code', 'region', 'district'),
        Index('idx_user_language', 'primary_language', 'language_code'),
        Index('idx_user_active_verified', 'is_active', 'is_verified'),
    )
    
    def set_password(self, password: str):
        """Set user password with hashing."""
        self.hashed_password = pwd_context.hash(password)
    
    def verify_password(self, password: str) -> bool:
        """Verify user password."""
        return pwd_context.verify(password, self.hashed_password)
    
    @hybrid_property
    def full_name(self) -> str:
        """Get user's full name."""
        names = [self.first_name]
        if self.middle_name:
            names.append(self.middle_name)
        names.append(self.last_name)
        return " ".join(names)
    
    @hybrid_property
    def display_name(self) -> str:
        """Get user's display name with traditional name if available."""
        if self.traditional_name:
            return f"{self.full_name} ({self.traditional_name})"
        return self.full_name
    
    @hybrid_property
    def age(self) -> Optional[int]:
        """Calculate user's age."""
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None
    
    def update_login_info(self):
        """Update login information."""
        self.last_login = datetime.utcnow()
        self.login_count += 1
        self.failed_login_attempts = 0
    
    def increment_failed_login(self):
        """Increment failed login attempts."""
        self.failed_login_attempts += 1
        if self.failed_login_attempts >= 5:
            # Lock account for 30 minutes
            self.account_locked_until = datetime.utcnow() + timedelta(minutes=30)
    
    def is_account_locked(self) -> bool:
        """Check if account is locked."""
        if self.account_locked_until:
            return datetime.utcnow() < self.account_locked_until
        return False


class UserProfile(BaseModel, MultiLanguageMixin):
    """
    Module 2: Profile Management
    
    Extended user profile with African cultural context and agricultural information.
    """
    
    __tablename__ = "user_profiles"
    
    # User reference
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
        unique=True,
        comment="User reference"
    )
    
    # Profile information
    bio = Column(
        Text,
        nullable=True,
        comment="User biography"
    )
    
    occupation = Column(
        String(100),
        nullable=True,
        comment="Primary occupation"
    )
    
    agricultural_role = Column(
        String(50),
        nullable=True,
        comment="Role in agriculture: farmer, trader, processor, advisor"
    )
    
    # Experience
    years_in_agriculture = Column(
        Integer,
        nullable=True,
        comment="Years of experience in agriculture"
    )
    
    farming_experience_level = Column(
        String(20),
        nullable=True,
        comment="Farming experience: beginner, intermediate, advanced, expert"
    )
    
    # Specializations
    crop_specializations = Column(
        JSON,
        nullable=True,
        comment="List of crop specializations"
    )
    
    livestock_specializations = Column(
        JSON,
        nullable=True,
        comment="List of livestock specializations"
    )
    
    # Skills and certifications
    skills = Column(
        JSON,
        nullable=True,
        comment="List of agricultural skills"
    )
    
    certifications = Column(
        JSON,
        nullable=True,
        comment="List of certifications and training"
    )
    
    # Social information
    marital_status = Column(
        String(20),
        nullable=True,
        comment="Marital status"
    )
    
    household_size = Column(
        Integer,
        nullable=True,
        comment="Number of people in household"
    )
    
    dependents = Column(
        Integer,
        nullable=True,
        comment="Number of dependents"
    )
    
    # Economic information
    income_level = Column(
        String(20),
        nullable=True,
        comment="Income level category"
    )
    
    land_ownership_status = Column(
        String(20),
        nullable=True,
        comment="Land ownership: owner, tenant, sharecropper, communal"
    )
    
    # Technology adoption
    technology_adoption_level = Column(
        String(20),
        nullable=True,
        comment="Technology adoption: low, medium, high"
    )
    
    mobile_money_usage = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Uses mobile money services"
    )
    
    # Preferences
    communication_preferences = Column(
        JSON,
        nullable=True,
        comment="Communication preferences and settings"
    )
    
    notification_settings = Column(
        JSON,
        nullable=True,
        comment="Notification preferences"
    )
    
    privacy_settings = Column(
        JSON,
        nullable=True,
        comment="Privacy settings"
    )
    
    # Profile media
    profile_picture_url = Column(
        String(500),
        nullable=True,
        comment="Profile picture URL"
    )
    
    cover_photo_url = Column(
        String(500),
        nullable=True,
        comment="Cover photo URL"
    )
    
    # Verification documents
    identity_document_type = Column(
        String(50),
        nullable=True,
        comment="Type of identity document"
    )
    
    identity_document_number = Column(
        String(100),
        nullable=True,
        comment="Identity document number"
    )
    
    identity_verified = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Identity verification status"
    )
    
    # Relationship
    user = relationship("User", backref=backref("profile", uselist=False))


class UserRole(BaseModel):
    """
    Module 3: Role-Based Access Control
    
    Role management system with African agricultural context.
    """
    
    __tablename__ = "user_roles_table"
    
    # Role information
    name = Column(
        String(50),
        unique=True,
        nullable=False,
        comment="Role name"
    )
    
    display_name = Column(
        String(100),
        nullable=False,
        comment="Display name for role"
    )
    
    description = Column(
        Text,
        nullable=True,
        comment="Role description"
    )
    
    # Role hierarchy
    parent_role_id = Column(
        UUID(as_uuid=True),
        ForeignKey('user_roles_table.id'),
        nullable=True,
        comment="Parent role for hierarchy"
    )
    
    role_level = Column(
        Integer,
        default=1,
        nullable=False,
        comment="Role hierarchy level"
    )
    
    # Permissions
    permissions = Column(
        JSON,
        nullable=True,
        comment="List of permissions"
    )
    
    # Role status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Role active status"
    )
    
    is_system_role = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="System role flag"
    )
    
    # African context
    applicable_regions = Column(
        JSON,
        nullable=True,
        comment="Applicable African regions"
    )
    
    cultural_context = Column(
        JSON,
        nullable=True,
        comment="Cultural context for role"
    )
    
    # Relationships
    users = relationship(
        "User",
        secondary=user_roles,
        back_populates="roles"
    )
    
    parent_role = relationship(
        "UserRole",
        remote_side="UserRole.id",
        backref="child_roles"
    )


class UserPermission(BaseModel):
    """
    Module 3: Role-Based Access Control (Permissions)
    
    Granular permission system for agricultural operations.
    """
    
    __tablename__ = "user_permissions"
    
    # Permission information
    name = Column(
        String(100),
        unique=True,
        nullable=False,
        comment="Permission name"
    )
    
    display_name = Column(
        String(150),
        nullable=False,
        comment="Display name for permission"
    )
    
    description = Column(
        Text,
        nullable=True,
        comment="Permission description"
    )
    
    # Permission category
    category = Column(
        String(50),
        nullable=False,
        comment="Permission category"
    )
    
    # Permission scope
    scope = Column(
        String(20),
        default="user",
        nullable=False,
        comment="Permission scope: user, farm, community, region, system"
    )
    
    # Resource and action
    resource = Column(
        String(50),
        nullable=False,
        comment="Resource this permission applies to"
    )
    
    action = Column(
        String(20),
        nullable=False,
        comment="Action: create, read, update, delete, execute"
    )
    
    # Permission status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Permission active status"
    )


class Community(BaseModel, GeospatialMixin, MultiLanguageMixin):
    """
    Module 4: Community Integration
    
    Community management for African agricultural communities.
    """
    
    __tablename__ = "communities"
    
    # Community information
    name = Column(
        String(200),
        nullable=False,
        comment="Community name"
    )
    
    description = Column(
        Text,
        nullable=True,
        comment="Community description"
    )
    
    community_type = Column(
        String(50),
        nullable=False,
        comment="Type: village, ethnic_group, farming_group, women_group"
    )
    
    # Leadership
    leader_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=True,
        comment="Community leader"
    )
    
    # Community details
    established_date = Column(
        Date,
        nullable=True,
        comment="Community establishment date"
    )
    
    population = Column(
        Integer,
        nullable=True,
        comment="Community population"
    )
    
    households = Column(
        Integer,
        nullable=True,
        comment="Number of households"
    )
    
    # Agricultural focus
    primary_crops = Column(
        JSON,
        nullable=True,
        comment="Primary crops grown in community"
    )
    
    primary_livestock = Column(
        JSON,
        nullable=True,
        comment="Primary livestock in community"
    )
    
    # Traditional practices
    traditional_practices = Column(
        JSON,
        nullable=True,
        comment="Traditional agricultural practices"
    )
    
    cultural_calendar = Column(
        JSON,
        nullable=True,
        comment="Cultural and agricultural calendar"
    )
    
    # Community status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Community active status"
    )
    
    verification_status = Column(
        String(20),
        default="pending",
        nullable=False,
        comment="Verification status"
    )
    
    # Relationships
    leader = relationship("User", foreign_keys=[leader_id])
    members = relationship(
        "User",
        secondary=user_communities,
        back_populates="communities"
    )


class Cooperative(BaseModel, GeospatialMixin):
    """
    Module 7: Cooperative Management
    
    Agricultural cooperative management system.
    """
    
    __tablename__ = "cooperatives"
    
    # Cooperative information
    name = Column(
        String(200),
        nullable=False,
        comment="Cooperative name"
    )
    
    registration_number = Column(
        String(100),
        unique=True,
        nullable=True,
        comment="Official registration number"
    )
    
    cooperative_type = Column(
        String(50),
        nullable=False,
        comment="Type: farming, marketing, credit, multipurpose"
    )
    
    # Legal information
    legal_status = Column(
        String(50),
        nullable=True,
        comment="Legal registration status"
    )
    
    registration_date = Column(
        Date,
        nullable=True,
        comment="Registration date"
    )
    
    # Leadership
    chairman_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=True,
        comment="Cooperative chairman"
    )
    
    secretary_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=True,
        comment="Cooperative secretary"
    )
    
    treasurer_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=True,
        comment="Cooperative treasurer"
    )
    
    # Membership
    total_members = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Total number of members"
    )
    
    active_members = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Number of active members"
    )
    
    # Financial information
    share_value = Column(
        Float,
        nullable=True,
        comment="Value per share"
    )
    
    total_shares = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Total shares issued"
    )
    
    # Services offered
    services_offered = Column(
        JSON,
        nullable=True,
        comment="List of services offered"
    )
    
    # Contact information
    contact_person = Column(
        String(200),
        nullable=True,
        comment="Contact person name"
    )
    
    contact_phone = Column(
        String(20),
        nullable=True,
        comment="Contact phone number"
    )
    
    contact_email = Column(
        String(255),
        nullable=True,
        comment="Contact email"
    )
    
    # Status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Cooperative active status"
    )
    
    # Relationships
    chairman = relationship("User", foreign_keys=[chairman_id])
    secretary = relationship("User", foreign_keys=[secretary_id])
    treasurer = relationship("User", foreign_keys=[treasurer_id])
    members = relationship(
        "User",
        secondary=user_cooperatives,
        back_populates="cooperatives"
    )


class ExtensionAgent(BaseModel):
    """
    Module 6: Extension Agent Management
    
    Agricultural extension agent management system.
    """
    
    __tablename__ = "extension_agents"
    
    # User reference
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
        unique=True,
        comment="User reference"
    )
    
    # Agent information
    agent_id = Column(
        String(50),
        unique=True,
        nullable=False,
        comment="Unique agent identifier"
    )
    
    employment_type = Column(
        String(20),
        nullable=False,
        comment="Employment type: government, ngo, private, volunteer"
    )
    
    organization = Column(
        String(200),
        nullable=True,
        comment="Employing organization"
    )
    
    # Qualifications
    education_background = Column(
        JSON,
        nullable=True,
        comment="Education background"
    )
    
    certifications = Column(
        JSON,
        nullable=True,
        comment="Professional certifications"
    )
    
    specializations = Column(
        JSON,
        nullable=True,
        comment="Areas of specialization"
    )
    
    # Service area
    service_regions = Column(
        JSON,
        nullable=True,
        comment="Regions served"
    )
    
    service_communities = Column(
        JSON,
        nullable=True,
        comment="Communities served"
    )
    
    # Performance
    farmers_served = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Number of farmers served"
    )
    
    training_sessions_conducted = Column(
        Integer,
        default=0,
        nullable=False,
        comment="Training sessions conducted"
    )
    
    # Status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Agent active status"
    )
    
    verification_status = Column(
        String(20),
        default="pending",
        nullable=False,
        comment="Verification status"
    )
    
    # Relationship
    user = relationship("User", backref=backref("extension_agent", uselist=False))


class GovernmentOfficial(BaseModel):
    """
    Module 8: Government Official Access
    
    Government official management for agricultural oversight.
    """
    
    __tablename__ = "government_officials"
    
    # User reference
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
        unique=True,
        comment="User reference"
    )
    
    # Official information
    employee_id = Column(
        String(50),
        unique=True,
        nullable=False,
        comment="Government employee ID"
    )
    
    department = Column(
        String(200),
        nullable=False,
        comment="Government department"
    )
    
    position = Column(
        String(100),
        nullable=False,
        comment="Official position/title"
    )
    
    # Jurisdiction
    jurisdiction_level = Column(
        String(20),
        nullable=False,
        comment="Jurisdiction level: local, state, national, regional"
    )
    
    jurisdiction_areas = Column(
        JSON,
        nullable=True,
        comment="Areas under jurisdiction"
    )
    
    # Authority
    authority_level = Column(
        String(20),
        nullable=False,
        comment="Authority level: view, approve, enforce"
    )
    
    permissions = Column(
        JSON,
        nullable=True,
        comment="Specific permissions"
    )
    
    # Contact
    office_address = Column(
        Text,
        nullable=True,
        comment="Office address"
    )
    
    office_phone = Column(
        String(20),
        nullable=True,
        comment="Office phone number"
    )
    
    # Status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Official active status"
    )
    
    verification_status = Column(
        String(20),
        default="pending",
        nullable=False,
        comment="Verification status"
    )
    
    # Relationship
    user = relationship("User", backref=backref("government_official", uselist=False))


# Export all user management models
__all__ = [
    "User",
    "UserProfile", 
    "UserRole",
    "UserPermission",
    "Community",
    "Cooperative",
    "ExtensionAgent",
    "GovernmentOfficial"
]

