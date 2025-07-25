"""
WebWaka Agriculture Production Management Models

Production Management Tissue - 15 Modules:
21. Planting Activities
22. Crop Monitoring
23. Pest & Disease Management
24. Fertilizer Management
25. Irrigation Management
26. Harvest Management
27. Post-Harvest Handling
28. Livestock Breeding
29. Animal Health Management
30. Feed Management
31. Milk Production
32. Egg Production
33. Meat Production
34. Production Records
35. Quality Control

African optimizations: Traditional production methods, indigenous knowledge,
seasonal patterns, and community-based production systems.
"""

import uuid
from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from decimal import Decimal
from sqlalchemy import (
    Column, String, Boolean, DateTime, Date, Time, Text, JSON, Integer, 
    Float, Numeric, ForeignKey, Table, UniqueConstraint, Index, Enum
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
import enum

from app.models.shared import BaseModel, GeospatialMixin, MultiLanguageMixin
from app.core.database import Base

# Production-specific enums
class PlantingMethod(str, enum.Enum):
    DIRECT_SEEDING = "direct_seeding"
    TRANSPLANTING = "transplanting"
    BROADCASTING = "broadcasting"
    DRILLING = "drilling"
    TRADITIONAL = "traditional"
    INTERCROPPING = "intercropping"

class CropStage(str, enum.Enum):
    LAND_PREPARATION = "land_preparation"
    PLANTING = "planting"
    GERMINATION = "germination"
    VEGETATIVE = "vegetative"
    FLOWERING = "flowering"
    FRUITING = "fruiting"
    MATURITY = "maturity"
    HARVEST = "harvest"

class PestType(str, enum.Enum):
    INSECT = "insect"
    DISEASE = "disease"
    WEED = "weed"
    RODENT = "rodent"
    BIRD = "bird"
    NEMATODE = "nematode"

class TreatmentMethod(str, enum.Enum):
    CHEMICAL = "chemical"
    BIOLOGICAL = "biological"
    CULTURAL = "cultural"
    MECHANICAL = "mechanical"
    TRADITIONAL = "traditional"
    INTEGRATED = "integrated"

class FertilizerType(str, enum.Enum):
    ORGANIC = "organic"
    INORGANIC = "inorganic"
    COMPOST = "compost"
    MANURE = "manure"
    BIOFERTILIZER = "biofertilizer"
    TRADITIONAL = "traditional"

class HarvestMethod(str, enum.Enum):
    MANUAL = "manual"
    MECHANICAL = "mechanical"
    TRADITIONAL = "traditional"
    SELECTIVE = "selective"
    BULK = "bulk"

class AnimalBreedingMethod(str, enum.Enum):
    NATURAL = "natural"
    ARTIFICIAL_INSEMINATION = "artificial_insemination"
    EMBRYO_TRANSFER = "embryo_transfer"
    TRADITIONAL = "traditional"

class HealthStatus(str, enum.Enum):
    HEALTHY = "healthy"
    SICK = "sick"
    RECOVERING = "recovering"
    QUARANTINE = "quarantine"
    DEAD = "dead"

class FeedType(str, enum.Enum):
    CONCENTRATE = "concentrate"
    ROUGHAGE = "roughage"
    PASTURE = "pasture"
    SUPPLEMENT = "supplement"
    TRADITIONAL = "traditional"

class QualityGrade(str, enum.Enum):
    PREMIUM = "premium"
    GRADE_A = "grade_a"
    GRADE_B = "grade_b"
    GRADE_C = "grade_c"
    REJECT = "reject"


class PlantingActivity(BaseModel, GeospatialMixin):
    """
    Module 21: Planting Activities
    
    Comprehensive planting activity tracking with African agricultural practices.
    """
    
    __tablename__ = "planting_activities"
    
    # Plot and crop plan references
    plot_id = Column(
        UUID(as_uuid=True),
        ForeignKey('plots.id'),
        nullable=False,
        comment="Plot reference"
    )
    
    crop_plan_id = Column(
        UUID(as_uuid=True),
        ForeignKey('crop_plans.id'),
        nullable=True,
        comment="Crop plan reference"
    )
    
    # Activity identification
    activity_name = Column(
        String(100),
        nullable=False,
        comment="Planting activity name"
    )
    
    activity_code = Column(
        String(50),
        nullable=True,
        comment="Activity code"
    )
    
    # Crop information
    crop_name = Column(
        String(100),
        nullable=False,
        comment="Crop being planted"
    )
    
    variety = Column(
        String(100),
        nullable=True,
        comment="Crop variety"
    )
    
    local_variety_name = Column(
        String(100),
        nullable=True,
        comment="Local variety name"
    )
    
    # Planting details
    planting_date = Column(
        Date,
        nullable=False,
        comment="Actual planting date"
    )
    
    planting_method = Column(
        Enum(PlantingMethod),
        nullable=False,
        comment="Planting method used"
    )
    
    # Traditional planting information
    traditional_planting_method = Column(
        String(100),
        nullable=True,
        comment="Traditional planting method description"
    )
    
    moon_phase = Column(
        String(20),
        nullable=True,
        comment="Moon phase during planting"
    )
    
    traditional_timing_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional timing indicators used"
    )
    
    # Area and spacing
    planted_area = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Area planted in hectares"
    )
    
    row_spacing = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Row spacing in cm"
    )
    
    plant_spacing = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Plant spacing in cm"
    )
    
    planting_density = Column(
        Integer,
        nullable=True,
        comment="Plants per hectare"
    )
    
    # Seed information
    seed_source = Column(
        String(200),
        nullable=True,
        comment="Source of seeds"
    )
    
    seed_variety_details = Column(
        JSON,
        nullable=True,
        comment="Detailed seed variety information"
    )
    
    seed_quantity_used = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Quantity of seeds used in kg"
    )
    
    seed_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Cost of seeds"
    )
    
    # Soil preparation
    land_preparation_activities = Column(
        JSON,
        nullable=True,
        comment="Land preparation activities performed"
    )
    
    soil_condition_at_planting = Column(
        String(100),
        nullable=True,
        comment="Soil condition during planting"
    )
    
    # Weather conditions
    weather_conditions = Column(
        JSON,
        nullable=True,
        comment="Weather conditions during planting"
    )
    
    rainfall_before_planting = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Rainfall in mm before planting"
    )
    
    # Labor and resources
    labor_used = Column(
        JSON,
        nullable=True,
        comment="Labor resources used"
    )
    
    equipment_used = Column(
        JSON,
        nullable=True,
        comment="Equipment used for planting"
    )
    
    total_cost = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Total planting cost"
    )
    
    # Expected outcomes
    expected_germination_date = Column(
        Date,
        nullable=True,
        comment="Expected germination date"
    )
    
    expected_harvest_date = Column(
        Date,
        nullable=True,
        comment="Expected harvest date"
    )
    
    expected_yield = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Expected yield in kg"
    )
    
    # Activity status
    completion_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Activity completion status"
    )
    
    success_rating = Column(
        Integer,
        nullable=True,
        comment="Success rating 1-10"
    )
    
    notes = Column(
        Text,
        nullable=True,
        comment="Additional notes"
    )
    
    # Relationships
    plot = relationship("Plot", backref="planting_activities")
    crop_plan = relationship("CropPlan", backref="planting_activities")
    
    # Indexes
    __table_args__ = (
        Index('idx_planting_plot_date', 'plot_id', 'planting_date'),
        Index('idx_planting_crop', 'crop_name', 'variety'),
        Index('idx_planting_method', 'planting_method'),
    )


