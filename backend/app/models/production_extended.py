"""
WebWaka Agriculture Production Management Extended Models

Remaining Production Management Tissue Modules:
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

Continuation of production management with harvest, livestock, and quality systems.
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

# Import enums from production.py
from app.models.production import (
    CropStage, HarvestMethod, AnimalBreedingMethod, 
    HealthStatus, FeedType, QualityGrade
)

# Additional enums for extended production management
class HarvestStage(str, enum.Enum):
    EARLY = "early"
    OPTIMAL = "optimal"
    LATE = "late"
    OVERRIPE = "overripe"

class StorageMethod(str, enum.Enum):
    TRADITIONAL = "traditional"
    MODERN = "modern"
    REFRIGERATED = "refrigerated"
    DRIED = "dried"
    PROCESSED = "processed"

class ProcessingType(str, enum.Enum):
    CLEANING = "cleaning"
    SORTING = "sorting"
    GRADING = "grading"
    DRYING = "drying"
    MILLING = "milling"
    PACKAGING = "packaging"

class BreedingStatus(str, enum.Enum):
    BREEDING_AGE = "breeding_age"
    PREGNANT = "pregnant"
    LACTATING = "lactating"
    DRY = "dry"
    RETIRED = "retired"

class TreatmentType(str, enum.Enum):
    VACCINATION = "vaccination"
    DEWORMING = "deworming"
    MEDICATION = "medication"
    SURGERY = "surgery"
    TRADITIONAL = "traditional"

class ProductionType(str, enum.Enum):
    MILK = "milk"
    EGGS = "eggs"
    MEAT = "meat"
    FIBER = "fiber"
    MANURE = "manure"


class HarvestActivity(BaseModel, GeospatialMixin):
    """
    Module 26: Harvest Management
    
    Comprehensive harvest activity tracking with traditional methods.
    """
    
    __tablename__ = "harvest_activities"
    
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
    
    # Harvest information
    harvest_date = Column(
        Date,
        nullable=False,
        comment="Harvest date"
    )
    
    harvest_name = Column(
        String(100),
        nullable=False,
        comment="Harvest activity name"
    )
    
    # Crop information
    crop_name = Column(
        String(100),
        nullable=False,
        comment="Crop harvested"
    )
    
    variety = Column(
        String(100),
        nullable=True,
        comment="Crop variety"
    )
    
    # Harvest timing
    harvest_stage = Column(
        Enum(HarvestStage),
        nullable=False,
        comment="Harvest maturity stage"
    )
    
    days_after_planting = Column(
        Integer,
        nullable=True,
        comment="Days from planting to harvest"
    )
    
    # Traditional timing
    traditional_harvest_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional harvest timing indicators"
    )
    
    moon_phase = Column(
        String(20),
        nullable=True,
        comment="Moon phase during harvest"
    )
    
    # Harvest method
    harvest_method = Column(
        Enum(HarvestMethod),
        nullable=False,
        comment="Harvest method used"
    )
    
    traditional_harvest_method = Column(
        String(100),
        nullable=True,
        comment="Traditional harvest method description"
    )
    
    # Area and yield
    harvested_area = Column(
        Numeric(8, 4),
        nullable=True,
        comment="Area harvested in hectares"
    )
    
    total_yield = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Total yield in kg"
    )
    
    yield_per_hectare = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Yield per hectare in kg/ha"
    )
    
    # Quality assessment
    quality_grade = Column(
        Enum(QualityGrade),
        nullable=True,
        comment="Overall quality grade"
    )
    
    quality_characteristics = Column(
        JSON,
        nullable=True,
        comment="Quality characteristics observed"
    )
    
    moisture_content = Column(
        Float,
        nullable=True,
        comment="Moisture content percentage"
    )
    
    # Traditional quality assessment
    traditional_quality_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional quality indicators"
    )
    
    farmer_quality_assessment = Column(
        Text,
        nullable=True,
        comment="Farmer's quality assessment"
    )
    
    # Weather conditions
    weather_conditions = Column(
        JSON,
        nullable=True,
        comment="Weather conditions during harvest"
    )
    
    # Labor and resources
    labor_used = Column(
        JSON,
        nullable=True,
        comment="Labor resources used for harvest"
    )
    
    equipment_used = Column(
        JSON,
        nullable=True,
        comment="Equipment used for harvest"
    )
    
    harvest_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Total harvest cost"
    )
    
    # Losses and waste
    field_losses = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Field losses in kg"
    )
    
    loss_percentage = Column(
        Float,
        nullable=True,
        comment="Loss percentage"
    )
    
    loss_causes = Column(
        JSON,
        nullable=True,
        comment="Causes of losses"
    )
    
    # Economic information
    market_price = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Market price per kg"
    )
    
    estimated_revenue = Column(
        Numeric(12, 2),
        nullable=True,
        comment="Estimated revenue"
    )
    
    # Storage and handling
    immediate_storage_method = Column(
        String(50),
        nullable=True,
        comment="Immediate storage method"
    )
    
    storage_location = Column(
        String(100),
        nullable=True,
        comment="Storage location"
    )
    
    # Performance comparison
    expected_yield = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Expected yield in kg"
    )
    
    yield_variance = Column(
        Float,
        nullable=True,
        comment="Yield variance percentage"
    )
    
    performance_rating = Column(
        Integer,
        nullable=True,
        comment="Performance rating 1-10"
    )
    
    # Harvest status
    harvest_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Harvest status"
    )
    
    # Documentation
    photo_urls = Column(
        JSON,
        nullable=True,
        comment="Harvest photos"
    )
    
    notes = Column(
        Text,
        nullable=True,
        comment="Additional harvest notes"
    )
    
    # Relationships
    plot = relationship("Plot", backref="harvest_activities")
    planting_activity = relationship("PlantingActivity", backref="harvest_activities")
    
    # Indexes
    __table_args__ = (
        Index('idx_harvest_plot_date', 'plot_id', 'harvest_date'),
        Index('idx_harvest_crop', 'crop_name', 'variety'),
        Index('idx_harvest_quality', 'quality_grade', 'yield_per_hectare'),
    )


class PostHarvestHandling(BaseModel):
    """
    Module 27: Post-Harvest Handling
    
    Post-harvest processing and storage management.
    """
    
    __tablename__ = "post_harvest_handling"
    
    # Harvest activity reference
    harvest_activity_id = Column(
        UUID(as_uuid=True),
        ForeignKey('harvest_activities.id'),
        nullable=False,
        comment="Related harvest activity"
    )
    
    # Handling information
    handling_date = Column(
        Date,
        nullable=False,
        comment="Post-harvest handling date"
    )
    
    handling_activity = Column(
        String(100),
        nullable=False,
        comment="Handling activity name"
    )
    
    # Processing details
    processing_type = Column(
        Enum(ProcessingType),
        nullable=False,
        comment="Type of processing"
    )
    
    processing_method = Column(
        String(100),
        nullable=True,
        comment="Processing method used"
    )
    
    traditional_processing = Column(
        Text,
        nullable=True,
        comment="Traditional processing methods"
    )
    
    # Quantity handling
    input_quantity = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Input quantity in kg"
    )
    
    output_quantity = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Output quantity in kg"
    )
    
    processing_efficiency = Column(
        Float,
        nullable=True,
        comment="Processing efficiency percentage"
    )
    
    # Quality changes
    quality_before = Column(
        Enum(QualityGrade),
        nullable=True,
        comment="Quality before processing"
    )
    
    quality_after = Column(
        Enum(QualityGrade),
        nullable=True,
        comment="Quality after processing"
    )
    
    moisture_content_before = Column(
        Float,
        nullable=True,
        comment="Moisture content before processing"
    )
    
    moisture_content_after = Column(
        Float,
        nullable=True,
        comment="Moisture content after processing"
    )
    
    # Storage information
    storage_method = Column(
        Enum(StorageMethod),
        nullable=True,
        comment="Storage method used"
    )
    
    storage_location = Column(
        String(100),
        nullable=True,
        comment="Storage location"
    )
    
    storage_conditions = Column(
        JSON,
        nullable=True,
        comment="Storage conditions"
    )
    
    # Traditional storage
    traditional_storage_method = Column(
        Text,
        nullable=True,
        comment="Traditional storage methods"
    )
    
    traditional_preservation = Column(
        JSON,
        nullable=True,
        comment="Traditional preservation techniques"
    )
    
    # Equipment and infrastructure
    equipment_used = Column(
        JSON,
        nullable=True,
        comment="Equipment used for processing"
    )
    
    infrastructure_used = Column(
        JSON,
        nullable=True,
        comment="Infrastructure used"
    )
    
    # Cost and resources
    processing_cost = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Processing cost"
    )
    
    storage_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Storage cost"
    )
    
    labor_hours = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Labor hours for processing"
    )
    
    # Losses and waste
    processing_losses = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Processing losses in kg"
    )
    
    storage_losses = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Storage losses in kg"
    )
    
    loss_causes = Column(
        JSON,
        nullable=True,
        comment="Causes of losses"
    )
    
    # Value addition
    value_added = Column(
        Numeric(10, 2),
        nullable=True,
        comment="Value added through processing"
    )
    
    market_price_increase = Column(
        Float,
        nullable=True,
        comment="Market price increase percentage"
    )
    
    # Quality control
    quality_tests_performed = Column(
        JSON,
        nullable=True,
        comment="Quality tests performed"
    )
    
    quality_standards_met = Column(
        JSON,
        nullable=True,
        comment="Quality standards met"
    )
    
    # Packaging
    packaging_type = Column(
        String(50),
        nullable=True,
        comment="Packaging type used"
    )
    
    packaging_size = Column(
        String(20),
        nullable=True,
        comment="Packaging size"
    )
    
    packaging_cost = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Packaging cost"
    )
    
    # Status
    handling_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Handling status"
    )
    
    # Relationships
    harvest_activity = relationship("HarvestActivity", backref="post_harvest_handling")
    
    # Indexes
    __table_args__ = (
        Index('idx_postharvest_harvest', 'harvest_activity_id'),
        Index('idx_postharvest_date', 'handling_date'),
        Index('idx_postharvest_type', 'processing_type'),
    )


class LivestockBreeding(BaseModel):
    """
    Module 28: Livestock Breeding
    
    Livestock breeding management with traditional and modern methods.
    """
    
    __tablename__ = "livestock_breeding"
    
    # Animal references
    female_animal_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=False,
        comment="Female animal ID"
    )
    
    male_animal_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=True,
        comment="Male animal ID (if natural breeding)"
    )
    
    # Breeding information
    breeding_date = Column(
        Date,
        nullable=False,
        comment="Breeding date"
    )
    
    breeding_method = Column(
        Enum(AnimalBreedingMethod),
        nullable=False,
        comment="Breeding method used"
    )
    
    breeding_season = Column(
        String(20),
        nullable=True,
        comment="Breeding season"
    )
    
    # Traditional breeding
    traditional_breeding_practices = Column(
        JSON,
        nullable=True,
        comment="Traditional breeding practices"
    )
    
    traditional_timing_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional timing indicators"
    )
    
    # Breeding details
    breeding_objective = Column(
        String(100),
        nullable=True,
        comment="Breeding objective"
    )
    
    desired_traits = Column(
        JSON,
        nullable=True,
        comment="Desired traits for offspring"
    )
    
    # Artificial insemination details
    semen_source = Column(
        String(200),
        nullable=True,
        comment="Semen source (for AI)"
    )
    
    semen_batch_number = Column(
        String(50),
        nullable=True,
        comment="Semen batch number"
    )
    
    insemination_technician = Column(
        String(200),
        nullable=True,
        comment="AI technician name"
    )
    
    # Pregnancy tracking
    pregnancy_confirmed = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Pregnancy confirmation status"
    )
    
    pregnancy_confirmation_date = Column(
        Date,
        nullable=True,
        comment="Pregnancy confirmation date"
    )
    
    pregnancy_confirmation_method = Column(
        String(50),
        nullable=True,
        comment="Pregnancy confirmation method"
    )
    
    expected_delivery_date = Column(
        Date,
        nullable=True,
        comment="Expected delivery date"
    )
    
    gestation_period = Column(
        Integer,
        nullable=True,
        comment="Expected gestation period in days"
    )
    
    # Delivery information
    actual_delivery_date = Column(
        Date,
        nullable=True,
        comment="Actual delivery date"
    )
    
    delivery_complications = Column(
        Text,
        nullable=True,
        comment="Delivery complications"
    )
    
    delivery_assistance = Column(
        String(100),
        nullable=True,
        comment="Delivery assistance provided"
    )
    
    # Offspring information
    number_of_offspring = Column(
        Integer,
        nullable=True,
        comment="Number of offspring born"
    )
    
    offspring_survival_rate = Column(
        Float,
        nullable=True,
        comment="Offspring survival rate percentage"
    )
    
    offspring_details = Column(
        JSON,
        nullable=True,
        comment="Details of each offspring"
    )
    
    # Health monitoring
    pre_breeding_health_check = Column(
        JSON,
        nullable=True,
        comment="Pre-breeding health check"
    )
    
    pregnancy_health_monitoring = Column(
        JSON,
        nullable=True,
        comment="Pregnancy health monitoring"
    )
    
    post_delivery_health_check = Column(
        JSON,
        nullable=True,
        comment="Post-delivery health check"
    )
    
    # Cost tracking
    breeding_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Total breeding cost"
    )
    
    veterinary_cost = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Veterinary costs"
    )
    
    feed_cost_increase = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Additional feed costs"
    )
    
    # Performance metrics
    conception_rate = Column(
        Float,
        nullable=True,
        comment="Conception rate percentage"
    )
    
    breeding_efficiency = Column(
        Float,
        nullable=True,
        comment="Breeding efficiency score"
    )
    
    # Traditional practices
    cultural_practices = Column(
        JSON,
        nullable=True,
        comment="Cultural practices during breeding"
    )
    
    traditional_care = Column(
        JSON,
        nullable=True,
        comment="Traditional care practices"
    )
    
    # Status
    breeding_status = Column(
        Enum(BreedingStatus),
        default=BreedingStatus.BREEDING_AGE,
        nullable=False,
        comment="Current breeding status"
    )
    
    breeding_cycle_status = Column(
        String(20),
        default="active",
        nullable=False,
        comment="Breeding cycle status"
    )
    
    # Relationships
    female_animal = relationship("Livestock", foreign_keys=[female_animal_id])
    male_animal = relationship("Livestock", foreign_keys=[male_animal_id])
    
    # Indexes
    __table_args__ = (
        Index('idx_breeding_female', 'female_animal_id'),
        Index('idx_breeding_date', 'breeding_date'),
        Index('idx_breeding_status', 'breeding_status', 'breeding_cycle_status'),
    )


class AnimalHealthRecord(BaseModel):
    """
    Module 29: Animal Health Management
    
    Comprehensive animal health tracking with traditional and modern veterinary care.
    """
    
    __tablename__ = "animal_health_records"
    
    # Animal reference
    animal_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=False,
        comment="Animal reference"
    )
    
    # Health record information
    record_date = Column(
        Date,
        nullable=False,
        comment="Health record date"
    )
    
    record_type = Column(
        String(50),
        nullable=False,
        comment="Type of health record"
    )
    
    # Health assessment
    health_status = Column(
        Enum(HealthStatus),
        nullable=False,
        comment="Current health status"
    )
    
    body_condition_score = Column(
        Float,
        nullable=True,
        comment="Body condition score (1-5)"
    )
    
    weight = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Animal weight in kg"
    )
    
    temperature = Column(
        Float,
        nullable=True,
        comment="Body temperature in Celsius"
    )
    
    # Symptoms and observations
    symptoms_observed = Column(
        JSON,
        nullable=True,
        comment="Symptoms observed"
    )
    
    behavioral_changes = Column(
        Text,
        nullable=True,
        comment="Behavioral changes noted"
    )
    
    appetite_status = Column(
        String(20),
        nullable=True,
        comment="Appetite status: normal, reduced, absent"
    )
    
    # Traditional health assessment
    traditional_health_indicators = Column(
        JSON,
        nullable=True,
        comment="Traditional health indicators"
    )
    
    traditional_diagnosis = Column(
        Text,
        nullable=True,
        comment="Traditional health diagnosis"
    )
    
    # Veterinary examination
    veterinarian_name = Column(
        String(200),
        nullable=True,
        comment="Veterinarian name"
    )
    
    clinical_examination = Column(
        JSON,
        nullable=True,
        comment="Clinical examination findings"
    )
    
    diagnosis = Column(
        Text,
        nullable=True,
        comment="Veterinary diagnosis"
    )
    
    # Treatment information
    treatment_type = Column(
        Enum(TreatmentType),
        nullable=True,
        comment="Type of treatment"
    )
    
    treatment_details = Column(
        JSON,
        nullable=True,
        comment="Treatment details"
    )
    
    medications_administered = Column(
        JSON,
        nullable=True,
        comment="Medications administered"
    )
    
    # Traditional treatments
    traditional_treatment = Column(
        Text,
        nullable=True,
        comment="Traditional treatment methods"
    )
    
    herbal_medicines = Column(
        JSON,
        nullable=True,
        comment="Herbal medicines used"
    )
    
    traditional_healer = Column(
        String(200),
        nullable=True,
        comment="Traditional healer consulted"
    )
    
    # Vaccination records
    vaccines_administered = Column(
        JSON,
        nullable=True,
        comment="Vaccines administered"
    )
    
    vaccination_schedule = Column(
        JSON,
        nullable=True,
        comment="Vaccination schedule"
    )
    
    next_vaccination_date = Column(
        Date,
        nullable=True,
        comment="Next vaccination due date"
    )
    
    # Deworming records
    deworming_treatment = Column(
        JSON,
        nullable=True,
        comment="Deworming treatment details"
    )
    
    parasite_load = Column(
        String(20),
        nullable=True,
        comment="Parasite load: none, low, medium, high"
    )
    
    next_deworming_date = Column(
        Date,
        nullable=True,
        comment="Next deworming due date"
    )
    
    # Cost information
    treatment_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Treatment cost"
    )
    
    medication_cost = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Medication cost"
    )
    
    veterinary_fee = Column(
        Numeric(6, 2),
        nullable=True,
        comment="Veterinary consultation fee"
    )
    
    # Recovery tracking
    recovery_status = Column(
        String(20),
        nullable=True,
        comment="Recovery status"
    )
    
    recovery_date = Column(
        Date,
        nullable=True,
        comment="Recovery date"
    )
    
    follow_up_required = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Follow-up required"
    )
    
    follow_up_date = Column(
        Date,
        nullable=True,
        comment="Follow-up date"
    )
    
    # Prevention measures
    prevention_measures = Column(
        JSON,
        nullable=True,
        comment="Prevention measures implemented"
    )
    
    quarantine_required = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="Quarantine required"
    )
    
    quarantine_period = Column(
        Integer,
        nullable=True,
        comment="Quarantine period in days"
    )
    
    # Record status
    record_status = Column(
        String(20),
        default="active",
        nullable=False,
        comment="Health record status"
    )
    
    # Relationships
    animal = relationship("Livestock", backref="health_records")
    
    # Indexes
    __table_args__ = (
        Index('idx_health_animal_date', 'animal_id', 'record_date'),
        Index('idx_health_status', 'health_status'),
        Index('idx_health_treatment', 'treatment_type'),
    )


class FeedManagement(BaseModel):
    """
    Module 30: Feed Management
    
    Animal feed management with traditional and commercial feeds.
    """
    
    __tablename__ = "feed_management"
    
    # Animal or group reference
    animal_id = Column(
        UUID(as_uuid=True),
        ForeignKey('livestock.id'),
        nullable=True,
        comment="Individual animal reference"
    )
    
    animal_group = Column(
        String(100),
        nullable=True,
        comment="Animal group identifier"
    )
    
    # Feed information
    feeding_date = Column(
        Date,
        nullable=False,
        comment="Feeding date"
    )
    
    feeding_time = Column(
        Time,
        nullable=True,
        comment="Feeding time"
    )
    
    # Feed details
    feed_type = Column(
        Enum(FeedType),
        nullable=False,
        comment="Type of feed"
    )
    
    feed_name = Column(
        String(100),
        nullable=False,
        comment="Feed name or description"
    )
    
    feed_source = Column(
        String(200),
        nullable=True,
        comment="Feed source or supplier"
    )
    
    # Traditional feeds
    traditional_feed = Column(
        String(100),
        nullable=True,
        comment="Traditional feed type"
    )
    
    local_feed_ingredients = Column(
        JSON,
        nullable=True,
        comment="Local feed ingredients used"
    )
    
    traditional_preparation = Column(
        Text,
        nullable=True,
        comment="Traditional feed preparation method"
    )
    
    # Quantity and nutrition
    quantity_fed = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Quantity fed in kg"
    )
    
    dry_matter_content = Column(
        Float,
        nullable=True,
        comment="Dry matter content percentage"
    )
    
    protein_content = Column(
        Float,
        nullable=True,
        comment="Protein content percentage"
    )
    
    energy_content = Column(
        Float,
        nullable=True,
        comment="Energy content MJ/kg"
    )
    
    # Nutritional analysis
    nutritional_composition = Column(
        JSON,
        nullable=True,
        comment="Detailed nutritional composition"
    )
    
    feed_quality = Column(
        String(20),
        nullable=True,
        comment="Feed quality: excellent, good, fair, poor"
    )
    
    # Feeding method
    feeding_method = Column(
        String(50),
        nullable=True,
        comment="Feeding method used"
    )
    
    feeding_frequency = Column(
        String(20),
        nullable=True,
        comment="Feeding frequency"
    )
    
    # Pasture information
    pasture_type = Column(
        String(50),
        nullable=True,
        comment="Type of pasture"
    )
    
    pasture_quality = Column(
        String(20),
        nullable=True,
        comment="Pasture quality"
    )
    
    grazing_hours = Column(
        Numeric(4, 2),
        nullable=True,
        comment="Grazing hours per day"
    )
    
    # Cost information
    feed_cost = Column(
        Numeric(8, 2),
        nullable=True,
        comment="Feed cost"
    )
    
    cost_per_kg = Column(
        Numeric(6, 4),
        nullable=True,
        comment="Cost per kg of feed"
    )
    
    # Feed conversion
    feed_conversion_ratio = Column(
        Float,
        nullable=True,
        comment="Feed conversion ratio"
    )
    
    feed_efficiency = Column(
        Float,
        nullable=True,
        comment="Feed efficiency percentage"
    )
    
    # Animal response
    animal_response = Column(
        Text,
        nullable=True,
        comment="Animal response to feed"
    )
    
    intake_level = Column(
        String(20),
        nullable=True,
        comment="Feed intake level: low, normal, high"
    )
    
    # Supplements
    supplements_given = Column(
        JSON,
        nullable=True,
        comment="Supplements provided"
    )
    
    mineral_supplements = Column(
        JSON,
        nullable=True,
        comment="Mineral supplements"
    )
    
    vitamin_supplements = Column(
        JSON,
        nullable=True,
        comment="Vitamin supplements"
    )
    
    # Traditional supplements
    traditional_supplements = Column(
        JSON,
        nullable=True,
        comment="Traditional supplements used"
    )
    
    medicinal_plants = Column(
        JSON,
        nullable=True,
        comment="Medicinal plants in feed"
    )
    
    # Feed storage
    storage_method = Column(
        String(50),
        nullable=True,
        comment="Feed storage method"
    )
    
    storage_conditions = Column(
        JSON,
        nullable=True,
        comment="Feed storage conditions"
    )
    
    # Planning
    feeding_plan = Column(
        JSON,
        nullable=True,
        comment="Feeding plan details"
    )
    
    next_feeding_date = Column(
        Date,
        nullable=True,
        comment="Next feeding date"
    )
    
    # Status
    feeding_status = Column(
        String(20),
        default="completed",
        nullable=False,
        comment="Feeding status"
    )
    
    # Relationships
    animal = relationship("Livestock", backref="feed_records")
    
    # Indexes
    __table_args__ = (
        Index('idx_feed_animal_date', 'animal_id', 'feeding_date'),
        Index('idx_feed_type', 'feed_type'),
        Index('idx_feed_group', 'animal_group'),
    )


# Continue with remaining production models...
# Due to length constraints, I'll create the final production models in the next section

# Export extended production management models
__all__ = [
    "HarvestActivity",
    "PostHarvestHandling",
    "LivestockBreeding",
    "AnimalHealthRecord",
    "FeedManagement",
    "HarvestStage",
    "StorageMethod",
    "ProcessingType",
    "BreedingStatus",
    "TreatmentType",
    "ProductionType"
]

