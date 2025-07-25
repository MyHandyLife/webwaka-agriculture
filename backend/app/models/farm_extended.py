"""
WebWaka Agriculture Farm Management Extended Models

Remaining Farm Management Tissue Modules:
13. Equipment Tracking
14. Infrastructure Management  
15. Resource Allocation
16. Farm Analytics
17. Geospatial Mapping
18. Soil Management
19. Water Management
20. Certification Tracking

Continuation of farm management with equipment, infrastructure, and analytics.
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

# Additional enums for extended farm management
class EquipmentType(str, enum.Enum):
    TRACTOR = "tractor"
    PLOW = "plow"
    HARROW = "harrow"
    PLANTER = "planter"
    HARVESTER = "harvester"
    IRRIGATION = "irrigation"
    HAND_TOOLS = "hand_tools"
    TRADITIONAL = "traditional"

class EquipmentCondition(str, enum.Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    BROKEN = "broken"

class InfrastructureType(str, enum.Enum):
    STORAGE = "storage"
    PROCESSING = "processing"
    HOUSING = "housing"
    FENCING = "fencing"
    ROADS = "roads"
    WATER_SYSTEM = "water_system"
    POWER_SYSTEM = "power_system"

class WaterSourceType(str, enum.Enum):
    BOREHOLE = "borehole"
    WELL = "well"
    RIVER = "river"
    LAKE = "lake"
    RAINWATER = "rainwater"
    SPRING = "spring"
    MUNICIPAL = "municipal"

class CertificationType(str, enum.Enum):
    ORGANIC = "organic"
    FAIR_TRADE = "fair_trade"
    GAP = "gap"  # Good Agricultural Practices
    HALAL = "halal"
    KOSHER = "kosher"
    RAINFOREST_ALLIANCE = "rainforest_alliance"


class Equipment(BaseModel, GeospatialMixin):
    """
    Module 13: Equipment Tracking
    
    Farm equipment and machinery management with traditional tools.
    """
    
    __tablename__ = "equipment"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Equipment identification
    equipment_name = Column(
        String(100),
        nullable=False,
        comment="Equipment name"
    )
    
    equipment_type = Column(
        Enum(EquipmentType),
        nullable=False,
        comment="Equipment type"
    )
    
    model = Column(
        String(100),
        nullable=True,
        comment="Equipment model"
    )
    
    manufacturer = Column(
        String(100),
        nullable=True,
        comment="Manufacturer"
    )
    
    serial_number = Column(
        String(100),
        nullable=True,
        comment="Serial number"
    )
    
    # Traditional equipment
    traditional_name = Column(
        String(100),
        nullable=True,
        comment="Traditional or local name"
    )
    
    traditional_type = Column(
        String(100),
        nullable=True,
        comment="Traditional equipment type"
    )
    
    # Acquisition information
    acquisition_date = Column(
        Date,
        nullable=True,
        comment="Date acquired"
    )
    
    acquisition_cost = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Acquisition cost"
    )
    
    acquisition_method = Column(
        String(50),
        nullable=True,
        comment="How acquired: purchase, lease, gift, made"
    )
    
    supplier = Column(
        String(200),
        nullable=True,
        comment="Supplier or source"
    )
    
    # Condition and maintenance
    current_condition = Column(
        Enum(EquipmentCondition),
        default=EquipmentCondition.GOOD,
        nullable=False,
        comment="Current condition"
    )
    
    last_maintenance_date = Column(
        Date,
        nullable=True,
        comment="Last maintenance date"
    )
    
    next_maintenance_date = Column(
        Date,
        nullable=True,
        comment="Next scheduled maintenance"
    )
    
    maintenance_cost_annual = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Annual maintenance cost"
    )
    
    maintenance_records = Column(
        JSON,
        nullable=True,
        comment="Maintenance history"
    )
    
    # Usage tracking
    hours_used = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Total hours used"
    )
    
    usage_records = Column(
        JSON,
        nullable=True,
        comment="Usage tracking records"
    )
    
    # Economic information
    current_value = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Current estimated value"
    )
    
    depreciation_rate = Column(
        Float,
        nullable=True,
        comment="Annual depreciation rate"
    )
    
    insurance_value = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Insurance value"
    )
    
    # Operational details
    fuel_type = Column(
        String(50),
        nullable=True,
        comment="Fuel type required"
    )
    
    fuel_consumption = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Fuel consumption per hour"
    )
    
    operator_required = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Requires trained operator"
    )
    
    # Status
    is_operational = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Operational status"
    )
    
    is_shared = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Shared with other farmers"
    )
    
    sharing_arrangement = Column(
        JSON,
        nullable=True,
        comment="Sharing arrangement details"
    )
    
    # Relationship
    farm = relationship("Farm", backref="equipment")
    
    # Indexes
    __table_args__ = (
        Index('idx_equipment_farm', 'farm_id'),
        Index('idx_equipment_type', 'equipment_type'),
        Index('idx_equipment_condition', 'current_condition', 'is_operational'),
    )


class Infrastructure(BaseModel, GeospatialMixin):
    """
    Module 14: Infrastructure Management
    
    Farm infrastructure management including traditional structures.
    """
    
    __tablename__ = "infrastructure"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Infrastructure identification
    name = Column(
        String(100),
        nullable=False,
        comment="Infrastructure name"
    )
    
    infrastructure_type = Column(
        Enum(InfrastructureType),
        nullable=False,
        comment="Infrastructure type"
    )
    
    description = Column(
        Text,
        nullable=True,
        comment="Infrastructure description"
    )
    
    # Traditional infrastructure
    traditional_name = Column(
        String(100),
        nullable=True,
        comment="Traditional name"
    )
    
    traditional_design = Column(
        Text,
        nullable=True,
        comment="Traditional design elements"
    )
    
    # Physical characteristics
    dimensions = Column(
        JSON,
        nullable=True,
        comment="Dimensions (length, width, height)"
    )
    
    capacity = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Storage or processing capacity"
    )
    
    capacity_unit = Column(
        String(20),
        nullable=True,
        comment="Capacity measurement unit"
    )
    
    materials_used = Column(
        JSON,
        nullable=True,
        comment="Construction materials"
    )
    
    # Construction information
    construction_date = Column(
        Date,
        nullable=True,
        comment="Construction completion date"
    )
    
    construction_cost = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Construction cost"
    )
    
    contractor = Column(
        String(200),
        nullable=True,
        comment="Contractor or builder"
    )
    
    # Condition and maintenance
    current_condition = Column(
        String(20),
        default="good",
        nullable=False,
        comment="Current condition"
    )
    
    last_maintenance_date = Column(
        Date,
        nullable=True,
        comment="Last maintenance date"
    )
    
    maintenance_schedule = Column(
        JSON,
        nullable=True,
        comment="Maintenance schedule"
    )
    
    maintenance_cost_annual = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Annual maintenance cost"
    )
    
    # Utilities
    has_electricity = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Has electricity connection"
    )
    
    has_water = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Has water connection"
    )
    
    has_drainage = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Has drainage system"
    )
    
    # Economic information
    current_value = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Current estimated value"
    )
    
    insurance_value = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Insurance value"
    )
    
    # Usage
    current_usage = Column(
        String(100),
        nullable=True,
        comment="Current usage"
    )
    
    utilization_rate = Column(
        Float,
        nullable=True,
        comment="Utilization rate percentage"
    )
    
    # Status
    is_functional = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Functional status"
    )
    
    # Relationship
    farm = relationship("Farm", backref="infrastructure")
    
    # Indexes
    __table_args__ = (
        Index('idx_infrastructure_farm', 'farm_id'),
        Index('idx_infrastructure_type', 'infrastructure_type'),
        Index('idx_infrastructure_condition', 'current_condition', 'is_functional'),
    )


class Resource(BaseModel):
    """
    Module 15: Resource Allocation
    
    Farm resource management and allocation tracking.
    """
    
    __tablename__ = "resources"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Resource identification
    resource_name = Column(
        String(100),
        nullable=False,
        comment="Resource name"
    )
    
    resource_type = Column(
        String(50),
        nullable=False,
        comment="Resource type: input, labor, financial, natural"
    )
    
    resource_category = Column(
        String(50),
        nullable=True,
        comment="Resource category"
    )
    
    # Quantity and units
    total_quantity = Column(
        Numeric(12, 4),
        nullable=True,
        comment="Total quantity available"
    )
    
    allocated_quantity = Column(
        Numeric(12, 4),
        nullable=True,
        comment="Currently allocated quantity"
    )
    
    available_quantity = Column(
        Numeric(12, 4),
        nullable=True,
        comment="Available quantity"
    )
    
    unit_of_measurement = Column(
        String(20),
        nullable=True,
        comment="Unit of measurement"
    )
    
    # Cost information
    unit_cost = Column(
        Numeric(10, 4),
        nullable=True,
        comment="Cost per unit"
    )
    
    total_cost = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Total cost"
    )
    
    # Allocation tracking
    allocation_records = Column(
        JSON,
        nullable=True,
        comment="Resource allocation records"
    )
    
    allocation_plan = Column(
        JSON,
        nullable=True,
        comment="Resource allocation plan"
    )
    
    # Procurement information
    supplier = Column(
        String(200),
        nullable=True,
        comment="Resource supplier"
    )
    
    procurement_date = Column(
        Date,
        nullable=True,
        comment="Procurement date"
    )
    
    expiry_date = Column(
        Date,
        nullable=True,
        comment="Expiry date"
    )
    
    # Quality information
    quality_grade = Column(
        String(20),
        nullable=True,
        comment="Quality grade"
    )
    
    quality_specifications = Column(
        JSON,
        nullable=True,
        comment="Quality specifications"
    )
    
    # Storage information
    storage_location = Column(
        String(100),
        nullable=True,
        comment="Storage location"
    )
    
    storage_conditions = Column(
        JSON,
        nullable=True,
        comment="Required storage conditions"
    )
    
    # Status
    status = Column(
        String(20),
        default="available",
        nullable=False,
        comment="Resource status"
    )
    
    # Relationship
    farm = relationship("Farm", backref="resources")
    
    # Indexes
    __table_args__ = (
        Index('idx_resource_farm', 'farm_id'),
        Index('idx_resource_type', 'resource_type', 'resource_category'),
        Index('idx_resource_status', 'status'),
    )


class FarmAnalytics(BaseModel):
    """
    Module 16: Farm Analytics
    
    Farm performance analytics and metrics tracking.
    """
    
    __tablename__ = "farm_analytics"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Analytics period
    analytics_period = Column(
        String(20),
        nullable=False,
        comment="Analytics period: daily, weekly, monthly, seasonal, annual"
    )
    
    period_start_date = Column(
        Date,
        nullable=False,
        comment="Period start date"
    )
    
    period_end_date = Column(
        Date,
        nullable=False,
        comment="Period end date"
    )
    
    # Production metrics
    total_production = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Total production in kg"
    )
    
    yield_per_hectare = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Yield per hectare"
    )
    
    production_efficiency = Column(
        Float,
        nullable=True,
        comment="Production efficiency percentage"
    )
    
    # Financial metrics
    total_revenue = Column(
        Numeric(15, 2),
        nullable=True,
        comment="Total revenue"
    )
    
    total_costs = Column(
        Numeric(15, 2),
        nullable=True,
        comment="Total costs"
    )
    
    net_profit = Column(
        Numeric(15, 2),
        nullable=True,
        comment="Net profit"
    )
    
    profit_margin = Column(
        Float,
        nullable=True,
        comment="Profit margin percentage"
    )
    
    roi = Column(
        Float,
        nullable=True,
        comment="Return on investment percentage"
    )
    
    # Cost breakdown
    input_costs = Column(
        JSON,
        nullable=True,
        comment="Input costs breakdown"
    )
    
    labor_costs = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Labor costs"
    )
    
    equipment_costs = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Equipment costs"
    )
    
    # Resource utilization
    land_utilization = Column(
        Float,
        nullable=True,
        comment="Land utilization percentage"
    )
    
    water_usage = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Water usage in liters"
    )
    
    fertilizer_usage = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Fertilizer usage in kg"
    )
    
    # Sustainability metrics
    carbon_footprint = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Carbon footprint in CO2 equivalent"
    )
    
    biodiversity_index = Column(
        Float,
        nullable=True,
        comment="Biodiversity index"
    )
    
    soil_health_score = Column(
        Float,
        nullable=True,
        comment="Soil health score"
    )
    
    # Risk metrics
    weather_risk_score = Column(
        Float,
        nullable=True,
        comment="Weather risk score"
    )
    
    market_risk_score = Column(
        Float,
        nullable=True,
        comment="Market risk score"
    )
    
    pest_disease_incidents = Column(
        Integer,
        nullable=True,
        comment="Number of pest/disease incidents"
    )
    
    # Comparative metrics
    regional_benchmark = Column(
        JSON,
        nullable=True,
        comment="Regional benchmark comparison"
    )
    
    historical_comparison = Column(
        JSON,
        nullable=True,
        comment="Historical performance comparison"
    )
    
    # Analytics metadata
    calculation_method = Column(
        String(50),
        nullable=True,
        comment="Calculation method used"
    )
    
    data_quality_score = Column(
        Float,
        nullable=True,
        comment="Data quality score"
    )
    
    # Relationship
    farm = relationship("Farm", backref="analytics")
    
    # Indexes
    __table_args__ = (
        Index('idx_analytics_farm_period', 'farm_id', 'analytics_period'),
        Index('idx_analytics_dates', 'period_start_date', 'period_end_date'),
    )


class GeospatialData(BaseModel, GeospatialMixin):
    """
    Module 17: Geospatial Mapping
    
    Geospatial data management for farms and plots.
    """
    
    __tablename__ = "geospatial_data"
    
    # Reference (can be farm, plot, or other entity)
    entity_type = Column(
        String(50),
        nullable=False,
        comment="Entity type: farm, plot, infrastructure, etc."
    )
    
    entity_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        comment="Entity ID"
    )
    
    # Geospatial information
    geometry_type = Column(
        String(20),
        nullable=False,
        comment="Geometry type: point, polygon, line"
    )
    
    coordinates = Column(
        JSON,
        nullable=False,
        comment="Coordinate data"
    )
    
    # Boundary information
    boundary_points = Column(
        JSON,
        nullable=True,
        comment="Boundary coordinate points"
    )
    
    area_calculated = Column(
        Numeric(10, 4),
        nullable=True,
        comment="Calculated area in hectares"
    )
    
    perimeter = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Perimeter in meters"
    )
    
    # Mapping metadata
    mapping_date = Column(
        Date,
        nullable=True,
        comment="Date of mapping"
    )
    
    mapping_method = Column(
        String(50),
        nullable=True,
        comment="Mapping method: gps, satellite, survey, traditional"
    )
    
    accuracy_level = Column(
        Float,
        nullable=True,
        comment="Accuracy level in meters"
    )
    
    coordinate_system = Column(
        String(50),
        default="WGS84",
        nullable=False,
        comment="Coordinate reference system"
    )
    
    # Traditional mapping
    traditional_boundaries = Column(
        JSON,
        nullable=True,
        comment="Traditional boundary descriptions"
    )
    
    landmarks = Column(
        JSON,
        nullable=True,
        comment="Natural and cultural landmarks"
    )
    
    # Satellite imagery
    satellite_image_url = Column(
        String(500),
        nullable=True,
        comment="Satellite image URL"
    )
    
    image_date = Column(
        Date,
        nullable=True,
        comment="Satellite image date"
    )
    
    image_resolution = Column(
        Float,
        nullable=True,
        comment="Image resolution in meters"
    )
    
    # Elevation data
    elevation_data = Column(
        JSON,
        nullable=True,
        comment="Elevation data points"
    )
    
    slope_analysis = Column(
        JSON,
        nullable=True,
        comment="Slope analysis data"
    )
    
    # Status
    is_verified = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Verification status"
    )
    
    verification_date = Column(
        Date,
        nullable=True,
        comment="Verification date"
    )
    
    # Indexes
    __table_args__ = (
        Index('idx_geospatial_entity', 'entity_type', 'entity_id'),
        Index('idx_geospatial_location', 'country_code', 'region'),
    )


class SoilData(BaseModel, GeospatialMixin):
    """
    Module 18: Soil Management
    
    Comprehensive soil data management and analysis.
    """
    
    __tablename__ = "soil_data"
    
    # Plot reference
    plot_id = Column(
        UUID(as_uuid=True),
        ForeignKey('plots.id'),
        nullable=False,
        comment="Plot reference"
    )
    
    # Sample information
    sample_id = Column(
        String(50),
        unique=True,
        nullable=True,
        comment="Soil sample ID"
    )
    
    sampling_date = Column(
        Date,
        nullable=False,
        comment="Soil sampling date"
    )
    
    sampling_depth = Column(
        Integer,
        nullable=True,
        comment="Sampling depth in cm"
    )
    
    sampling_method = Column(
        String(50),
        nullable=True,
        comment="Sampling method"
    )
    
    # Physical properties
    soil_texture = Column(
        String(50),
        nullable=True,
        comment="Soil texture classification"
    )
    
    sand_percentage = Column(
        Float,
        nullable=True,
        comment="Sand percentage"
    )
    
    silt_percentage = Column(
        Float,
        nullable=True,
        comment="Silt percentage"
    )
    
    clay_percentage = Column(
        Float,
        nullable=True,
        comment="Clay percentage"
    )
    
    bulk_density = Column(
        Float,
        nullable=True,
        comment="Bulk density g/cm³"
    )
    
    porosity = Column(
        Float,
        nullable=True,
        comment="Soil porosity percentage"
    )
    
    # Chemical properties
    ph_level = Column(
        Float,
        nullable=True,
        comment="Soil pH level"
    )
    
    organic_matter = Column(
        Float,
        nullable=True,
        comment="Organic matter percentage"
    )
    
    nitrogen_content = Column(
        Float,
        nullable=True,
        comment="Nitrogen content ppm"
    )
    
    phosphorus_content = Column(
        Float,
        nullable=True,
        comment="Phosphorus content ppm"
    )
    
    potassium_content = Column(
        Float,
        nullable=True,
        comment="Potassium content ppm"
    )
    
    # Micronutrients
    micronutrients = Column(
        JSON,
        nullable=True,
        comment="Micronutrient analysis"
    )
    
    # Biological properties
    microbial_activity = Column(
        Float,
        nullable=True,
        comment="Microbial activity index"
    )
    
    earthworm_count = Column(
        Integer,
        nullable=True,
        comment="Earthworm count per m²"
    )
    
    # Soil health indicators
    soil_health_score = Column(
        Float,
        nullable=True,
        comment="Overall soil health score"
    )
    
    fertility_rating = Column(
        String(20),
        nullable=True,
        comment="Fertility rating: low, medium, high"
    )
    
    # Traditional assessment
    traditional_soil_type = Column(
        String(100),
        nullable=True,
        comment="Traditional soil type name"
    )
    
    traditional_fertility_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional fertility indicators"
    )
    
    farmer_assessment = Column(
        Text,
        nullable=True,
        comment="Farmer's soil assessment"
    )
    
    # Recommendations
    fertilizer_recommendations = Column(
        JSON,
        nullable=True,
        comment="Fertilizer recommendations"
    )
    
    lime_requirement = Column(
        Float,
        nullable=True,
        comment="Lime requirement kg/ha"
    )
    
    organic_matter_recommendations = Column(
        JSON,
        nullable=True,
        comment="Organic matter recommendations"
    )
    
    # Analysis metadata
    laboratory = Column(
        String(200),
        nullable=True,
        comment="Testing laboratory"
    )
    
    analysis_method = Column(
        String(100),
        nullable=True,
        comment="Analysis method used"
    )
    
    report_url = Column(
        String(500),
        nullable=True,
        comment="Soil analysis report URL"
    )
    
    # Relationship
    plot = relationship("Plot", backref="soil_data")
    
    # Indexes
    __table_args__ = (
        Index('idx_soil_plot', 'plot_id'),
        Index('idx_soil_date', 'sampling_date'),
        Index('idx_soil_health', 'soil_health_score', 'fertility_rating'),
    )


class WaterSource(BaseModel, GeospatialMixin):
    """
    Module 19: Water Management
    
    Water source and irrigation management system.
    """
    
    __tablename__ = "water_sources"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Water source information
    source_name = Column(
        String(100),
        nullable=False,
        comment="Water source name"
    )
    
    source_type = Column(
        Enum(WaterSourceType),
        nullable=False,
        comment="Water source type"
    )
    
    description = Column(
        Text,
        nullable=True,
        comment="Water source description"
    )
    
    # Traditional water source
    traditional_name = Column(
        String(100),
        nullable=True,
        comment="Traditional name for water source"
    )
    
    cultural_significance = Column(
        Text,
        nullable=True,
        comment="Cultural significance of water source"
    )
    
    # Capacity and flow
    capacity = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Water capacity in liters"
    )
    
    flow_rate = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Flow rate in liters per minute"
    )
    
    depth = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Depth in meters"
    )
    
    # Water quality
    water_quality = Column(
        String(20),
        nullable=True,
        comment="Water quality: excellent, good, fair, poor"
    )
    
    ph_level = Column(
        Float,
        nullable=True,
        comment="Water pH level"
    )
    
    salinity_level = Column(
        Float,
        nullable=True,
        comment="Salinity level ppm"
    )
    
    quality_test_date = Column(
        Date,
        nullable=True,
        comment="Last quality test date"
    )
    
    quality_test_results = Column(
        JSON,
        nullable=True,
        comment="Detailed quality test results"
    )
    
    # Seasonal availability
    seasonal_availability = Column(
        JSON,
        nullable=True,
        comment="Seasonal water availability"
    )
    
    dry_season_capacity = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Dry season capacity"
    )
    
    rainy_season_capacity = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Rainy season capacity"
    )
    
    # Infrastructure
    has_pump = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Has water pump"
    )
    
    pump_type = Column(
        String(50),
        nullable=True,
        comment="Pump type"
    )
    
    has_storage = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Has water storage"
    )
    
    storage_capacity = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Storage capacity in liters"
    )
    
    # Distribution system
    distribution_method = Column(
        String(50),
        nullable=True,
        comment="Water distribution method"
    )
    
    irrigation_coverage = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Irrigation coverage in hectares"
    )
    
    # Usage tracking
    daily_usage = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Average daily usage in liters"
    )
    
    usage_records = Column(
        JSON,
        nullable=True,
        comment="Water usage records"
    )
    
    # Cost information
    development_cost = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Development cost"
    )
    
    maintenance_cost_annual = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Annual maintenance cost"
    )
    
    water_cost_per_liter = Column(
        Numeric(6, 4),
        nullable=True,
        comment="Cost per liter"
    )
    
    # Status
    is_functional = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Functional status"
    )
    
    last_maintenance_date = Column(
        Date,
        nullable=True,
        comment="Last maintenance date"
    )
    
    # Relationship
    farm = relationship("Farm", backref="water_sources")
    
    # Indexes
    __table_args__ = (
        Index('idx_water_farm', 'farm_id'),
        Index('idx_water_type', 'source_type'),
        Index('idx_water_quality', 'water_quality', 'is_functional'),
    )


class Certification(BaseModel):
    """
    Module 20: Certification Tracking
    
    Agricultural certification management and tracking.
    """
    
    __tablename__ = "certifications"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Certification information
    certification_name = Column(
        String(100),
        nullable=False,
        comment="Certification name"
    )
    
    certification_type = Column(
        Enum(CertificationType),
        nullable=False,
        comment="Certification type"
    )
    
    certification_body = Column(
        String(200),
        nullable=False,
        comment="Certifying organization"
    )
    
    # Certification details
    certificate_number = Column(
        String(100),
        unique=True,
        nullable=True,
        comment="Certificate number"
    )
    
    issue_date = Column(
        Date,
        nullable=False,
        comment="Certificate issue date"
    )
    
    expiry_date = Column(
        Date,
        nullable=False,
        comment="Certificate expiry date"
    )
    
    # Scope
    certification_scope = Column(
        JSON,
        nullable=True,
        comment="Certification scope and coverage"
    )
    
    certified_area = Column(
        Numeric(10, 4),
        nullable=True,
        comment="Certified area in hectares"
    )
    
    certified_crops = Column(
        JSON,
        nullable=True,
        comment="List of certified crops"
    )
    
    # Standards and requirements
    standards_version = Column(
        String(50),
        nullable=True,
        comment="Standards version"
    )
    
    requirements_met = Column(
        JSON,
        nullable=True,
        comment="Requirements met for certification"
    )
    
    compliance_score = Column(
        Float,
        nullable=True,
        comment="Compliance score percentage"
    )
    
    # Audit information
    last_audit_date = Column(
        Date,
        nullable=True,
        comment="Last audit date"
    )
    
    next_audit_date = Column(
        Date,
        nullable=True,
        comment="Next scheduled audit date"
    )
    
    auditor_name = Column(
        String(200),
        nullable=True,
        comment="Auditor name"
    )
    
    audit_report_url = Column(
        String(500),
        nullable=True,
        comment="Audit report URL"
    )
    
    # Cost information
    certification_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Certification cost"
    )
    
    annual_fee = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Annual certification fee"
    )
    
    audit_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Audit cost"
    )
    
    # Benefits tracking
    premium_received = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Premium price received"
    )
    
    market_access_benefits = Column(
        JSON,
        nullable=True,
        comment="Market access benefits"
    )
    
    # Status
    status = Column(
        String(20),
        default="active",
        nullable=False,
        comment="Certification status: active, expired, suspended, revoked"
    )
    
    renewal_status = Column(
        String(20),
        nullable=True,
        comment="Renewal status"
    )
    
    # Documents
    certificate_url = Column(
        String(500),
        nullable=True,
        comment="Certificate document URL"
    )
    
    supporting_documents = Column(
        JSON,
        nullable=True,
        comment="Supporting document URLs"
    )
    
    # Relationship
    farm = relationship("Farm", backref="certifications")
    
    # Indexes
    __table_args__ = (
        Index('idx_certification_farm', 'farm_id'),
        Index('idx_certification_type', 'certification_type'),
        Index('idx_certification_status', 'status', 'expiry_date'),
    )


# Export extended farm management models
__all__ = [
    "Equipment",
    "Infrastructure",
    "Resource", 
    "FarmAnalytics",
    "GeospatialData",
    "SoilData",
    "WaterSource",
    "Certification",
    "EquipmentType",
    "EquipmentCondition",
    "InfrastructureType",
    "WaterSourceType",
    "CertificationType"
]

