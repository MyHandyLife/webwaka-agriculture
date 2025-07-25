"""
WebWaka Agriculture Farm Management Models

Farm Management Tissue - 12 Modules:
9. Farm Registration
10. Plot Management
11. Crop Planning
12. Livestock Management
13. Equipment Tracking
14. Infrastructure Management
15. Resource Allocation
16. Farm Analytics
17. Geospatial Mapping
18. Soil Management
19. Water Management
20. Certification Tracking

African optimizations: Traditional farming practices, communal land management,
smallholder farm support, and indigenous knowledge integration.
"""

import uuid
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from decimal import Decimal
from sqlalchemy import (
    Column, String, Boolean, DateTime, Date, Text, JSON, Integer, 
    Float, Numeric, ForeignKey, Table, UniqueConstraint, Index, Enum
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from geoalchemy2 import Geometry
import enum

from app.models.shared import BaseModel, GeospatialMixin, MultiLanguageMixin
from app.core.database import Base

# Enums for farm management
class LandOwnershipType(str, enum.Enum):
    OWNED = "owned"
    RENTED = "rented"
    LEASED = "leased"
    SHARECROPPED = "sharecropped"
    COMMUNAL = "communal"
    TRADITIONAL = "traditional"
    FAMILY = "family"

class FarmingSystem(str, enum.Enum):
    SUBSISTENCE = "subsistence"
    COMMERCIAL = "commercial"
    MIXED = "mixed"
    ORGANIC = "organic"
    TRADITIONAL = "traditional"
    AGROECOLOGICAL = "agroecological"

class IrrigationType(str, enum.Enum):
    RAINFED = "rainfed"
    DRIP = "drip"
    SPRINKLER = "sprinkler"
    FLOOD = "flood"
    FURROW = "furrow"
    TRADITIONAL = "traditional"

class SoilType(str, enum.Enum):
    CLAY = "clay"
    SANDY = "sandy"
    LOAM = "loam"
    SILT = "silt"
    LATERITE = "laterite"
    VOLCANIC = "volcanic"
    ALLUVIAL = "alluvial"

# Association tables
farm_owners = Table(
    'farm_owners',
    Base.metadata,
    Column('farm_id', UUID(as_uuid=True), ForeignKey('farms.id'), primary_key=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
    Column('ownership_percentage', Float, default=100.0),
    Column('ownership_type', String(20), default='owner'),
    Column('start_date', Date, default=date.today),
    Column('end_date', Date, nullable=True),
    comment="Farm ownership relationships"
)

farm_workers = Table(
    'farm_workers',
    Base.metadata,
    Column('farm_id', UUID(as_uuid=True), ForeignKey('farms.id'), primary_key=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
    Column('role', String(50), default='worker'),
    Column('employment_type', String(20), default='seasonal'),
    Column('start_date', Date, default=date.today),
    Column('end_date', Date, nullable=True),
    Column('is_active', Boolean, default=True),
    comment="Farm worker relationships"
)


class Farm(BaseModel, GeospatialMixin, MultiLanguageMixin):
    """
    Module 9: Farm Registration
    
    Core farm entity with African agricultural context including traditional
    farming systems, communal land management, and smallholder support.
    """
    
    __tablename__ = "farms"
    
    # Basic farm information
    name = Column(
        String(200),
        nullable=False,
        comment="Farm name"
    )
    
    farm_code = Column(
        String(50),
        unique=True,
        nullable=True,
        comment="Unique farm identification code"
    )
    
    description = Column(
        Text,
        nullable=True,
        comment="Farm description"
    )
    
    # Farm classification
    farm_type = Column(
        String(50),
        nullable=False,
        comment="Farm type: crop, livestock, mixed, aquaculture, forestry"
    )
    
    farming_system = Column(
        Enum(FarmingSystem),
        default=FarmingSystem.SUBSISTENCE,
        nullable=False,
        comment="Farming system type"
    )
    
    # Size and area
    total_area = Column(
        Numeric(10, 4),
        nullable=True,
        comment="Total farm area in hectares"
    )
    
    cultivated_area = Column(
        Numeric(10, 4),
        nullable=True,
        comment="Cultivated area in hectares"
    )
    
    area_unit = Column(
        String(20),
        default="hectares",
        nullable=False,
        comment="Area measurement unit"
    )
    
    # Traditional area measurements
    traditional_area_measurement = Column(
        String(100),
        nullable=True,
        comment="Traditional area measurement (e.g., acres, plots)"
    )
    
    traditional_area_value = Column(
        Numeric(10, 4),
        nullable=True,
        comment="Area in traditional units"
    )
    
    # Land ownership
    land_ownership_type = Column(
        Enum(LandOwnershipType),
        default=LandOwnershipType.OWNED,
        nullable=False,
        comment="Land ownership type"
    )
    
    land_title_number = Column(
        String(100),
        nullable=True,
        comment="Land title or certificate number"
    )
    
    land_acquisition_date = Column(
        Date,
        nullable=True,
        comment="Date land was acquired"
    )
    
    # Traditional land rights
    traditional_land_rights = Column(
        JSON,
        nullable=True,
        comment="Traditional land rights and customs"
    )
    
    customary_land_authority = Column(
        String(200),
        nullable=True,
        comment="Traditional authority overseeing land"
    )
    
    # Farm establishment
    establishment_date = Column(
        Date,
        nullable=True,
        comment="Farm establishment date"
    )
    
    years_in_operation = Column(
        Integer,
        nullable=True,
        comment="Years farm has been in operation"
    )
    
    # Contact and location details
    physical_address = Column(
        Text,
        nullable=True,
        comment="Physical address of farm"
    )
    
    nearest_landmark = Column(
        String(200),
        nullable=True,
        comment="Nearest landmark for navigation"
    )
    
    access_road_condition = Column(
        String(20),
        nullable=True,
        comment="Access road condition: good, fair, poor"
    )
    
    # Climate and environment
    climate_zone = Column(
        String(50),
        nullable=True,
        comment="Climate zone classification"
    )
    
    rainfall_pattern = Column(
        String(50),
        nullable=True,
        comment="Rainfall pattern: bimodal, unimodal, irregular"
    )
    
    average_annual_rainfall = Column(
        Integer,
        nullable=True,
        comment="Average annual rainfall in mm"
    )
    
    # Topography
    topography = Column(
        String(50),
        nullable=True,
        comment="Topography: flat, hilly, mountainous, valley"
    )
    
    slope_percentage = Column(
        Float,
        nullable=True,
        comment="Average slope percentage"
    )
    
    elevation = Column(
        Integer,
        nullable=True,
        comment="Elevation above sea level in meters"
    )
    
    # Farm status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Farm active status"
    )
    
    is_certified_organic = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Organic certification status"
    )
    
    registration_status = Column(
        String(20),
        default="registered",
        nullable=False,
        comment="Registration status with authorities"
    )
    
    # Economic information
    estimated_value = Column(
        Numeric(15, 2),
        nullable=True,
        comment="Estimated farm value in local currency"
    )
    
    annual_revenue = Column(
        Numeric(15, 2),
        nullable=True,
        comment="Annual revenue in local currency"
    )
    
    # Technology adoption
    technology_level = Column(
        String(20),
        nullable=True,
        comment="Technology adoption level: low, medium, high"
    )
    
    mechanization_level = Column(
        String(20),
        nullable=True,
        comment="Mechanization level: manual, semi, fully"
    )
    
    # Relationships
    owners = relationship(
        "User",
        secondary=farm_owners,
        backref="owned_farms"
    )
    
    workers = relationship(
        "User", 
        secondary=farm_workers,
        backref="worked_farms"
    )
    
    # Indexes for performance
    __table_args__ = (
        Index('idx_farm_location', 'country_code', 'region', 'district'),
        Index('idx_farm_type_system', 'farm_type', 'farming_system'),
        Index('idx_farm_ownership', 'land_ownership_type'),
        Index('idx_farm_active', 'is_active', 'registration_status'),
    )
    
    @hybrid_property
    def total_area_acres(self) -> Optional[float]:
        """Convert total area to acres."""
        if self.total_area:
            return float(self.total_area * Decimal('2.47105'))  # 1 hectare = 2.47105 acres
        return None
    
    @hybrid_property
    def farm_age(self) -> Optional[int]:
        """Calculate farm age in years."""
        if self.establishment_date:
            return (date.today() - self.establishment_date).days // 365
        return self.years_in_operation


class Plot(BaseModel, GeospatialMixin):
    """
    Module 10: Plot Management
    
    Individual plot management within farms with traditional plot systems.
    """
    
    __tablename__ = "plots"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Plot identification
    plot_number = Column(
        String(50),
        nullable=False,
        comment="Plot number within farm"
    )
    
    plot_name = Column(
        String(100),
        nullable=True,
        comment="Plot name or identifier"
    )
    
    # Traditional plot naming
    traditional_plot_name = Column(
        String(100),
        nullable=True,
        comment="Traditional or local plot name"
    )
    
    # Plot characteristics
    area = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Plot area in hectares"
    )
    
    area_unit = Column(
        String(20),
        default="hectares",
        nullable=False,
        comment="Area measurement unit"
    )
    
    # Traditional measurements
    traditional_area_measurement = Column(
        String(50),
        nullable=True,
        comment="Traditional area measurement"
    )
    
    traditional_area_value = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Area in traditional units"
    )
    
    # Plot boundaries
    boundary_description = Column(
        Text,
        nullable=True,
        comment="Plot boundary description"
    )
    
    boundary_markers = Column(
        JSON,
        nullable=True,
        comment="Boundary markers and landmarks"
    )
    
    # Soil characteristics
    soil_type = Column(
        Enum(SoilType),
        nullable=True,
        comment="Primary soil type"
    )
    
    soil_ph = Column(
        Float,
        nullable=True,
        comment="Soil pH level"
    )
    
    soil_fertility = Column(
        String(20),
        nullable=True,
        comment="Soil fertility level: low, medium, high"
    )
    
    # Topography
    slope = Column(
        Float,
        nullable=True,
        comment="Plot slope percentage"
    )
    
    drainage = Column(
        String(20),
        nullable=True,
        comment="Drainage condition: poor, fair, good, excellent"
    )
    
    # Water access
    water_source = Column(
        String(50),
        nullable=True,
        comment="Primary water source"
    )
    
    irrigation_type = Column(
        Enum(IrrigationType),
        default=IrrigationType.RAINFED,
        nullable=False,
        comment="Irrigation type"
    )
    
    # Plot status
    current_use = Column(
        String(50),
        nullable=True,
        comment="Current land use"
    )
    
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Plot active status"
    )
    
    is_fallow = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Fallow status"
    )
    
    fallow_since = Column(
        Date,
        nullable=True,
        comment="Date plot was left fallow"
    )
    
    # Traditional practices
    traditional_practices = Column(
        JSON,
        nullable=True,
        comment="Traditional farming practices used"
    )
    
    crop_rotation_pattern = Column(
        JSON,
        nullable=True,
        comment="Traditional crop rotation pattern"
    )
    
    # Relationship
    farm = relationship("Farm", backref="plots")
    
    # Unique constraint
    __table_args__ = (
        UniqueConstraint('farm_id', 'plot_number', name='uq_farm_plot_number'),
        Index('idx_plot_farm', 'farm_id'),
        Index('idx_plot_soil', 'soil_type', 'soil_fertility'),
        Index('idx_plot_water', 'water_source', 'irrigation_type'),
    )


