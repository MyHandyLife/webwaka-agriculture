# WebWaka Agriculture API Documentation

**Version 1.0 | African-Optimized Agricultural Platform**

## Table of Contents

1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [African Context Integration](#african-context-integration)
4. [User Management API](#user-management-api)
5. [Farm Management API](#farm-management-api)
6. [Production Management API](#production-management-api)
7. [Market Access API](#market-access-api)
8. [Advisory Services API](#advisory-services-api)
9. [Cultural Adaptation API](#cultural-adaptation-api)
10. [Offline Synchronization](#offline-synchronization)
11. [Error Handling](#error-handling)
12. [Rate Limiting](#rate-limiting)
13. [SDK and Libraries](#sdk-and-libraries)

## Introduction

The WebWaka Agriculture API is designed specifically for African agricultural systems, incorporating traditional knowledge, cultural practices, and infrastructure realities. This RESTful API provides comprehensive access to all platform features while maintaining optimal performance for African network conditions.

### Base URLs

**Production Environments:**
- West Africa: `https://api-west.webwaka.africa/v1`
- East Africa: `https://api-east.webwaka.africa/v1`
- Southern Africa: `https://api-south.webwaka.africa/v1`

**Staging Environment:**
- `https://api-staging.webwaka.africa/v1`

### African Infrastructure Optimizations

The API is optimized for African infrastructure with the following features:

- **Bandwidth Optimization:** Compressed responses with optional field selection
- **Offline Support:** Batch operations and conflict resolution
- **Mobile-First:** Optimized for smartphone and feature phone access
- **Cultural Adaptation:** Multi-language support and traditional knowledge integration
- **Network Resilience:** Intelligent retry mechanisms and graceful degradation

### API Design Principles

1. **African-Centered:** Designed for African farmers, cooperatives, and agricultural systems
2. **Traditional Knowledge Integration:** Respects and incorporates indigenous practices
3. **Mobile-Optimized:** Efficient for 2G/3G networks and limited data plans
4. **Offline-Capable:** Supports offline operations with intelligent synchronization
5. **Culturally Sensitive:** Adapts to local languages, customs, and practices
6. **Community-Focused:** Enables collaboration and knowledge sharing

## Authentication

WebWaka Agriculture uses phone-based authentication optimized for African mobile networks.

### Phone-Based Authentication

African farmers primarily use mobile phones, so our authentication system is built around phone numbers rather than email addresses.

```http
POST /auth/register
Content-Type: application/json

{
  "phone_number": "+234801234567",
  "country_code": "NG",
  "language": "en",
  "traditional_name": "Eze Ubi",
  "village": "Umuahia",
  "ethnic_group": "Igbo"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Verification code sent",
  "verification_id": "ver_abc123",
  "expires_in": 300
}
```

### Verification

```http
POST /auth/verify
Content-Type: application/json

{
  "verification_id": "ver_abc123",
  "code": "123456"
}
```

**Response:**
```json
{
  "status": "success",
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "rt_def456",
  "expires_in": 3600,
  "user": {
    "id": "user_789",
    "phone_number": "+234801234567",
    "traditional_name": "Eze Ubi",
    "village": "Umuahia",
    "verified": true
  }
}
```

### Token Refresh

```http
POST /auth/refresh
Content-Type: application/json
Authorization: Bearer {refresh_token}

{
  "refresh_token": "rt_def456"
}
```

### Cultural Authentication Features

- **Traditional Names:** Support for traditional titles and names
- **Community Verification:** Village elders can verify farmer identities
- **Multi-Language:** Authentication messages in 8 African languages
- **Offline Capability:** Authentication tokens work offline for 7 days

## African Context Integration

The API includes comprehensive African context integration to ensure cultural relevance and practical applicability.

### Supported Countries and Regions

```http
GET /context/countries
```

**Response:**
```json
{
  "countries": [
    {
      "code": "NG",
      "name": "Nigeria",
      "regions": ["North", "Middle Belt", "South"],
      "languages": ["en", "ha", "yo", "ig"],
      "currencies": ["NGN"],
      "agricultural_zones": [
        {
          "name": "Guinea Savanna",
          "crops": ["maize", "yam", "cassava"],
          "seasons": ["wet", "dry"]
        }
      ]
    }
  ]
}
```

### Traditional Knowledge Database

```http
GET /context/traditional-knowledge
```

**Response:**
```json
{
  "practices": [
    {
      "id": "tk_001",
      "name": "Moon Phase Planting",
      "description": "Planting crops according to lunar cycles",
      "regions": ["West Africa", "East Africa"],
      "crops": ["yam", "cassava", "maize"],
      "cultural_groups": ["Yoruba", "Igbo", "Akan"]
    }
  ]
}
```

### Cultural Calendars

```http
GET /context/cultural-calendar/{country_code}
```

**Response:**
```json
{
  "calendar": {
    "country": "Nigeria",
    "seasons": [
      {
        "name": "Harmattan",
        "start_month": 11,
        "end_month": 2,
        "activities": ["land_preparation", "dry_season_farming"],
        "traditional_indicators": ["dry_winds", "dust_haze"]
      }
    ],
    "festivals": [
      {
        "name": "New Yam Festival",
        "month": 8,
        "significance": "Celebration of yam harvest",
        "farming_activities": ["yam_harvest", "thanksgiving"]
      }
    ]
  }
}
```

## User Management API

The User Management API handles farmer profiles, community connections, and role-based access control with African cultural integration.

### User Profile Management

#### Get User Profile

```http
GET /users/profile
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "user": {
    "id": "user_789",
    "phone_number": "+234801234567",
    "traditional_name": "Eze Ubi",
    "english_name": "John Okafor",
    "village": "Umuahia",
    "local_government": "Umuahia North",
    "state": "Abia",
    "country": "Nigeria",
    "ethnic_group": "Igbo",
    "languages": ["ig", "en"],
    "farming_experience_years": 15,
    "primary_crops": ["yam", "cassava", "plantain"],
    "farm_size_hectares": 2.5,
    "traditional_title": "Eze Ubi",
    "community_role": "Village Farmer",
    "verification_status": "community_verified",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-20T14:45:00Z"
  }
}
```

#### Update User Profile

```http
PUT /users/profile
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "traditional_name": "Eze Ubi Ukwu",
  "farming_experience_years": 16,
  "primary_crops": ["yam", "cassava", "plantain", "cocoyam"],
  "traditional_practices": [
    {
      "practice": "crop_rotation",
      "description": "Three-year rotation with fallow period",
      "inherited_from": "grandfather"
    }
  ]
}
```

### Community Integration

#### Join Village Community

```http
POST /users/communities/village
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "village_name": "Umuahia",
  "traditional_authority": "Eze Umuahia",
  "community_role": "Farmer",
  "verification_request": true
}
```

#### Get Community Members

```http
GET /users/communities/village/members
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "community": {
    "name": "Umuahia Village",
    "total_members": 45,
    "farmers": 38,
    "extension_agents": 2,
    "traditional_authorities": 1,
    "members": [
      {
        "id": "user_790",
        "traditional_name": "Mama Ngozi",
        "role": "Senior Farmer",
        "crops": ["cassava", "vegetables"],
        "experience_years": 25,
        "verification_status": "elder_verified"
      }
    ]
  }
}
```

### Cooperative Management

#### Join Cooperative

```http
POST /users/cooperatives/join
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "cooperative_id": "coop_123",
  "membership_type": "full",
  "contribution_amount": 5000,
  "currency": "NGN"
}
```

#### Get Cooperative Information

```http
GET /users/cooperatives/{cooperative_id}
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "cooperative": {
    "id": "coop_123",
    "name": "Umuahia Farmers Cooperative",
    "registration_number": "RC123456",
    "total_members": 120,
    "established_year": 2018,
    "primary_activities": ["input_supply", "marketing", "credit"],
    "leadership": {
      "chairman": "Chief Emeka Okafor",
      "secretary": "Mrs. Ada Nwankwo",
      "treasurer": "Mr. Chidi Okoro"
    },
    "services": [
      {
        "service": "Input Supply",
        "description": "Bulk purchase of seeds and fertilizers",
        "discount_rate": 15
      }
    ]
  }
}
```

## Farm Management API

The Farm Management API handles farm registration, plot management, and resource tracking with traditional land tenure support.

### Farm Registration

#### Register New Farm

```http
POST /farms
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Ezi Ubi Farm",
  "location": {
    "latitude": 5.5288,
    "longitude": 7.4951,
    "address": "Near the big iroko tree, Umuahia",
    "traditional_landmarks": ["iroko_tree", "old_market_path"]
  },
  "size_hectares": 2.5,
  "land_tenure": {
    "type": "family_land",
    "traditional_authority": "Eze Umuahia",
    "inheritance_type": "patrilineal",
    "documentation": "traditional_agreement"
  },
  "soil_type": "loamy",
  "water_sources": ["seasonal_stream", "rainwater"],
  "established_year": 2010
}
```

**Response:**
```json
{
  "farm": {
    "id": "farm_456",
    "name": "Ezi Ubi Farm",
    "owner_id": "user_789",
    "registration_status": "registered",
    "traditional_approval": "pending",
    "created_at": "2024-01-20T15:30:00Z"
  }
}
```

### Plot Management

#### Add New Plot

```http
POST /farms/{farm_id}/plots
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Yam Plot by the Stream",
  "size_hectares": 0.8,
  "boundaries": {
    "north": "Stream",
    "south": "Path to market",
    "east": "Neighbor's cassava farm",
    "west": "Old palm tree"
  },
  "soil_characteristics": {
    "type": "sandy_loam",
    "fertility": "high",
    "drainage": "well_drained",
    "traditional_assessment": "good_for_yam"
  },
  "current_crop": "yam",
  "crop_variety": "white_yam_ubi_ocha",
  "planting_date": "2024-03-15",
  "expected_harvest": "2024-12-15"
}
```

#### Get Plot Information

```http
GET /farms/{farm_id}/plots/{plot_id}
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "plot": {
    "id": "plot_789",
    "name": "Yam Plot by the Stream",
    "size_hectares": 0.8,
    "current_status": "planted",
    "crop_stage": "tuber_formation",
    "health_status": "healthy",
    "last_inspection": "2024-01-18T09:00:00Z",
    "traditional_indicators": {
      "leaf_color": "deep_green",
      "vine_growth": "vigorous",
      "soil_moisture": "adequate"
    },
    "modern_metrics": {
      "soil_ph": 6.2,
      "organic_matter": "3.2%",
      "nitrogen_level": "medium"
    }
  }
}
```

### Livestock Management

#### Register Livestock

```http
POST /farms/{farm_id}/livestock
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "animals": [
    {
      "traditional_name": "Ogbunigwe",
      "species": "goat",
      "breed": "west_african_dwarf",
      "gender": "male",
      "age_months": 18,
      "color": "brown_white",
      "identification_marks": "white_patch_on_forehead",
      "acquisition_date": "2023-06-15",
      "acquisition_method": "purchased",
      "cultural_significance": "for_traditional_ceremonies",
      "health_status": "healthy",
      "vaccination_status": "up_to_date"
    }
  ]
}
```

#### Track Animal Health

```http
POST /farms/{farm_id}/livestock/{animal_id}/health
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "observation_date": "2024-01-20",
  "health_status": "healthy",
  "traditional_assessment": {
    "appetite": "good",
    "activity_level": "active",
    "coat_condition": "shiny",
    "traditional_indicators": ["bright_eyes", "wet_nose"]
  },
  "veterinary_assessment": {
    "temperature": 39.2,
    "weight_kg": 25.5,
    "body_condition_score": 3.5
  },
  "treatments": [
    {
      "type": "traditional_medicine",
      "medicine": "neem_leaves",
      "purpose": "deworming",
      "dosage": "handful_daily",
      "duration_days": 7
    }
  ]
}
```

## Production Management API

The Production Management API tracks the complete agricultural production cycle, integrating traditional practices with modern monitoring.

### Planting Activities

#### Record Planting Activity

```http
POST /farms/{farm_id}/plots/{plot_id}/planting
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "crop": "yam",
  "variety": "white_yam_ubi_ocha",
  "planting_date": "2024-03-15",
  "planting_method": "traditional_mounds",
  "seed_source": "own_saved_seeds",
  "traditional_practices": {
    "moon_phase": "waxing_moon",
    "traditional_timing": "after_first_rains",
    "soil_preparation": "manual_clearing_and_mounding",
    "blessing_ceremony": "performed_by_elder"
  },
  "modern_practices": {
    "soil_testing": true,
    "improved_varieties": false,
    "fertilizer_application": "organic_compost"
  },
  "area_planted_hectares": 0.8,
  "seed_quantity_kg": 150,
  "expected_yield_kg": 2000,
  "labor_used": {
    "family_labor_days": 5,
    "hired_labor_days": 2,
    "community_labor_days": 3
  }
}
```

### Crop Monitoring

#### Record Crop Observation

```http
POST /farms/{farm_id}/plots/{plot_id}/observations
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "observation_date": "2024-05-20",
  "crop_stage": "vine_development",
  "traditional_assessment": {
    "overall_health": "very_good",
    "leaf_color": "deep_green",
    "vine_length": "reaching_stakes",
    "traditional_indicators": [
      "strong_vine_growth",
      "no_yellowing_leaves",
      "good_ground_cover"
    ]
  },
  "modern_assessment": {
    "plant_height_cm": 180,
    "leaf_area_index": 3.2,
    "chlorophyll_content": "high"
  },
  "pest_disease_status": {
    "pests_observed": ["yam_beetle"],
    "severity": "low",
    "traditional_control": "neem_spray",
    "modern_control": "none_needed"
  },
  "weather_conditions": {
    "rainfall_last_week_mm": 45,
    "temperature_avg_c": 28,
    "humidity_percent": 75
  }
}
```

### Harvest Management

#### Record Harvest Activity

```http
POST /farms/{farm_id}/plots/{plot_id}/harvest
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "harvest_date": "2024-12-15",
  "crop": "yam",
  "variety": "white_yam_ubi_ocha",
  "traditional_practices": {
    "harvest_timing": "after_vine_yellowing",
    "moon_phase": "waning_moon",
    "traditional_ceremony": "first_yam_ceremony",
    "elder_blessing": true
  },
  "harvest_results": {
    "total_yield_kg": 1850,
    "quality_grades": {
      "premium": 1200,
      "standard": 500,
      "processing": 150
    },
    "tuber_sizes": {
      "large": 800,
      "medium": 750,
      "small": 300
    }
  },
  "post_harvest_handling": {
    "curing_method": "traditional_barn_drying",
    "storage_method": "traditional_yam_barn",
    "expected_storage_months": 8
  },
  "labor_used": {
    "family_labor_days": 8,
    "hired_labor_days": 4,
    "community_labor_days": 6
  },
  "costs": {
    "labor_cost_ngn": 15000,
    "transport_cost_ngn": 5000,
    "storage_cost_ngn": 2000
  }
}
```

## Market Access API

The Market Access API connects farmers to buyers, provides market information, and facilitates transactions with mobile money integration.

### Market Information

#### Get Current Market Prices

```http
GET /markets/prices
Authorization: Bearer {access_token}
Query Parameters:
- crop: yam
- location: umuahia
- radius_km: 50
```

**Response:**
```json
{
  "market_prices": [
    {
      "market_name": "Umuahia Main Market",
      "distance_km": 5,
      "crop": "yam",
      "variety": "white_yam",
      "prices": {
        "wholesale_ngn_per_kg": 350,
        "retail_ngn_per_kg": 450,
        "premium_ngn_per_kg": 550
      },
      "demand_level": "high",
      "quality_requirements": {
        "size": "medium_to_large",
        "condition": "fresh_no_damage",
        "traditional_preferences": "white_flesh_preferred"
      },
      "last_updated": "2024-01-20T08:00:00Z"
    }
  ]
}
```

#### Get Buyer Contacts

```http
GET /markets/buyers
Authorization: Bearer {access_token}
Query Parameters:
- crop: yam
- location: umuahia
- buyer_type: wholesaler
```

**Response:**
```json
{
  "buyers": [
    {
      "id": "buyer_123",
      "name": "Chief Okoro Yam Trading",
      "type": "wholesaler",
      "location": "Umuahia Main Market",
      "contact_phone": "+234803456789",
      "crops_purchased": ["yam", "cassava", "plantain"],
      "payment_methods": ["cash", "mobile_money", "bank_transfer"],
      "minimum_quantity_kg": 500,
      "quality_requirements": {
        "grade": "premium_and_standard",
        "packaging": "jute_bags_preferred"
      },
      "reputation_score": 4.5,
      "verified_by_cooperative": true
    }
  ]
}
```

### Sales Management

#### Create Sale Listing

```http
POST /markets/listings
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "crop": "yam",
  "variety": "white_yam_ubi_ocha",
  "quantity_kg": 1000,
  "quality_grade": "premium",
  "price_per_kg_ngn": 400,
  "location": "Umuahia",
  "harvest_date": "2024-12-15",
  "available_from": "2024-12-20",
  "storage_location": "traditional_yam_barn",
  "packaging": "jute_bags_50kg",
  "payment_terms": ["cash_on_delivery", "mobile_money"],
  "delivery_options": ["farm_pickup", "market_delivery"],
  "contact_preference": "phone_call",
  "traditional_certification": "elder_verified_quality",
  "organic_status": "traditional_organic"
}
```

#### Record Sale Transaction

```http
POST /markets/transactions
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "listing_id": "listing_456",
  "buyer_id": "buyer_123",
  "quantity_sold_kg": 800,
  "price_per_kg_ngn": 400,
  "total_amount_ngn": 320000,
  "payment_method": "mobile_money",
  "payment_status": "completed",
  "delivery_method": "farm_pickup",
  "transaction_date": "2024-12-22",
  "quality_feedback": {
    "buyer_rating": 5,
    "buyer_comments": "Excellent quality yam, very satisfied"
  },
  "cooperative_commission_ngn": 16000,
  "transport_cost_ngn": 8000,
  "net_income_ngn": 296000
}
```

---

*This is a comprehensive sample of the API documentation. The full documentation includes detailed examples, error codes, rate limiting information, and SDK documentation for all supported programming languages.*

