"""
WebWaka Agriculture Models Package

Comprehensive data models for African agricultural digital transformation.
Organized by biological architecture: cells (modules) → tissues → organs → system.
"""

# Import all models to ensure they are registered with SQLAlchemy
from .user import *
from .farm import *
from .production import *
from .market import *
from .advisory import *
from .shared import *

# Model registry for biological architecture
MODEL_REGISTRY = {
    # User Management Tissue (8 modules)
    "user_management": [
        "User", "UserProfile", "UserRole", "UserPermission",
        "Community", "Cooperative", "ExtensionAgent", "GovernmentOfficial"
    ],
    
    # Farm Management Tissue (12 modules)
    "farm_management": [
        "Farm", "Plot", "CropPlan", "Livestock",
        "Equipment", "Infrastructure", "Resource", "FarmAnalytics",
        "GeospatialData", "SoilData", "WaterSource", "Certification"
    ],
    
    # Production Management Tissue (15 modules)
    "production_management": [
        "CropProduction", "PlantingRecord", "GrowthMonitoring", "PestDiseaseRecord",
        "FertilizerApplication", "IrrigationSchedule", "HarvestPlan", "YieldRecord",
        "QualityAssessment", "PostHarvestHandling", "StorageRecord", "ProcessingRecord",
        "LossRecord", "OrganicCertification", "TraceabilityRecord"
    ],
    
    # Market Access Tissue (8 modules)
    "market_access": [
        "MarketPrice", "BuyerSellerMatch", "ContractFarming", "Auction",
        "Transportation", "Payment", "TradeFinance", "ExportDocument"
    ],
    
    # Advisory Services Tissue (4 modules)
    "advisory_services": [
        "ExtensionService", "WeatherData", "BestPractice", "Training"
    ]
}

# Export all models
__all__ = [
    # User Management Models
    "User", "UserProfile", "UserRole", "UserPermission",
    "Community", "Cooperative", "ExtensionAgent", "GovernmentOfficial",
    
    # Farm Management Models
    "Farm", "Plot", "CropPlan", "Livestock",
    "Equipment", "Infrastructure", "Resource", "FarmAnalytics",
    "GeospatialData", "SoilData", "WaterSource", "Certification",
    
    # Production Management Models
    "CropProduction", "PlantingRecord", "GrowthMonitoring", "PestDiseaseRecord",
    "FertilizerApplication", "IrrigationSchedule", "HarvestPlan", "YieldRecord",
    "QualityAssessment", "PostHarvestHandling", "StorageRecord", "ProcessingRecord",
    "LossRecord", "OrganicCertification", "TraceabilityRecord",
    
    # Market Access Models
    "MarketPrice", "BuyerSellerMatch", "ContractFarming", "Auction",
    "Transportation", "Payment", "TradeFinance", "ExportDocument",
    
    # Advisory Services Models
    "ExtensionService", "WeatherData", "BestPractice", "Training",
    
    # Shared Models
    "BaseModel", "TimestampMixin", "SoftDeleteMixin", "AfricanOptimizationMixin",
    
    # Registry
    "MODEL_REGISTRY"
]