class CropPlan(BaseModel):
    """
    Module 11: Crop Planning
    
    Crop planning and rotation management with African crop varieties.
    """
    
    __tablename__ = "crop_plans"
    
    # Plot reference
    plot_id = Column(
        UUID(as_uuid=True),
        ForeignKey('plots.id'),
        nullable=False,
        comment="Plot reference"
    )
    
    # Planning information
    plan_name = Column(
        String(100),
        nullable=False,
        comment="Crop plan name"
    )
    
    planning_season = Column(
        String(50),
        nullable=False,
        comment="Planning season"
    )
    
    plan_year = Column(
        Integer,
        nullable=False,
        comment="Planning year"
    )
    
    # Crop information
    primary_crop = Column(
        String(100),
        nullable=False,
        comment="Primary crop to be planted"
    )
    
    crop_variety = Column(
        String(100),
        nullable=True,
        comment="Specific crop variety"
    )
    
    # African crop varieties
    local_variety_name = Column(
        String(100),
        nullable=True,
        comment="Local or traditional variety name"
    )
    
    seed_source = Column(
        String(100),
        nullable=True,
        comment="Source of seeds"
    )
    
    # Intercropping
    intercrop_crops = Column(
        JSON,
        nullable=True,
        comment="List of intercrop crops"
    )
    
    cropping_pattern = Column(
        String(50),
        nullable=True,
        comment="Cropping pattern: monocrop, intercrop, relay, mixed"
    )
    
    # Timing
    planned_planting_date = Column(
        Date,
        nullable=True,
        comment="Planned planting date"
    )
    
    expected_harvest_date = Column(
        Date,
        nullable=True,
        comment="Expected harvest date"
    )
    
    growing_period_days = Column(
        Integer,
        nullable=True,
        comment="Expected growing period in days"
    )
    
    # Traditional calendar
    traditional_planting_time = Column(
        String(100),
        nullable=True,
        comment="Traditional planting time description"
    )
    
    traditional_harvest_time = Column(
        String(100),
        nullable=True,
        comment="Traditional harvest time description"
    )
    
    # Area allocation
    planned_area = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Planned planting area in hectares"
    )
    
    # Expected outcomes
    expected_yield = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Expected yield in kg/ha"
    )
    
    expected_revenue = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Expected revenue in local currency"
    )
    
    # Input requirements
    seed_requirement = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Seed requirement in kg"
    )
    
    fertilizer_plan = Column(
        JSON,
        nullable=True,
        comment="Fertilizer application plan"
    )
    
    pesticide_plan = Column(
        JSON,
        nullable=True,
        comment="Pesticide application plan"
    )
    
    # Labor requirements
    labor_requirement = Column(
        JSON,
        nullable=True,
        comment="Labor requirement by activity"
    )
    
    # Risk assessment
    risk_factors = Column(
        JSON,
        nullable=True,
        comment="Identified risk factors"
    )
    
    mitigation_strategies = Column(
        JSON,
        nullable=True,
        comment="Risk mitigation strategies"
    )
    
    # Plan status
    plan_status = Column(
        String(20),
        default="draft",
        nullable=False,
        comment="Plan status: draft, approved, active, completed"
    )
    
    is_implemented = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Implementation status"
    )
    
    # Relationship
    plot = relationship("Plot", backref="crop_plans")
    
    # Indexes
    __table_args__ = (
        Index('idx_crop_plan_season', 'planning_season', 'plan_year'),
        Index('idx_crop_plan_crop', 'primary_crop', 'crop_variety'),
        Index('idx_crop_plan_status', 'plan_status', 'is_implemented'),
    )