class CropMonitoring(BaseModel, GeospatialMixin):
    """
    Module 22: Crop Monitoring
    
    Comprehensive crop growth monitoring and observation system.
    """
    
    __tablename__ = "crop_monitoring"
    
    # Plot reference
    plot_id = Column(
        UUID(as_uuid=True),
        ForeignKey('plots.id'),
        nullable=False,
        comment="Plot reference"
    )
    
    # Planting activity reference
    planting_activity_id = Column(
        UUID(as_uuid=True),
        ForeignKey('planting_activities.id'),
        nullable=True,
        comment="Related planting activity"
    )
    
    # Monitoring information
    monitoring_date = Column(
        Date,
        nullable=False,
        comment="Monitoring date"
    )
    
    monitoring_time = Column(
        Time,
        nullable=True,
        comment="Monitoring time"
    )
    
    days_after_planting = Column(
        Integer,
        nullable=True,
        comment="Days after planting"
    )
    
    # Crop stage and development
    current_stage = Column(
        Enum(CropStage),
        nullable=False,
        comment="Current crop development stage"
    )
    
    stage_description = Column(
        Text,
        nullable=True,
        comment="Detailed stage description"
    )
    
    # Growth measurements
    plant_height = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Average plant height in cm"
    )
    
    number_of_leaves = Column(
        Integer,
        nullable=True,
        comment="Average number of leaves"
    )
    
    stem_diameter = Column(
        Numeric(5, 2),
        nullable=True,
        comment="Stem diameter in cm"
    )
    
    # Population and stand
    plant_population = Column(
        Integer,
        nullable=True,
        comment="Plants per hectare"
    )
    
    germination_rate = Column(
        Float,
        nullable=True,
        comment="Germination rate percentage"
    )
    
    plant_stand_uniformity = Column(
        String(20),
        nullable=True,
        comment="Stand uniformity: excellent, good, fair, poor"
    )
    
    # Health assessment
    overall_health = Column(
        String(20),
        nullable=True,
        comment="Overall crop health: excellent, good, fair, poor"
    )
    
    vigor_rating = Column(
        Integer,
        nullable=True,
        comment="Crop vigor rating 1-10"
    )
    
    stress_indicators = Column(
        JSON,
        nullable=True,
        comment="Observed stress indicators"
    )
    
    # Environmental conditions
    weather_conditions = Column(
        JSON,
        nullable=True,
        comment="Weather conditions during monitoring"
    )
    
    soil_moisture = Column(
        String(20),
        nullable=True,
        comment="Soil moisture level: dry, moist, wet, saturated"
    )
    
    # Pest and disease observations
    pest_observations = Column(
        JSON,
        nullable=True,
        comment="Pest observations"
    )
    
    disease_observations = Column(
        JSON,
        nullable=True,
        comment="Disease observations"
    )
    
    weed_pressure = Column(
        String(20),
        nullable=True,
        comment="Weed pressure: none, low, medium, high"
    )
    
    # Flowering and fruiting
    flowering_status = Column(
        String(20),
        nullable=True,
        comment="Flowering status"
    )
    
    flowering_percentage = Column(
        Float,
        nullable=True,
        comment="Percentage of plants flowering"
    )
    
    fruit_set_percentage = Column(
        Float,
        nullable=True,
        comment="Fruit set percentage"
    )
    
    # Traditional observations
    traditional_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional growth indicators observed"
    )
    
    farmer_assessment = Column(
        Text,
        nullable=True,
        comment="Farmer's assessment and observations"
    )
    
    # Recommendations
    immediate_actions_needed = Column(
        JSON,
        nullable=True,
        comment="Immediate actions recommended"
    )
    
    next_monitoring_date = Column(
        Date,
        nullable=True,
        comment="Next recommended monitoring date"
    )
    
    # Photos and documentation
    photo_urls = Column(
        JSON,
        nullable=True,
        comment="Photo URLs for visual documentation"
    )
    
    # Monitoring metadata
    monitored_by = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=True,
        comment="Person who conducted monitoring"
    )
    
    monitoring_method = Column(
        String(50),
        nullable=True,
        comment="Monitoring method used"
    )
    
    # Relationships
    plot = relationship("Plot", backref="crop_monitoring")
    planting_activity = relationship("PlantingActivity", backref="monitoring_records")
    monitored_by_user = relationship("User", foreign_keys=[monitored_by])
    
    # Indexes
    __table_args__ = (
        Index('idx_monitoring_plot_date', 'plot_id', 'monitoring_date'),
        Index('idx_monitoring_stage', 'current_stage'),
        Index('idx_monitoring_health', 'overall_health', 'vigor_rating'),
    )


