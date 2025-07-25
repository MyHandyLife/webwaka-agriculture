"""
WebWaka Agriculture Testing Configuration
Comprehensive test fixtures for African agricultural system testing
"""

import pytest
import asyncio
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from unittest.mock import Mock, AsyncMock
import json

# Test data for African agricultural contexts
AFRICAN_COUNTRIES = [
    "Nigeria", "Kenya", "Ghana", "Uganda", "Tanzania", "Ethiopia", 
    "South Africa", "Senegal", "Mali", "Burkina Faso", "Rwanda", "Malawi"
]

AFRICAN_LANGUAGES = {
    "en": "English",
    "sw": "Kiswahili", 
    "ha": "Hausa",
    "yo": "Yoruba",
    "ig": "Igbo",
    "am": "Amharic",
    "fr": "Français",
    "ar": "العربية"
}

TRADITIONAL_CROPS = {
    "Nigeria": ["White Yam", "Cassava", "Plantain", "Cocoyam", "Sweet Potato"],
    "Kenya": ["Maize", "Beans", "Sweet Potato", "Cassava", "Millet"],
    "Ghana": ["Yam", "Cassava", "Plantain", "Maize", "Cocoa"],
    "Uganda": ["Banana", "Cassava", "Sweet Potato", "Maize", "Beans"],
    "Ethiopia": ["Teff", "Barley", "Wheat", "Maize", "Sorghum"]
}

TRADITIONAL_LIVESTOCK = {
    "West Africa": ["West African Dwarf Goat", "Djallonke Sheep", "Local Chicken"],
    "East Africa": ["Zebu Cattle", "Red Maasai Sheep", "Local Goat"],
    "Southern Africa": ["Nguni Cattle", "Damara Sheep", "Boer Goat"]
}

MOON_PHASES = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", 
               "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]

TRADITIONAL_FARMING_METHODS = [
    "Traditional Mounding", "Ridge Planting", "Intercropping", 
    "Crop Rotation", "Fallowing", "Mixed Farming"
]

NETWORK_CONDITIONS = {
    "2G": {"bandwidth": "64kbps", "latency": "500ms", "packet_loss": "5%"},
    "3G": {"bandwidth": "384kbps", "latency": "200ms", "packet_loss": "2%"},
    "4G": {"bandwidth": "10Mbps", "latency": "50ms", "packet_loss": "0.5%"},
    "WiFi": {"bandwidth": "50Mbps", "latency": "20ms", "packet_loss": "0.1%"}
}

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def african_farmer_profile():
    """Sample African farmer profile for testing."""
    return {
        "id": "farmer_001",
        "name": "Adaora Okafor",
        "traditional_title": "Eze Ubi",  # Farm King in Igbo
        "phone_number": "+234803123456",
        "country": "Nigeria",
        "state": "Enugu",
        "village": "Nsukka",
        "ethnic_group": "Igbo",
        "primary_language": "ig",
        "secondary_languages": ["en"],
        "farming_experience": 15,
        "farm_size": 2.5,  # hectares
        "primary_crops": ["White Yam", "Cassava", "Plantain"],
        "livestock": ["Local Chicken", "West African Dwarf Goat"],
        "traditional_knowledge": True,
        "cooperative_member": True,
        "mobile_money_user": True,
        "education_level": "Primary",
        "gender": "Female",
        "age": 42,
        "family_size": 6
    }

@pytest.fixture
def african_farm_data():
    """Sample African farm data for testing."""
    return {
        "id": "farm_001",
        "name": "Okafor Family Farm",
        "owner_id": "farmer_001",
        "location": {
            "country": "Nigeria",
            "state": "Enugu", 
            "lga": "Nsukka",
            "village": "Nsukka",
            "coordinates": {"lat": 6.8567, "lng": 7.3958}
        },
        "total_area": 2.5,
        "land_ownership": "Family Land",
        "traditional_authority": "Village Head Approval",
        "plots": [
            {
                "id": "plot_001",
                "name": "Ubi Plot",
                "area": 1.0,
                "crop": "White Yam",
                "soil_type": "Loamy",
                "traditional_boundary": "Marked by Iroko Tree"
            },
            {
                "id": "plot_002", 
                "name": "Akpu Plot",
                "area": 1.5,
                "crop": "Cassava",
                "soil_type": "Sandy Loam",
                "traditional_boundary": "Stone Markers"
            }
        ],
        "water_sources": ["Seasonal Stream", "Rain Water"],
        "traditional_practices": ["Crop Rotation", "Intercropping"],
        "certification": None,
        "established_year": 2010
    }