class Livestock(BaseModel, GeospatialMixin):
    """
    Module 12: Livestock Management
    
    Livestock management with African livestock systems and traditional practices.
    """
    
    __tablename__ = "livestock"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Livestock identification
    animal_id = Column(
        String(50),
        unique=True,
        nullable=True,
        comment="Unique animal identification"
    )
    
    tag_number = Column(
        String(50),
        nullable=True,
        comment="Tag or ear mark number"
    )
    
    # Traditional identification
    traditional_name = Column(
        String(100),
        nullable=True,
        comment="Traditional or local name for animal"
    )
    
    traditional_marking = Column(
        String(100),
        nullable=True,
        comment="Traditional marking or identification"
    )
    
    # Animal information
    species = Column(
        String(50),
        nullable=False,
        comment="Animal species"
    )
    
    breed = Column(
        String(100),
        nullable=True,
        comment="Animal breed"
    )
    
    local_breed_name = Column(
        String(100),
        nullable=True,
        comment="Local or indigenous breed name"
    )
    
    # Physical characteristics
    gender = Column(
        String(10),
        nullable=True,
        comment="Animal gender"
    )
    
    color = Column(
        String(50),
        nullable=True,
        comment="Animal color/markings"
    )
    
    weight = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Animal weight in kg"
    )
    
    height = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Animal height in cm"
    )
    
    # Age information
    date_of_birth = Column(
        Date,
        nullable=True,
        comment="Date of birth"
    )
    
    age_months = Column(
        Integer,
        nullable=True,
        comment="Age in months"
    )
    
    # Acquisition information
    acquisition_date = Column(
        Date,
        nullable=True,
        comment="Date animal was acquired"
    )
    
    acquisition_method = Column(
        String(50),
        nullable=True,
        comment="How animal was acquired: birth, purchase, gift, inheritance"
    )
    
    acquisition_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Acquisition cost in local currency"
    )
    
    source = Column(
        String(200),
        nullable=True,
        comment="Source of animal"
    )
    
    # Parentage
    sire_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=True,
        comment="Father animal ID"
    )
    
    dam_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=True,
        comment="Mother animal ID"
    )
    
    # Health information
    health_status = Column(
        String(20),
        default="healthy",
        nullable=False,
        comment="Current health status"
    )
    
    vaccination_status = Column(
        JSON,
        nullable=True,
        comment="Vaccination records"
    )
    
    health_records = Column(
        JSON,
        nullable=True,
        comment="Health and treatment records"
    )
    
    # Production information
    production_purpose = Column(
        String(50),
        nullable=True,
        comment="Production purpose: milk, meat, eggs, breeding, draft"
    )
    
    current_production = Column(
        JSON,
        nullable=True,
        comment="Current production data"
    )
    
    # Breeding information
    breeding_status = Column(
        String(20),
        nullable=True,
        comment="Breeding status"
    )
    
    last_breeding_date = Column(
        Date,
        nullable=True,
        comment="Last breeding date"
    )
    
    expected_delivery_date = Column(
        Date,
        nullable=True,
        comment="Expected delivery date"
    )
    
    # Management
    housing_type = Column(
        String(50),
        nullable=True,
        comment="Housing type"
    )
    
    feeding_system = Column(
        String(50),
        nullable=True,
        comment="Feeding system: grazing, stall, mixed"
    )
    
    # Traditional practices
    traditional_management = Column(
        JSON,
        nullable=True,
        comment="Traditional management practices"
    )
    
    cultural_significance = Column(
        Text,
        nullable=True,
        comment="Cultural or ceremonial significance"
    )
    
    # Economic value
    current_value = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Current estimated value"
    )
    
    insurance_value = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Insurance value"
    )
    
    # Status
    status = Column(
        String(20),
        default="active",
        nullable=False,
        comment="Animal status: active, sold, dead, missing"
    )
    
    disposal_date = Column(
        Date,
        nullable=True,
        comment="Date of disposal/death/sale"
    )
    
    disposal_reason = Column(
        String(100),
        nullable=True,
        comment="Reason for disposal"
    )
    
    disposal_value = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Disposal value"
    )
    
    # Relationships
    farm = relationship("Farm", backref="livestock")
    sire = relationship("Livestock", remote_side="Livestock.id", foreign_keys=[sire_id])
    dam = relationship("Livestock", remote_side="Livestock.id", foreign_keys=[dam_id])
    
    # Indexes
    __table_args__ = (
        Index('idx_livestock_farm', 'farm_id'),
        Index('idx_livestock_species', 'species', 'breed'),
        Index('idx_livestock_status', 'status', 'health_status'),
        Index('idx_livestock_production', 'production_purpose'),
    )
    
    @hybrid_property
    def age_years(self) -> Optional[float]:
        """Calculate age in years."""
        if self.date_of_birth:
            return (date.today() - self.date_of_birth).days / 365.25
        elif self.age_months:
            return self.age_months / 12
        return None


# Continue with remaining farm management models...
# Due to length constraints, I'll create the remaining models in the next file

# Export farm management models
__all__ = [
    "Farm",
    "Plot", 
    "CropPlan",
    "Livestock",
    "LandOwnershipType",
    "FarmingSystem",
    "IrrigationType",
    "SoilType"
]