class PestDiseaseManagement(BaseModel, GeospatialMixin):
    """
    Module 23: Pest & Disease Management
    
    Comprehensive pest and disease management with traditional and modern methods.
    """
    
    __tablename__ = "pest_disease_management"
    
    # Plot reference
    plot_id = Column(
        UUID(as_uuid=True),
        ForeignKey('plots.id'),
        nullable=False,
        comment="Plot reference"
    )
    
    # Incident information
    incident_date = Column(
        Date,
        nullable=False,
        comment="Date pest/disease was identified"
    )
    
    incident_type = Column(
        Enum(PestType),
        nullable=False,
        comment="Type of pest or disease"
    )
    
    # Pest/Disease identification
    pest_disease_name = Column(
        String(100),
        nullable=False,
        comment="Scientific or common name"
    )
    
    local_name = Column(
        String(100),
        nullable=True,
        comment="Local or traditional name"
    )
    
    identification_method = Column(
        String(50),
        nullable=True,
        comment="How it was identified"
    )
    
    # Severity assessment
    severity_level = Column(
        String(20),
        nullable=False,
        comment="Severity: low, medium, high, severe"
    )
    
    affected_area = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Affected area in hectares"
    )
    
    affected_percentage = Column(
        Float,
        nullable=True,
        comment="Percentage of crop affected"
    )
    
    damage_description = Column(
        Text,
        nullable=True,
        comment="Description of damage observed"
    )
    
    # Environmental factors
    weather_conditions = Column(
        JSON,
        nullable=True,
        comment="Weather conditions during outbreak"
    )
    
    contributing_factors = Column(
        JSON,
        nullable=True,
        comment="Factors contributing to outbreak"
    )
    
    # Treatment information
    treatment_date = Column(
        Date,
        nullable=True,
        comment="Date treatment was applied"
    )
    
    treatment_method = Column(
        Enum(TreatmentMethod),
        nullable=True,
        comment="Treatment method used"
    )
    
    treatment_details = Column(
        JSON,
        nullable=True,
        comment="Detailed treatment information"
    )
    
    # Traditional treatments
    traditional_treatment = Column(
        Text,
        nullable=True,
        comment="Traditional treatment methods used"
    )
    
    traditional_materials = Column(
        JSON,
        nullable=True,
        comment="Traditional materials used"
    )
    
    # Chemical treatments
    chemicals_used = Column(
        JSON,
        nullable=True,
        comment="Chemical pesticides/fungicides used"
    )
    
    application_rate = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Application rate"
    )
    
    application_method = Column(
        String(50),
        nullable=True,
        comment="Application method"
    )
    
    # Biological control
    biological_agents = Column(
        JSON,
        nullable=True,
        comment="Biological control agents used"
    )
    
    beneficial_insects_released = Column(
        JSON,
        nullable=True,
        comment="Beneficial insects released"
    )
    
    # Cultural control
    cultural_practices = Column(
        JSON,
        nullable=True,
        comment="Cultural control practices implemented"
    )
    
    # Cost and resources
    treatment_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Total treatment cost"
    )
    
    labor_hours = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Labor hours spent on treatment"
    )
    
    # Effectiveness assessment
    treatment_effectiveness = Column(
        String(20),
        nullable=True,
        comment="Treatment effectiveness: excellent, good, fair, poor"
    )
    
    follow_up_date = Column(
        Date,
        nullable=True,
        comment="Follow-up assessment date"
    )
    
    follow_up_notes = Column(
        Text,
        nullable=True,
        comment="Follow-up assessment notes"
    )
    
    # Prevention measures
    prevention_measures = Column(
        JSON,
        nullable=True,
        comment="Prevention measures implemented"
    )
    
    future_prevention_plan = Column(
        JSON,
        nullable=True,
        comment="Future prevention strategies"
    )
    
    # Economic impact
    estimated_yield_loss = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Estimated yield loss in kg"
    )
    
    economic_loss = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Estimated economic loss"
    )
    
    # Status
    incident_status = Column(
        String(20),
        default="active",
        nullable=False,
        comment="Incident status: active, controlled, resolved"
    )
    
    # Documentation
    photo_urls = Column(
        JSON,
        nullable=True,
        comment="Photos of pest/disease damage"
    )
    
    # Relationships
    plot = relationship("Plot", backref="pest_disease_incidents")
    
    # Indexes
    __table_args__ = (
        Index('idx_pest_plot_date', 'plot_id', 'incident_date'),
        Index('idx_pest_type_severity', 'incident_type', 'severity_level'),
        Index('idx_pest_status', 'incident_status'),
    )