@pytest.fixture
def traditional_planting_activity():
    """Sample traditional planting activity for testing."""
    return {
        "id": "planting_001",
        "farmer_id": "farmer_001",
        "plot_id": "plot_001",
        "crop": "White Yam",
        "variety": "Local Variety - Ubi Ọcha",
        "planting_date": "2024-04-15",
        "method": "Traditional Mounding",
        "moon_phase": "Waxing Moon",
        "traditional_indicators": "First rains after dry season",
        "seed_source": "Saved from previous harvest",
        "quantity_planted": "200 setts",
        "expected_harvest": "2024-12-15",
        "traditional_timing": "After Iroko tree flowers",
        "cultural_practices": ["Blessing ceremony", "Community planting"]
    }

@pytest.fixture
def mobile_device_specs():
    """Mobile device specifications for African context testing."""
    return {
        "smartphone": {
            "screen_size": "5.5 inches",
            "resolution": "720x1280",
            "ram": "2GB",
            "storage": "16GB",
            "network": "3G/4G",
            "battery": "3000mAh",
            "os": "Android 8.0"
        },
        "feature_phone": {
            "screen_size": "2.4 inches",
            "resolution": "240x320",
            "ram": "512MB",
            "storage": "4GB",
            "network": "2G/3G",
            "battery": "1500mAh",
            "os": "KaiOS"
        }
    }

@pytest.fixture
def network_simulation():
    """Network condition simulation for African contexts."""
    def simulate_network(condition: str):
        if condition not in NETWORK_CONDITIONS:
            raise ValueError(f"Unknown network condition: {condition}")
        return NETWORK_CONDITIONS[condition]
    return simulate_network

@pytest.fixture
def cultural_calendar():
    """African cultural calendar for agricultural timing."""
    return {
        "Nigeria": {
            "planting_season": {"start": "April", "end": "June"},
            "harvest_season": {"start": "October", "end": "December"},
            "cultural_festivals": ["New Yam Festival", "Harvest Festival"],
            "traditional_indicators": ["First rains", "Iroko flowering"]
        },
        "Kenya": {
            "long_rains": {"start": "March", "end": "May"},
            "short_rains": {"start": "October", "end": "December"},
            "cultural_festivals": ["Harvest Festival"],
            "traditional_indicators": ["Acacia flowering", "Bird migration"]
        }
    }

@pytest.fixture
def offline_data_sync():
    """Offline data synchronization testing utilities."""
    return {
        "pending_sync": [],
        "sync_conflicts": [],
        "last_sync": None,
        "offline_duration": timedelta(hours=0),
        "sync_priority": ["user_data", "farm_data", "production_data"]
    }

@pytest.fixture
def multi_language_content():
    """Multi-language content for testing."""
    return {
        "welcome_message": {
            "en": "Welcome to WebWaka Agriculture",
            "sw": "Karibu WebWaka Kilimo",
            "ha": "Maraba da zuwa WebWaka Noma",
            "yo": "Kaabo si WebWaka Ogbin",
            "ig": "Ndewo na WebWaka Oru Ugbo",
            "am": "እንኳን ወደ ዌብዋካ ግብርና በደህና መጡ",
            "fr": "Bienvenue à WebWaka Agriculture",
            "ar": "مرحباً بكم في ويب واكا للزراعة"
        },
        "crop_names": {
            "White Yam": {
                "en": "White Yam",
                "ig": "Ubi Ọcha",
                "yo": "Isu Funfun",
                "ha": "Doya Fari"
            },
            "Cassava": {
                "en": "Cassava", 
                "ig": "Akpu",
                "yo": "Gbaguda",
                "ha": "Rogo"
            }
        }
    }

@pytest.fixture
def traditional_knowledge_base():
    """Traditional agricultural knowledge for testing."""
    return {
        "planting_indicators": {
            "moon_phase": "Plant root crops during waxing moon",
            "weather": "Plant after first substantial rains",
            "natural_signs": "When Iroko tree flowers bloom"
        },
        "pest_control": {
            "neem_oil": "Traditional pest control using neem leaves",
            "wood_ash": "Wood ash for soil amendment and pest control",
            "companion_planting": "Marigold with tomatoes for pest control"
        },
        "soil_management": {
            "crop_rotation": "Rotate legumes with cereals",
            "fallowing": "Allow land to rest every 3-4 years",
            "organic_matter": "Use animal manure and compost"
        }
    }

