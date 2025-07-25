"""
WebWaka Agriculture Configuration

Comprehensive configuration management for African agricultural platform
with environment-specific settings and African infrastructure optimizations.
"""

import os
from typing import List, Optional, Union
from functools import lru_cache

from pydantic import BaseSettings, validator, Field
from pydantic.networks import AnyHttpUrl, PostgresDsn


class Settings(BaseSettings):
    """Application settings with African optimizations."""
    
    # Application
    APP_NAME: str = "WebWaka Agriculture API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    DEBUG: bool = Field(default=False, env="DEBUG")
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7, env="REFRESH_TOKEN_EXPIRE_DAYS")
    
    # Database
    DATABASE_URL: PostgresDsn = Field(..., env="DATABASE_URL")
    DATABASE_POOL_SIZE: int = Field(default=10, env="DATABASE_POOL_SIZE")
    DATABASE_MAX_OVERFLOW: int = Field(default=20, env="DATABASE_MAX_OVERFLOW")
    
    # Redis
    REDIS_URL: str = Field(default="redis://localhost:6379", env="REDIS_URL")
    REDIS_CACHE_TTL: int = Field(default=3600, env="REDIS_CACHE_TTL")
    
    # Security
    ALLOWED_HOSTS: List[str] = Field(
        default=["localhost", "127.0.0.1", "*.webwaka.africa", "*.africa"],
        env="ALLOWED_HOSTS"
    )
    
    CORS_ORIGINS: List[AnyHttpUrl] = Field(
        default=[
            "http://localhost:3000",
            "http://localhost:3001", 
            "https://agriculture.webwaka.africa",
            "https://app.webwaka.africa"
        ],
        env="CORS_ORIGINS"
    )
    
    # African Infrastructure Optimizations
    AFRICAN_REGIONS: List[str] = Field(
        default=[
            "west-africa", "east-africa", "central-africa",
            "north-africa", "southern-africa"
        ]
    )
    
    # Offline Support
    OFFLINE_SYNC_INTERVAL: int = Field(default=300, env="OFFLINE_SYNC_INTERVAL")  # 5 minutes
    OFFLINE_CACHE_SIZE: int = Field(default=100, env="OFFLINE_CACHE_SIZE")  # MB
    ENABLE_OFFLINE_MODE: bool = Field(default=True, env="ENABLE_OFFLINE_MODE")
    
    # Mobile Optimizations
    MOBILE_IMAGE_QUALITY: int = Field(default=70, env="MOBILE_IMAGE_QUALITY")  # 70% quality
    MOBILE_MAX_IMAGE_SIZE: int = Field(default=500, env="MOBILE_MAX_IMAGE_SIZE")  # 500KB
    ENABLE_IMAGE_COMPRESSION: bool = Field(default=True, env="ENABLE_IMAGE_COMPRESSION")
    
    # Bandwidth Optimizations
    ENABLE_GZIP_COMPRESSION: bool = Field(default=True, env="ENABLE_GZIP_COMPRESSION")
    MIN_COMPRESSION_SIZE: int = Field(default=1000, env="MIN_COMPRESSION_SIZE")  # 1KB
    API_RESPONSE_CACHE_TTL: int = Field(default=300, env="API_RESPONSE_CACHE_TTL")  # 5 minutes
    
    # Language Support
    SUPPORTED_LANGUAGES: List[str] = Field(
        default=["en", "fr", "ar", "sw", "ha", "yo", "am", "zu"],
        env="SUPPORTED_LANGUAGES"
    )
    DEFAULT_LANGUAGE: str = Field(default="en", env="DEFAULT_LANGUAGE")
    
    # Geospatial Configuration
    MAPBOX_ACCESS_TOKEN: Optional[str] = Field(default=None, env="MAPBOX_ACCESS_TOKEN")
    ENABLE_GEOSPATIAL: bool = Field(default=True, env="ENABLE_GEOSPATIAL")
    DEFAULT_MAP_CENTER: List[float] = Field(default=[0.0, 20.0])  # Center of Africa
    
    # Weather Integration
    OPENWEATHER_API_KEY: Optional[str] = Field(default=None, env="OPENWEATHER_API_KEY")
    WEATHER_CACHE_TTL: int = Field(default=1800, env="WEATHER_CACHE_TTL")  # 30 minutes
    ENABLE_WEATHER_ALERTS: bool = Field(default=True, env="ENABLE_WEATHER_ALERTS")
    
    # Market Data
    MARKET_DATA_UPDATE_INTERVAL: int = Field(default=3600, env="MARKET_DATA_UPDATE_INTERVAL")  # 1 hour
    ENABLE_PRICE_ALERTS: bool = Field(default=True, env="ENABLE_PRICE_ALERTS")
    
    # File Storage
    UPLOAD_DIR: str = Field(default="uploads", env="UPLOAD_DIR")
    MAX_FILE_SIZE: int = Field(default=10485760, env="MAX_FILE_SIZE")  # 10MB
    ALLOWED_FILE_TYPES: List[str] = Field(
        default=["jpg", "jpeg", "png", "pdf", "doc", "docx", "xls", "xlsx"],
        env="ALLOWED_FILE_TYPES"
    )
    
    # SMS Integration (for African mobile networks)
    SMS_PROVIDER: str = Field(default="twilio", env="SMS_PROVIDER")
    SMS_API_KEY: Optional[str] = Field(default=None, env="SMS_API_KEY")
    SMS_API_SECRET: Optional[str] = Field(default=None, env="SMS_API_SECRET")
    ENABLE_SMS_NOTIFICATIONS: bool = Field(default=True, env="ENABLE_SMS_NOTIFICATIONS")
    
    # Mobile Money Integration
    MOBILE_MONEY_PROVIDERS: List[str] = Field(
        default=["mpesa", "mtn_money", "orange_money", "airtel_money"],
        env="MOBILE_MONEY_PROVIDERS"
    )
    ENABLE_MOBILE_PAYMENTS: bool = Field(default=True, env="ENABLE_MOBILE_PAYMENTS")
    
    # Monitoring & Logging
    SENTRY_DSN: Optional[str] = Field(default=None, env="SENTRY_DSN")
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    ENABLE_METRICS: bool = Field(default=True, env="ENABLE_METRICS")
    
    # Performance
    WORKER_PROCESSES: int = Field(default=1, env="WORKER_PROCESSES")
    WORKER_CONNECTIONS: int = Field(default=1000, env="WORKER_CONNECTIONS")
    KEEPALIVE_TIMEOUT: int = Field(default=2, env="KEEPALIVE_TIMEOUT")
    
    # African Cultural Settings
    ENABLE_TRADITIONAL_CALENDAR: bool = Field(default=True, env="ENABLE_TRADITIONAL_CALENDAR")
    ENABLE_COMMUNITY_FEATURES: bool = Field(default=True, env="ENABLE_COMMUNITY_FEATURES")
    ENABLE_COOPERATIVE_SUPPORT: bool = Field(default=True, env="ENABLE_COOPERATIVE_SUPPORT")
    
    # Data Sovereignty
    DATA_RESIDENCY_REQUIRED: bool = Field(default=True, env="DATA_RESIDENCY_REQUIRED")
    ENABLE_DATA_EXPORT: bool = Field(default=True, env="ENABLE_DATA_EXPORT")
    DATA_RETENTION_DAYS: int = Field(default=2555, env="DATA_RETENTION_DAYS")  # 7 years
    
    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    @validator("ALLOWED_HOSTS", pre=True)
    def assemble_allowed_hosts(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    @validator("SUPPORTED_LANGUAGES", pre=True)
    def assemble_languages(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    class Config:
        env_file = ".env"
        case_sensitive = True


class DevelopmentSettings(Settings):
    """Development environment settings."""
    
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"
    
    # Relaxed security for development
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    # Development database
    DATABASE_URL: PostgresDsn = "postgresql://webwaka:webwaka@localhost/webwaka_agriculture_dev"


class ProductionSettings(Settings):
    """Production environment settings."""
    
    ENVIRONMENT: str = "production"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    
    # Strict security for production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    
    # Production optimizations
    WORKER_PROCESSES: int = 4
    WORKER_CONNECTIONS: int = 2000
    
    # Enhanced caching
    REDIS_CACHE_TTL: int = 7200  # 2 hours
    API_RESPONSE_CACHE_TTL: int = 600  # 10 minutes


class TestingSettings(Settings):
    """Testing environment settings."""
    
    ENVIRONMENT: str = "testing"
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"
    
    # Test database
    DATABASE_URL: PostgresDsn = "postgresql://webwaka:webwaka@localhost/webwaka_agriculture_test"
    
    # Disable external services in tests
    ENABLE_SMS_NOTIFICATIONS: bool = False
    ENABLE_WEATHER_ALERTS: bool = False
    ENABLE_METRICS: bool = False


@lru_cache()
def get_settings() -> Settings:
    """Get application settings based on environment."""
    environment = os.getenv("ENVIRONMENT", "development").lower()
    
    if environment == "production":
        return ProductionSettings()
    elif environment == "testing":
        return TestingSettings()
    else:
        return DevelopmentSettings()


# Global settings instance
settings = get_settings()


# African Country Configurations
AFRICAN_COUNTRIES = {
    "NG": {  # Nigeria
        "name": "Nigeria",
        "region": "west-africa",
        "languages": ["en", "ha", "yo"],
        "currency": "NGN",
        "mobile_money": ["mtn_money", "airtel_money"],
        "timezone": "Africa/Lagos"
    },
    "KE": {  # Kenya
        "name": "Kenya",
        "region": "east-africa", 
        "languages": ["en", "sw"],
        "currency": "KES",
        "mobile_money": ["mpesa", "airtel_money"],
        "timezone": "Africa/Nairobi"
    },
    "GH": {  # Ghana
        "name": "Ghana",
        "region": "west-africa",
        "languages": ["en"],
        "currency": "GHS",
        "mobile_money": ["mtn_money", "airtel_money"],
        "timezone": "Africa/Accra"
    },
    "ZA": {  # South Africa
        "name": "South Africa",
        "region": "southern-africa",
        "languages": ["en", "zu"],
        "currency": "ZAR",
        "mobile_money": [],
        "timezone": "Africa/Johannesburg"
    },
    "ET": {  # Ethiopia
        "name": "Ethiopia",
        "region": "east-africa",
        "languages": ["am", "en"],
        "currency": "ETB",
        "mobile_money": [],
        "timezone": "Africa/Addis_Ababa"
    },
    "SN": {  # Senegal
        "name": "Senegal",
        "region": "west-africa",
        "languages": ["fr"],
        "currency": "XOF",
        "mobile_money": ["orange_money"],
        "timezone": "Africa/Dakar"
    },
    "EG": {  # Egypt
        "name": "Egypt",
        "region": "north-africa",
        "languages": ["ar", "en"],
        "currency": "EGP",
        "mobile_money": [],
        "timezone": "Africa/Cairo"
    },
    "MA": {  # Morocco
        "name": "Morocco",
        "region": "north-africa",
        "languages": ["ar", "fr"],
        "currency": "MAD",
        "mobile_money": [],
        "timezone": "Africa/Casablanca"
    }
}


# Crop Calendar Data for African Regions
CROP_CALENDARS = {
    "west-africa": {
        "rainy_season": {"start": "05-01", "end": "10-31"},
        "dry_season": {"start": "11-01", "end": "04-30"},
        "main_crops": ["maize", "rice", "cassava", "yam", "cocoa"],
        "planting_months": ["04", "05", "06"],
        "harvest_months": ["09", "10", "11", "12"]
    },
    "east-africa": {
        "long_rains": {"start": "03-01", "end": "05-31"},
        "short_rains": {"start": "10-01", "end": "12-31"},
        "main_crops": ["maize", "beans", "coffee", "tea", "bananas"],
        "planting_months": ["03", "04", "10", "11"],
        "harvest_months": ["07", "08", "01", "02"]
    },
    "southern-africa": {
        "rainy_season": {"start": "11-01", "end": "03-31"},
        "dry_season": {"start": "04-01", "end": "10-31"},
        "main_crops": ["maize", "wheat", "soybeans", "tobacco"],
        "planting_months": ["10", "11", "12"],
        "harvest_months": ["03", "04", "05"]
    },
    "north-africa": {
        "winter_season": {"start": "11-01", "end": "04-30"},
        "summer_season": {"start": "05-01", "end": "10-31"},
        "main_crops": ["wheat", "barley", "olives", "citrus"],
        "planting_months": ["11", "12", "01"],
        "harvest_months": ["05", "06", "07"]
    },
    "central-africa": {
        "rainy_season": {"start": "04-01", "end": "11-30"},
        "dry_season": {"start": "12-01", "end": "03-31"},
        "main_crops": ["cassava", "plantain", "cocoa", "coffee"],
        "planting_months": ["04", "05", "06"],
        "harvest_months": ["10", "11", "12"]
    }
}