class FertilizerApplication(BaseModel, GeospatialMixin):
    """
    Module 24: Fertilizer Management
    
    Fertilizer application tracking with traditional and modern fertilizers.
    """
    
    __tablename__ = "fertilizer_applications"
    
    # Plot reference
    plot_id = Column(
        UUID(as_uuid=True),
        ForeignKey('plots.id'),
        nullable=False,
        comment="Plot reference"
    )
    
    # Application information
    application_date = Column(
        Date,
        nullable=False,
        comment="Fertilizer application date"
    )
    
    application_name = Column(
        String(100),
        nullable=False,
        comment="Application activity name"
    )
    
    # Fertilizer details
    fertilizer_type = Column(
        Enum(FertilizerType),
        nullable=False,
        comment="Type of fertilizer"
    )
    
    fertilizer_name = Column(
        String(100),
        nullable=False,
        comment="Fertilizer product name"
    )
    
    fertilizer_grade = Column(
        String(20),
        nullable=True,
        comment="Fertilizer grade (N-P-K)"
    )
    
    # Traditional fertilizers
    traditional_fertilizer = Column(
        String(100),
        nullable=True,
        comment="Traditional fertilizer type"
    )
    
    traditional_preparation = Column(
        Text,
        nullable=True,
        comment="Traditional fertilizer preparation method"
    )
    
    # Application details
    application_rate = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Application rate in kg/ha"
    )
    
    total_quantity = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Total quantity applied in kg"
    )
    
    application_method = Column(
        String(50),
        nullable=True,
        comment="Application method"
    )
    
    # Timing and crop stage
    crop_stage_at_application = Column(
        Enum(CropStage),
        nullable=True,
        comment="Crop stage during application"
    )
    
    days_after_planting = Column(
        Integer,
        nullable=True,
        comment="Days after planting"
    )
    
    # Nutrient content
    nitrogen_content = Column(
        Float,
        nullable=True,
        comment="Nitrogen content percentage"
    )
    
    phosphorus_content = Column(
        Float,
        nullable=True,
        comment="Phosphorus content percentage"
    )
    
    potassium_content = Column(
        Float,
        nullable=True,
        comment="Potassium content percentage"
    )
    
    micronutrients = Column(
        JSON,
        nullable=True,
        comment="Micronutrient content"
    )
    
    # Soil conditions
    soil_moisture_at_application = Column(
        String(20),
        nullable=True,
        comment="Soil moisture during application"
    )
    
    soil_ph_before = Column(
        Float,
        nullable=True,
        comment="Soil pH before application"
    )
    
    # Weather conditions
    weather_conditions = Column(
        JSON,
        nullable=True,
        comment="Weather conditions during application"
    )
    
    rainfall_after_application = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Rainfall in mm after application"
    )
    
    # Cost and sourcing
    fertilizer_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Cost of fertilizer"
    )
    
    supplier = Column(
        String(200),
        nullable=True,
        comment="Fertilizer supplier"
    )
    
    purchase_date = Column(
        Date,
        nullable=True,
        comment="Purchase date"
    )
    
    # Labor and equipment
    labor_hours = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Labor hours for application"
    )
    
    equipment_used = Column(
        JSON,
        nullable=True,
        comment="Equipment used for application"
    )
    
    application_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Total application cost"
    )
    
    # Effectiveness tracking
    expected_response = Column(
        Text,
        nullable=True,
        comment="Expected crop response"
    )
    
    observed_response = Column(
        Text,
        nullable=True,
        comment="Observed crop response"
    )
    
    effectiveness_rating = Column(
        Integer,
        nullable=True,
        comment="Effectiveness rating 1-10"
    )
    
    # Environmental considerations
    environmental_impact = Column(
        JSON,
        nullable=True,
        comment="Environmental impact considerations"
    )
    
    leaching_risk = Column(
        String(20),
        nullable=True,
        comment="Nutrient leaching risk: low, medium, high"
    )
    
    # Recommendations
    next_application_date = Column(
        Date,
        nullable=True,
        comment="Next recommended application date"
    )
    
    recommendations = Column(
        Text,
        nullable=True,
        comment="Recommendations for future applications"
    )
    
    # Application status
    application_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Application status"
    )
    
    # Relationships
    plot = relationship("Plot", backref="fertilizer_applications")
    
    # Indexes
    __table_args__ = (
        Index('idx_fertilizer_plot_date', 'plot_id', 'application_date'),
        Index('idx_fertilizer_type', 'fertilizer_type'),
        Index('idx_fertilizer_crop_stage', 'crop_stage_at_application'),
    )