@pytest.fixture
def accessibility_requirements():
    """WCAG 2.2 AA accessibility requirements for testing."""
    return {
        "color_contrast": {"normal_text": 4.5, "large_text": 3.0},
        "keyboard_navigation": True,
        "screen_reader_support": True,
        "focus_indicators": True,
        "alt_text": True,
        "form_labels": True,
        "heading_structure": True,
        "language_attributes": True,
        "error_identification": True,
        "resize_text": {"max_zoom": "200%", "no_horizontal_scroll": True}
    }

@pytest.fixture
def security_requirements():
    """Security requirements for African data sovereignty."""
    return {
        "data_encryption": {"at_rest": True, "in_transit": True},
        "authentication": {"multi_factor": True, "phone_based": True},
        "authorization": {"role_based": True, "community_based": True},
        "data_residency": {"african_servers": True, "local_backup": True},
        "privacy": {"gdpr_compliant": True, "african_privacy_laws": True},
        "audit_logging": {"user_actions": True, "data_access": True}
    }

@pytest.fixture
def performance_benchmarks():
    """Performance benchmarks for African network conditions."""
    return {
        "page_load_time": {"2G": 3.0, "3G": 2.0, "4G": 1.0},  # seconds
        "api_response_time": {"2G": 2.0, "3G": 1.0, "4G": 0.5},  # seconds
        "offline_sync_time": {"small_dataset": 5.0, "large_dataset": 30.0},  # seconds
        "battery_usage": {"low_power_mode": True, "background_sync": "minimal"},
        "data_usage": {"compression": 0.9, "caching": 0.8}  # reduction ratios
    }

# Test utilities
class AfricanTestUtils:
    """Utility class for African agricultural testing."""
    
    @staticmethod
    def generate_phone_number(country_code: str = "+234") -> str:
        """Generate a valid African phone number."""
        import random
        return f"{country_code}{random.randint(7000000000, 9999999999)}"
    
    @staticmethod
    def simulate_offline_period(duration_hours: int = 24):
        """Simulate offline period for testing."""
        return {
            "start_time": datetime.now(),
            "duration": timedelta(hours=duration_hours),
            "end_time": datetime.now() + timedelta(hours=duration_hours)
        }
    
    @staticmethod
    def get_traditional_crop_calendar(country: str, crop: str) -> Dict:
        """Get traditional crop calendar for specific country and crop."""
        calendars = {
            "Nigeria": {
                "White Yam": {
                    "planting": {"start": "April", "end": "June"},
                    "harvest": {"start": "December", "end": "February"}
                },
                "Cassava": {
                    "planting": {"start": "April", "end": "July"},
                    "harvest": {"start": "12 months", "end": "18 months"}
                }
            }
        }
        return calendars.get(country, {}).get(crop, {})

@pytest.fixture
def african_test_utils():
    """African agricultural testing utilities."""
    return AfricanTestUtils()

# Async test utilities
@pytest.fixture
async def async_db_session():
    """Async database session for testing."""
    # Mock async database session
    session = AsyncMock()
    session.add = Mock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    session.execute = AsyncMock()
    session.scalar = AsyncMock()
    return session

@pytest.fixture
def mock_external_apis():
    """Mock external APIs for testing."""
    return {
        "weather_api": Mock(),
        "market_price_api": Mock(),
        "mobile_money_api": Mock(),
        "translation_api": Mock(),
        "geolocation_api": Mock()
    }

# Performance testing fixtures
@pytest.fixture
def load_test_scenarios():
    """Load testing scenarios for African contexts."""
    return {
        "concurrent_farmers": [10, 50, 100, 500, 1000],
        "data_sync_load": ["light", "medium", "heavy"],
        "network_conditions": ["2G", "3G", "4G", "WiFi"],
        "device_types": ["smartphone", "feature_phone", "tablet"]
    }

# Cultural testing fixtures
@pytest.fixture
def cultural_validation_data():
    """Cultural validation data for testing."""
    return {
        "traditional_titles": {
            "Nigeria": ["Eze", "Obi", "Emir", "Oba"],
            "Kenya": ["Chief", "Elder", "Mzee"],
            "Ghana": ["Nana", "Chief", "Odikro"]
        },
        "cultural_practices": {
            "blessing_ceremonies": True,
            "community_planting": True,
            "harvest_festivals": True,
            "traditional_timing": True
        },
        "taboos_and_restrictions": {
            "planting_days": ["certain market days"],
            "harvest_restrictions": ["mourning periods"],
            "gender_roles": ["context_specific"]
        }
    }

# Mark all fixtures as available for all test modules
pytest_plugins = []

