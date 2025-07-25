"""
WebWaka Agriculture Production Management Final Models

Final Production Management Tissue Modules:
31. Milk Production
32. Egg Production
33. Meat Production
34. Production Records
35. Quality Control

Completion of production management with specialized production tracking and quality systems.
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

# Import enums from previous production models
from app.models.production_extended import ProductionType, QualityGrade

# Additional enums for final production management
class MilkingMethod(str, enum.Enum):
    HAND_MILKING = "hand_milking"
    MACHINE_MILKING = "machine_milking"
    TRADITIONAL = "traditional"

class EggCollectionMethod(str, enum.Enum):
    MANUAL = "manual"
    AUTOMATED = "automated"
    TRADITIONAL = "traditional"

class SlaughterMethod(str, enum.Enum):
    TRADITIONAL = "traditional"
    MODERN = "modern"
    HALAL = "halal"
    KOSHER = "kosher"

class QualityTestType(str, enum.Enum):
    VISUAL = "visual"
    CHEMICAL = "chemical"
    MICROBIOLOGICAL = "microbiological"
    PHYSICAL = "physical"
    SENSORY = "sensory"
    TRADITIONAL = "traditional"


class MilkProduction(BaseModel):
    """
    Module 31: Milk Production
    
    Dairy production tracking with traditional and modern milking systems.
    """
    
    __tablename__ = "milk_production"
    
    # Animal reference
    animal_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=False,
        comment="Dairy animal reference"
    )
    
    # Production information
    production_date = Column(
        Date,
        nullable=False,
        comment="Milk production date"
    )
    
    milking_session = Column(
        String(20),
        nullable=False,
        comment="Milking session: morning, afternoon, evening"
    )
    
    milking_time = Column(
        Time,
        nullable=True,
        comment="Milking time"
    )
    
    # Milking details
    milking_method = Column(
        Enum(MilkingMethod),
        nullable=False,
        comment="Milking method used"
    )
    
    traditional_milking_practice = Column(
        Text,
        nullable=True,
        comment="Traditional milking practices"
    )
    
    # Production quantity
    milk_yield = Column(
        Numeric(6, 2),
        nullable=False,
        comment="Milk yield in liters"
    )
    
    milking_duration = Column(
        Integer,
        nullable=True,
        comment="Milking duration in minutes"
    )
    
    # Lactation information
    days_in_lactation = Column(
        Integer,
        nullable=True,
        comment="Days in lactation"
    )
    
    lactation_number = Column(
        Integer,
        nullable=True,
        comment="Lactation number"
    )
    
    peak_lactation = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Peak lactation period"
    )
    
    # Quality assessment
    milk_quality = Column(
        Enum(QualityGrade),
        nullable=True,
        comment="Milk quality grade"
    )
    
    fat_content = Column(
        Float,
        nullable=True,
        comment="Fat content percentage"
    )
    
    protein_content = Column(
        Float,
        nullable=True,
        comment="Protein content percentage"
    )
    
    somatic_cell_count = Column(
        Integer,
        nullable=True,
        comment="Somatic cell count"
    )
    
    # Traditional quality indicators
    traditional_quality_assessment = Column(
        JSON,
        nullable=True,
        comment="Traditional quality indicators"
    )
    
    color_assessment = Column(
        String(50),
        nullable=True,
        comment="Milk color assessment"
    )
    
    taste_assessment = Column(
        String(50),
        nullable=True,
        comment="Milk taste assessment"
    )
    
    # Environmental factors
    weather_conditions = Column(
        JSON,
        nullable=True,
        comment="Weather conditions during milking"
    )
    
    temperature = Column(
        Float,
        nullable=True,
        comment="Temperature during milking"
    )
    
    # Animal condition
    animal_health_status = Column(
        String(20),
        nullable=True,
        comment="Animal health during milking"
    )
    
    udder_condition = Column(
        String(20),
        nullable=True,
        comment="Udder condition"
    )
    
    stress_indicators = Column(
        JSON,
        nullable=True,
        comment="Animal stress indicators"
    )
    
    # Feed and nutrition impact
    feed_type_before_milking = Column(
        String(100),
        nullable=True,
        comment="Feed type before milking"
    )
    
    water_intake = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Water intake in liters"
    )
    
    # Handling and storage
    immediate_handling = Column(
        String(50),
        nullable=True,
        comment="Immediate milk handling"
    )
    
    storage_method = Column(
        String(50),
        nullable=True,
        comment="Milk storage method"
    )
    
    storage_temperature = Column(
        Float,
        nullable=True,
        comment="Storage temperature"
    )
    
    # Traditional preservation
    traditional_preservation = Column(
        JSON,
        nullable=True,
        comment="Traditional preservation methods"
    )
    
    fermentation_process = Column(
        Text,
        nullable=True,
        comment="Traditional fermentation process"
    )
    
    # Economic information
    milk_price = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Milk price per liter"
    )
    
    revenue = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Revenue from milk sale"
    )
    
    buyer = Column(
        String(200),
        nullable=True,
        comment="Milk buyer"
    )
    
    # Usage allocation
    home_consumption = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Milk for home consumption"
    )
    
    calf_feeding = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Milk for calf feeding"
    )
    
    processing = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Milk for processing"
    )
    
    sale_quantity = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Milk quantity sold"
    )
    
    # Performance metrics
    daily_average = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Daily average milk yield"
    )
    
    monthly_total = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Monthly total milk production"
    )
    
    # Equipment and hygiene
    milking_equipment = Column(
        JSON,
        nullable=True,
        comment="Milking equipment used"
    )
    
    hygiene_practices = Column(
        JSON,
        nullable=True,
        comment="Hygiene practices followed"
    )
    
    # Status
    production_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Production status"
    )
    
    # Relationships
    animal = relationship("Livestock", backref="milk_production")
    
    # Indexes
    __table_args__ = (
        Index('idx_milk_animal_date', 'animal_id', 'production_date'),
        Index('idx_milk_session', 'milking_session'),
        Index('idx_milk_quality', 'milk_quality', 'milk_yield'),
    )


class EggProduction(BaseModel):
    """
    Module 32: Egg Production
    
    Poultry egg production tracking with traditional and modern systems.
    """
    
    __tablename__ = "egg_production"
    
    # Flock or individual bird reference
    animal_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=True,
        comment="Individual bird reference"
    )
    
    flock_id = Column(
        String(50),
        nullable=True,
        comment="Flock identifier"
    )
    
    # Production information
    production_date = Column(
        Date,
        nullable=False,
        comment="Egg production date"
    )
    
    collection_time = Column(
        Time,
        nullable=True,
        comment="Egg collection time"
    )
    
    # Collection details
    collection_method = Column(
        Enum(EggCollectionMethod),
        nullable=False,
        comment="Egg collection method"
    )
    
    traditional_collection_practice = Column(
        Text,
        nullable=True,
        comment="Traditional collection practices"
    )
    
    # Production quantity
    eggs_collected = Column(
        Integer,
        nullable=False,
        comment="Number of eggs collected"
    )
    
    collection_frequency = Column(
        String(20),
        nullable=True,
        comment="Collection frequency"
    )
    
    # Egg characteristics
    average_egg_weight = Column(
        Numeric(5, 2),
        nullable=True,
        comment="Average egg weight in grams"
    )
    
    egg_size_distribution = Column(
        JSON,
        nullable=True,
        comment="Egg size distribution"
    )
    
    shell_color = Column(
        String(20),
        nullable=True,
        comment="Predominant shell color"
    )
    
    # Quality assessment
    egg_quality = Column(
        Enum(QualityGrade),
        nullable=True,
        comment="Overall egg quality"
    )
    
    shell_quality = Column(
        String(20),
        nullable=True,
        comment="Shell quality: excellent, good, fair, poor"
    )
    
    cracked_eggs = Column(
        Integer,
        nullable=True,
        comment="Number of cracked eggs"
    )
    
    dirty_eggs = Column(
        Integer,
        nullable=True,
        comment="Number of dirty eggs"
    )
    
    # Traditional quality indicators
    traditional_quality_assessment = Column(
        JSON,
        nullable=True,
        comment="Traditional quality indicators"
    )
    
    freshness_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional freshness indicators"
    )
    
    # Flock information
    flock_size = Column(
        Integer,
        nullable=True,
        comment="Total flock size"
    )
    
    laying_hens = Column(
        Integer,
        nullable=True,
        comment="Number of laying hens"
    )
    
    production_rate = Column(
        Float,
        nullable=True,
        comment="Production rate percentage"
    )
    
    # Environmental factors
    weather_conditions = Column(
        JSON,
        nullable=True,
        comment="Weather conditions"
    )
    
    temperature = Column(
        Float,
        nullable=True,
        comment="Temperature during production"
    )
    
    daylight_hours = Column(
        Float,
        nullable=True,
        comment="Daylight hours"
    )
    
    # Housing and management
    housing_type = Column(
        String(50),
        nullable=True,
        comment="Housing type"
    )
    
    nesting_boxes = Column(
        Integer,
        nullable=True,
        comment="Number of nesting boxes"
    )
    
    traditional_housing = Column(
        Text,
        nullable=True,
        comment="Traditional housing description"
    )
    
    # Feed and nutrition
    feed_type = Column(
        String(100),
        nullable=True,
        comment="Feed type provided"
    )
    
    feed_consumption = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Feed consumption in kg"
    )
    
    traditional_feed = Column(
        JSON,
        nullable=True,
        comment="Traditional feed ingredients"
    )
    
    # Health status
    flock_health = Column(
        String(20),
        nullable=True,
        comment="Overall flock health"
    )
    
    mortality_count = Column(
        Integer,
        nullable=True,
        comment="Mortality count"
    )
    
    health_issues = Column(
        JSON,
        nullable=True,
        comment="Health issues observed"
    )
    
    # Economic information
    egg_price = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Price per egg or per dozen"
    )
    
    revenue = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Revenue from egg sales"
    )
    
    buyer = Column(
        String(200),
        nullable=True,
        comment="Egg buyer"
    )
    
    # Usage allocation
    home_consumption = Column(
        Integer,
        nullable=True,
        comment="Eggs for home consumption"
    )
    
    hatching_eggs = Column(
        Integer,
        nullable=True,
        comment="Eggs set for hatching"
    )
    
    sale_quantity = Column(
        Integer,
        nullable=True,
        comment="Eggs sold"
    )
    
    # Performance metrics
    daily_average = Column(
        Float,
        nullable=True,
        comment="Daily average egg production"
    )
    
    weekly_total = Column(
        Integer,
        nullable=True,
        comment="Weekly total egg production"
    )
    
    feed_conversion_ratio = Column(
        Float,
        nullable=True,
        comment="Feed conversion ratio"
    )
    
    # Storage and handling
    storage_method = Column(
        String(50),
        nullable=True,
        comment="Egg storage method"
    )
    
    storage_conditions = Column(
        JSON,
        nullable=True,
        comment="Storage conditions"
    )
    
    traditional_preservation = Column(
        JSON,
        nullable=True,
        comment="Traditional preservation methods"
    )
    
    # Status
    production_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Production status"
    )
    
    # Relationships
    animal = relationship("Livestock", backref="egg_production")
    
    # Indexes
    __table_args__ = (
        Index('idx_egg_animal_date', 'animal_id', 'production_date'),
        Index('idx_egg_flock_date', 'flock_id', 'production_date'),
        Index('idx_egg_quality', 'egg_quality', 'eggs_collected'),
    )


class MeatProduction(BaseModel):
    """
    Module 33: Meat Production
    
    Meat production tracking with traditional and modern slaughter systems.
    """
    
    __tablename__ = "meat_production"
    
    # Animal reference
    animal_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=False,
        comment="Animal reference"
    )
    
    # Slaughter information
    slaughter_date = Column(
        Date,
        nullable=False,
        comment="Slaughter date"
    )
    
    slaughter_age = Column(
        Integer,
        nullable=True,
        comment="Animal age at slaughter in months"
    )
    
    slaughter_weight = Column(
        Numeric(8, 2),
        nullable=False,
        comment="Live weight at slaughter in kg"
    )
    
    # Slaughter details
    slaughter_method = Column(
        Enum(SlaughterMethod),
        nullable=False,
        comment="Slaughter method used"
    )
    
    slaughter_location = Column(
        String(100),
        nullable=True,
        comment="Slaughter location"
    )
    
    traditional_slaughter_practice = Column(
        Text,
        nullable=True,
        comment="Traditional slaughter practices"
    )
    
    cultural_requirements = Column(
        JSON,
        nullable=True,
        comment="Cultural or religious requirements"
    )
    
    # Carcass information
    carcass_weight = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Carcass weight in kg"
    )
    
    dressing_percentage = Column(
        Float,
        nullable=True,
        comment="Dressing percentage"
    )
    
    # Meat cuts and processing
    primary_cuts = Column(
        JSON,
        nullable=True,
        comment="Primary meat cuts and weights"
    )
    
    secondary_cuts = Column(
        JSON,
        nullable=True,
        comment="Secondary cuts and processing"
    )
    
    offal_weight = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Offal weight in kg"
    )
    
    # Traditional processing
    traditional_processing = Column(
        JSON,
        nullable=True,
        comment="Traditional meat processing methods"
    )
    
    preservation_methods = Column(
        JSON,
        nullable=True,
        comment="Traditional preservation methods"
    )
    
    # Quality assessment
    meat_quality = Column(
        Enum(QualityGrade),
        nullable=True,
        comment="Meat quality grade"
    )
    
    marbling_score = Column(
        Integer,
        nullable=True,
        comment="Marbling score (1-5)"
    )
    
    tenderness_score = Column(
        Integer,
        nullable=True,
        comment="Tenderness score (1-5)"
    )
    
    color_score = Column(
        Integer,
        nullable=True,
        comment="Meat color score (1-5)"
    )
    
    # Traditional quality indicators
    traditional_quality_assessment = Column(
        JSON,
        nullable=True,
        comment="Traditional quality indicators"
    )
    
    fat_distribution = Column(
        String(50),
        nullable=True,
        comment="Fat distribution assessment"
    )
    
    # Health and safety
    ante_mortem_inspection = Column(
        JSON,
        nullable=True,
        comment="Ante-mortem inspection results"
    )
    
    post_mortem_inspection = Column(
        JSON,
        nullable=True,
        comment="Post-mortem inspection results"
    )
    
    health_certificate = Column(
        String(100),
        nullable=True,
        comment="Health certificate number"
    )
    
    # Economic information
    production_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Total production cost"
    )
    
    slaughter_cost = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Slaughter and processing cost"
    )
    
    meat_price_per_kg = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Meat price per kg"
    )
    
    total_revenue = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Total revenue from meat sales"
    )
    
    # Distribution and sales
    distribution_channels = Column(
        JSON,
        nullable=True,
        comment="Distribution channels used"
    )
    
    buyers = Column(
        JSON,
        nullable=True,
        comment="Meat buyers"
    )
    
    # Usage allocation
    home_consumption = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Meat for home consumption in kg"
    )
    
    community_sharing = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Meat shared with community in kg"
    )
    
    sale_quantity = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Meat quantity sold in kg"
    )
    
    # Storage and preservation
    storage_method = Column(
        String(50),
        nullable=True,
        comment="Meat storage method"
    )
    
    storage_temperature = Column(
        Float,
        nullable=True,
        comment="Storage temperature"
    )
    
    preservation_duration = Column(
        Integer,
        nullable=True,
        comment="Expected preservation duration in days"
    )
    
    # Performance metrics
    feed_conversion_efficiency = Column(
        Float,
        nullable=True,
        comment="Feed conversion efficiency"
    )
    
    growth_rate = Column(
        Float,
        nullable=True,
        comment="Average daily weight gain"
    )
    
    # By-products
    hide_weight = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Hide weight in kg"
    )
    
    hide_value = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Hide value"
    )
    
    other_byproducts = Column(
        JSON,
        nullable=True,
        comment="Other by-products and values"
    )
    
    # Status
    production_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Production status"
    )
    
    # Relationships
    animal = relationship("Livestock", backref="meat_production")
    
    # Indexes
    __table_args__ = (
        Index('idx_meat_animal_date', 'animal_id', 'slaughter_date'),
        Index('idx_meat_quality', 'meat_quality', 'carcass_weight'),
        Index('idx_meat_method', 'slaughter_method'),
    )


class ProductionRecord(BaseModel):
    """
    Module 34: Production Records
    
    Comprehensive production record aggregation and analysis.
    """
    
    __tablename__ = "production_records"
    
    # Farm reference
    farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=False,
        comment="Farm reference"
    )
    
    # Record information
    record_date = Column(
        Date,
        nullable=False,
        comment="Production record date"
    )
    
    record_period = Column(
        String(20),
        nullable=False,
        comment="Record period: daily, weekly, monthly, seasonal, annual"
    )
    
    production_type = Column(
        Enum(ProductionType),
        nullable=False,
        comment="Type of production"
    )
    
    # Crop production summary
    total_crop_area = Column(
        Numeric(10, 4),
        nullable=True,
        comment="Total crop area in hectares"
    )
    
    total_crop_yield = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Total crop yield in kg"
    )
    
    average_yield_per_hectare = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Average yield per hectare"
    )
    
    crop_production_details = Column(
        JSON,
        nullable=True,
        comment="Detailed crop production by type"
    )
    
    # Livestock production summary
    total_livestock_count = Column(
        Integer,
        nullable=True,
        comment="Total livestock count"
    )
    
    milk_production_total = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Total milk production in liters"
    )
    
    egg_production_total = Column(
        Integer,
        nullable=True,
        comment="Total egg production"
    )
    
    meat_production_total = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Total meat production in kg"
    )
    
    livestock_production_details = Column(
        JSON,
        nullable=True,
        comment="Detailed livestock production by type"
    )
    
    # Economic summary
    total_production_cost = Column(
        Numeric(15, 2),
        nullable=True,
        comment="Total production cost"
    )
    
    total_revenue = Column(
        Numeric(15, 2),
        nullable=True,
        comment="Total revenue"
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
    
    # Cost breakdown
    input_costs = Column(
        JSON,
        nullable=True,
        comment="Input costs breakdown"
    )
    
    labor_costs = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Labor costs"
    )
    
    equipment_costs = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Equipment costs"
    )
    
    # Productivity metrics
    land_productivity = Column(
        Float,
        nullable=True,
        comment="Land productivity index"
    )
    
    labor_productivity = Column(
        Float,
        nullable=True,
        comment="Labor productivity index"
    )
    
    resource_efficiency = Column(
        Float,
        nullable=True,
        comment="Resource use efficiency"
    )
    
    # Quality metrics
    average_quality_score = Column(
        Float,
        nullable=True,
        comment="Average quality score"
    )
    
    quality_distribution = Column(
        JSON,
        nullable=True,
        comment="Quality grade distribution"
    )
    
    # Environmental metrics
    water_usage_total = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Total water usage in liters"
    )
    
    fertilizer_usage_total = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Total fertilizer usage in kg"
    )
    
    carbon_footprint = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Carbon footprint"
    )
    
    # Traditional practices impact
    traditional_methods_percentage = Column(
        Float,
        nullable=True,
        comment="Percentage of traditional methods used"
    )
    
    traditional_knowledge_application = Column(
        JSON,
        nullable=True,
        comment="Traditional knowledge applications"
    )
    
    # Challenges and issues
    production_challenges = Column(
        JSON,
        nullable=True,
        comment="Production challenges faced"
    )
    
    pest_disease_incidents = Column(
        Integer,
        nullable=True,
        comment="Number of pest/disease incidents"
    )
    
    weather_impact = Column(
        JSON,
        nullable=True,
        comment="Weather impact on production"
    )
    
    # Performance comparison
    previous_period_comparison = Column(
        JSON,
        nullable=True,
        comment="Comparison with previous period"
    )
    
    regional_benchmark = Column(
        JSON,
        nullable=True,
        comment="Regional benchmark comparison"
    )
    
    performance_trends = Column(
        JSON,
        nullable=True,
        comment="Performance trends analysis"
    )
    
    # Recommendations
    improvement_recommendations = Column(
        JSON,
        nullable=True,
        comment="Improvement recommendations"
    )
    
    next_period_targets = Column(
        JSON,
        nullable=True,
        comment="Next period production targets"
    )
    
    # Record metadata
    data_sources = Column(
        JSON,
        nullable=True,
        comment="Data sources for record compilation"
    )
    
    data_quality_score = Column(
        Float,
        nullable=True,
        comment="Data quality score"
    )
    
    # Relationships
    farm = relationship("Farm", backref="production_records")
    
    # Indexes
    __table_args__ = (
        Index('idx_production_farm_date', 'farm_id', 'record_date'),
        Index('idx_production_period_type', 'record_period', 'production_type'),
        Index('idx_production_profit', 'net_profit', 'profit_margin'),
    )


class QualityControl(BaseModel):
    """
    Module 35: Quality Control
    
    Comprehensive quality control and assurance system.
    """
    
    __tablename__ = "quality_control"
    
    # Product reference (can be crop, milk, eggs, meat, etc.)
    product_type = Column(
        String(50),
        nullable=False,
        comment="Product type being tested"
    )
    
    product_batch_id = Column(
        String(100),
        nullable=True,
        comment="Product batch identifier"
    )
    
    source_farm_id = Column(
        UUID(as_uuid=True),
        ForeignKey('farms.id'),
        nullable=True,
        comment="Source farm reference"
    )
    
    # Quality control information
    test_date = Column(
        Date,
        nullable=False,
        comment="Quality test date"
    )
    
    test_time = Column(
        Time,
        nullable=True,
        comment="Quality test time"
    )
    
    test_location = Column(
        String(100),
        nullable=True,
        comment="Test location"
    )
    
    # Test details
    test_type = Column(
        Enum(QualityTestType),
        nullable=False,
        comment="Type of quality test"
    )
    
    test_method = Column(
        String(100),
        nullable=True,
        comment="Test method used"
    )
    
    testing_standard = Column(
        String(100),
        nullable=True,
        comment="Quality standard applied"
    )
    
    # Traditional quality assessment
    traditional_quality_methods = Column(
        JSON,
        nullable=True,
        comment="Traditional quality assessment methods"
    )
    
    elder_assessment = Column(
        Text,
        nullable=True,
        comment="Quality assessment by community elders"
    )
    
    cultural_quality_indicators = Column(
        JSON,
        nullable=True,
        comment="Cultural quality indicators"
    )
    
    # Sample information
    sample_size = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Sample size"
    )
    
    sampling_method = Column(
        String(50),
        nullable=True,
        comment="Sampling method used"
    )
    
    sample_condition = Column(
        String(50),
        nullable=True,
        comment="Sample condition"
    )
    
    # Test results
    overall_quality_grade = Column(
        Enum(QualityGrade),
        nullable=False,
        comment="Overall quality grade"
    )
    
    quality_score = Column(
        Float,
        nullable=True,
        comment="Quality score (0-100)"
    )
    
    test_results = Column(
        JSON,
        nullable=False,
        comment="Detailed test results"
    )
    
    # Physical characteristics
    appearance_score = Column(
        Float,
        nullable=True,
        comment="Appearance score"
    )
    
    color_assessment = Column(
        String(50),
        nullable=True,
        comment="Color assessment"
    )
    
    texture_assessment = Column(
        String(50),
        nullable=True,
        comment="Texture assessment"
    )
    
    size_uniformity = Column(
        Float,
        nullable=True,
        comment="Size uniformity percentage"
    )
    
    # Chemical analysis
    moisture_content = Column(
        Float,
        nullable=True,
        comment="Moisture content percentage"
    )
    
    protein_content = Column(
        Float,
        nullable=True,
        comment="Protein content percentage"
    )
    
    fat_content = Column(
        Float,
        nullable=True,
        comment="Fat content percentage"
    )
    
    ph_level = Column(
        Float,
        nullable=True,
        comment="pH level"
    )
    
    # Microbiological analysis
    total_bacterial_count = Column(
        Integer,
        nullable=True,
        comment="Total bacterial count"
    )
    
    pathogen_detection = Column(
        JSON,
        nullable=True,
        comment="Pathogen detection results"
    )
    
    shelf_life_assessment = Column(
        Integer,
        nullable=True,
        comment="Estimated shelf life in days"
    )
    
    # Sensory evaluation
    taste_score = Column(
        Float,
        nullable=True,
        comment="Taste score"
    )
    
    aroma_score = Column(
        Float,
        nullable=True,
        comment="Aroma score"
    )
    
    overall_acceptability = Column(
        Float,
        nullable=True,
        comment="Overall acceptability score"
    )
    
    # Contaminant testing
    pesticide_residues = Column(
        JSON,
        nullable=True,
        comment="Pesticide residue test results"
    )
    
    heavy_metals = Column(
        JSON,
        nullable=True,
        comment="Heavy metal test results"
    )
    
    mycotoxins = Column(
        JSON,
        nullable=True,
        comment="Mycotoxin test results"
    )
    
    # Compliance assessment
    standards_compliance = Column(
        JSON,
        nullable=True,
        comment="Standards compliance results"
    )
    
    certification_requirements = Column(
        JSON,
        nullable=True,
        comment="Certification requirements met"
    )
    
    regulatory_compliance = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Regulatory compliance status"
    )
    
    # Corrective actions
    defects_identified = Column(
        JSON,
        nullable=True,
        comment="Quality defects identified"
    )
    
    corrective_actions = Column(
        JSON,
        nullable=True,
        comment="Corrective actions recommended"
    )
    
    follow_up_required = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Follow-up testing required"
    )
    
    # Economic impact
    quality_premium = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Quality premium received"
    )
    
    rejection_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Cost of rejected products"
    )
    
    # Testing metadata
    tester_name = Column(
        String(200),
        nullable=True,
        comment="Quality tester name"
    )
    
    testing_laboratory = Column(
        String(200),
        nullable=True,
        comment="Testing laboratory"
    )
    
    test_report_url = Column(
        String(500),
        nullable=True,
        comment="Test report URL"
    )
    
    # Status
    test_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Test status"
    )
    
    approval_status = Column(
        String(20),
        default="pending",
        nullable=False,
        comment="Approval status"
    )
    
    # Relationships
    source_farm = relationship("Farm", backref="quality_controls")
    
    # Indexes
    __table_args__ = (
        Index('idx_quality_product_date', 'product_type', 'test_date'),
        Index('idx_quality_grade', 'overall_quality_grade', 'quality_score'),
        Index('idx_quality_farm', 'source_farm_id'),
    )


# Export final production management models
__all__ = [
    "MilkProduction",
    "EggProduction",
    "MeatProduction",
    "ProductionRecord",
    "QualityControl",
    "MilkingMethod",
    "EggCollectionMethod",
    "SlaughterMethod",
    "QualityTestType"
]