class IrrigationActivity(BaseModel, GeospatialMixin):
    """
    Module 25: Irrigation Management
    
    Irrigation activity tracking with traditional and modern systems.
    """
    
    __tablename__ = "irrigation_activities"
    
    # Plot reference
    plot_id = Column(
        UUID(as_uuid=True),
        ForeignKey('plots.id'),
        nullable=False,
        comment="Plot reference"
    )
    
    # Water source reference
    water_source_id = Column(
        UUID(as_uuid=True),
        ForeignKey('water_sources.id'),
        nullable=True,
        comment="Water source used"
    )
    
    # Irrigation information
    irrigation_date = Column(
        Date,
        nullable=False,
        comment="Irrigation date"
    )
    
    irrigation_time = Column(
        Time,
        nullable=True,
        comment="Irrigation start time"
    )
    
    duration_hours = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Irrigation duration in hours"
    )
    
    # Irrigation method
    irrigation_method = Column(
        String(50),
        nullable=False,
        comment="Irrigation method used"
    )
    
    traditional_method = Column(
        String(100),
        nullable=True,
        comment="Traditional irrigation method"
    )
    
    # Water application
    water_applied = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Water applied in liters"
    )
    
    application_rate = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Application rate in mm"
    )
    
    area_irrigated = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Area irrigated in hectares"
    )
    
    # Crop and timing
    crop_stage = Column(
        Enum(CropStage),
        nullable=True,
        comment="Crop stage during irrigation"
    )
    
    days_after_planting = Column(
        Integer,
        nullable=True,
        comment="Days after planting"
    )
    
    days_since_last_irrigation = Column(
        Integer,
        nullable=True,
        comment="Days since last irrigation"
    )
    
    # Soil conditions
    soil_moisture_before = Column(
        String(20),
        nullable=True,
        comment="Soil moisture before irrigation"
    )
    
    soil_moisture_after = Column(
        String(20),
        nullable=True,
        comment="Soil moisture after irrigation"
    )
    
    # Weather conditions
    weather_conditions = Column(
        JSON,
        nullable=True,
        comment="Weather conditions during irrigation"
    )
    
    temperature = Column(
        Float,
        nullable=True,
        comment="Temperature during irrigation"
    )
    
    wind_speed = Column(
        Float,
        nullable=True,
        comment="Wind speed during irrigation"
    )
    
    # Water quality
    water_quality = Column(
        String(20),
        nullable=True,
        comment="Water quality: excellent, good, fair, poor"
    )
    
    water_ph = Column(
        Float,
        nullable=True,
        comment="Water pH level"
    )
    
    salinity_level = Column(
        Float,
        nullable=True,
        comment="Water salinity level"
    )
    
    # Equipment and infrastructure
    equipment_used = Column(
        JSON,
        nullable=True,
        comment="Irrigation equipment used"
    )
    
    infrastructure_condition = Column(
        String(20),
        nullable=True,
        comment="Irrigation infrastructure condition"
    )
    
    # Cost and resources
    water_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Cost of water"
    )
    
    energy_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Energy cost for pumping"
    )
    
    labor_hours = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Labor hours for irrigation"
    )
    
    total_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Total irrigation cost"
    )
    
    # Efficiency metrics
    water_use_efficiency = Column(
        Float,
        nullable=True,
        comment="Water use efficiency percentage"
    )
    
    uniformity_coefficient = Column(
        Float,
        nullable=True,
        comment="Water distribution uniformity"
    )
    
    # Traditional practices
    traditional_timing_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional timing indicators used"
    )
    
    traditional_water_conservation = Column(
        JSON,
        nullable=True,
        comment="Traditional water conservation methods"
    )
    
    # Crop response
    crop_response = Column(
        Text,
        nullable=True,
        comment="Observed crop response to irrigation"
    )
    
    stress_relief = Column(
        String(20),
        nullable=True,
        comment="Stress relief achieved: excellent, good, fair, poor"
    )
    
    # Planning
    next_irrigation_date = Column(
        Date,
        nullable=True,
        comment="Next planned irrigation date"
    )
    
    irrigation_frequency = Column(
        String(50),
        nullable=True,
        comment="Irrigation frequency schedule"
    )
    
    # Status
    irrigation_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Irrigation status"
    )
    
    # Relationships
    plot = relationship("Plot", backref="irrigation_activities")
    water_source = relationship("WaterSource", backref="irrigation_activities")
    
    # Indexes
    __table_args__ = (
        Index('idx_irrigation_plot_date', 'plot_id', 'irrigation_date'),
        Index('idx_irrigation_method', 'irrigation_method'),
        Index('idx_irrigation_crop_stage', 'crop_stage'),
    )


# Continue with remaining production management models...
# Due to length constraints, I'll create the remaining models in the next file

# Export production management models
__all__ = [
    "PlantingActivity",
    "CropMonitoring",
    "PestDiseaseManagement",
    "FertilizerApplication",
    "IrrigationActivity",
    "PlantingMethod",
    "CropStage",
    "PestType",
    "TreatmentMethod",
    "FertilizerType",
    "HarvestMethod",
    "AnimalBreedingMethod",
    "HealthStatus",
    "FeedType",
    "QualityGrade"
]

