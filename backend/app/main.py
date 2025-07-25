"""
WebWaka Agriculture & Food Security Sector - Main Application

This is the main entry point for the WebWaka Agriculture sector backend API.
Designed for African agricultural transformation with offline-first capabilities,
multi-language support, and mobile-optimized performance.

Author: WebWaka Development Team
Version: 1.0.0
License: MIT
"""

import logging
import time
from contextlib import asynccontextmanager
from typing import Any, Dict

import structlog
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from prometheus_client import Counter, Histogram, generate_latest
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.database import engine, create_tables
from app.core.logging import setup_logging
from app.core.security import setup_security_headers
from app.utils.health import health_check
from app.utils.metrics import setup_metrics

# Setup structured logging
setup_logging()
logger = structlog.get_logger(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter(
    'webwaka_agriculture_requests_total',
    'Total number of HTTP requests',
    ['method', 'endpoint', 'status_code']
)

REQUEST_DURATION = Histogram(
    'webwaka_agriculture_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

ACTIVE_CONNECTIONS = Counter(
    'webwaka_agriculture_active_connections',
    'Number of active connections'
)


class MetricsMiddleware(BaseHTTPMiddleware):
    """Middleware for collecting Prometheus metrics."""
    
    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = time.time()
        
        # Track active connections
        ACTIVE_CONNECTIONS.inc()
        
        try:
            response = await call_next(request)
            
            # Record metrics
            REQUEST_COUNT.labels(
                method=request.method,
                endpoint=request.url.path,
                status_code=response.status_code
            ).inc()
            
            REQUEST_DURATION.labels(
                method=request.method,
                endpoint=request.url.path
            ).observe(time.time() - start_time)
            
            return response
            
        except Exception as e:
            REQUEST_COUNT.labels(
                method=request.method,
                endpoint=request.url.path,
                status_code=500
            ).inc()
            
            logger.error(
                "Request failed",
                method=request.method,
                path=request.url.path,
                error=str(e)
            )
            raise
            
        finally:
            ACTIVE_CONNECTIONS.dec()


class AfricanOptimizationMiddleware(BaseHTTPMiddleware):
    """Middleware for African infrastructure optimizations."""
    
    async def dispatch(self, request: Request, call_next) -> Response:
        # Add African-specific headers
        request.state.african_context = {
            "bandwidth_aware": True,
            "offline_capable": True,
            "mobile_optimized": True
        }
        
        # Check for offline mode header
        if request.headers.get("X-Offline-Mode") == "true":
            request.state.offline_mode = True
        
        # Add compression for mobile networks
        response = await call_next(request)
        
        # Add African optimization headers
        response.headers["X-African-Optimized"] = "true"
        response.headers["X-Offline-Capable"] = "true"
        response.headers["X-Mobile-First"] = "true"
        
        return response


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    logger.info("Starting WebWaka Agriculture API")
    
    # Create database tables
    await create_tables()
    
    # Setup metrics
    setup_metrics()
    
    logger.info("WebWaka Agriculture API started successfully")
    yield
    
    logger.info("Shutting down WebWaka Agriculture API")


# Create FastAPI application
app = FastAPI(
    title="WebWaka Agriculture & Food Security API",
    description="""
    Comprehensive API for African agricultural digital transformation.
    
    ## Features
    
    * **Offline-First**: Complete functionality without internet connection
    * **Mobile-Optimized**: Designed for smartphones and feature phones
    * **Multi-Language**: Support for 8 major African languages
    * **Cultural Integration**: Respects traditional farming practices
    * **Community-Focused**: Supports cooperative and community farming
    
    ## African Optimizations
    
    * **Low-Bandwidth**: Optimized for 2G/3G networks
    * **Power-Aware**: Battery optimization for limited power
    * **Geospatial**: Advanced mapping for African agriculture
    * **Weather Integration**: Local weather data and forecasting
    * **Market Access**: Integration with local and regional markets
    
    ## Modules
    
    The API provides access to 47 agricultural modules organized in biological architecture:
    
    * **User Management** (8 modules): Authentication, profiles, communities
    * **Farm Management** (12 modules): Farms, plots, resources, analytics
    * **Production Management** (15 modules): Crops, livestock, monitoring
    * **Market Access** (8 modules): Prices, trading, payments, logistics
    * **Advisory Services** (4 modules): Extension, weather, training
    """,
    version="1.0.0",
    contact={
        "name": "WebWaka Agriculture Team",
        "email": "agriculture@webwaka.africa",
        "url": "https://webwaka.africa/agriculture"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan
)

# Security middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)

# CORS middleware for African domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["X-African-Optimized", "X-Offline-Capable", "X-Mobile-First"]
)

# Compression middleware for mobile networks
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Custom middleware
app.add_middleware(MetricsMiddleware)
app.add_middleware(AfricanOptimizationMiddleware)


@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """Add security headers to all responses."""
    response = await call_next(request)
    return setup_security_headers(response)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests with structured logging."""
    start_time = time.time()
    
    logger.info(
        "Request started",
        method=request.method,
        path=request.url.path,
        client_ip=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent"),
        offline_mode=getattr(request.state, 'offline_mode', False)
    )
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    
    logger.info(
        "Request completed",
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        process_time=process_time
    )
    
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Include API routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Root"])
async def root() -> Dict[str, Any]:
    """Root endpoint with API information."""
    return {
        "message": "WebWaka Agriculture & Food Security API",
        "version": "1.0.0",
        "status": "operational",
        "african_optimized": True,
        "offline_capable": True,
        "mobile_first": True,
        "documentation": "/docs",
        "health_check": "/health",
        "metrics": "/metrics"
    }


@app.get("/health", tags=["Health"])
async def health() -> Dict[str, Any]:
    """Health check endpoint for monitoring."""
    return await health_check()


@app.get("/metrics", tags=["Monitoring"])
async def metrics():
    """Prometheus metrics endpoint."""
    return Response(
        generate_latest(),
        media_type="text/plain"
    )


@app.get("/info", tags=["Information"])
async def info() -> Dict[str, Any]:
    """API information and capabilities."""
    return {
        "api": {
            "name": "WebWaka Agriculture API",
            "version": "1.0.0",
            "environment": settings.ENVIRONMENT
        },
        "features": {
            "offline_first": True,
            "mobile_optimized": True,
            "multi_language": True,
            "african_optimized": True,
            "geospatial": True,
            "real_time": True
        },
        "modules": {
            "user_management": 8,
            "farm_management": 12,
            "production_management": 15,
            "market_access": 8,
            "advisory_services": 4,
            "total": 47
        },
        "languages": [
            "en", "fr", "ar", "sw", "ha", "yo", "am", "zu"
        ],
        "regions": [
            "West Africa", "East Africa", "Central Africa", 
            "North Africa", "Southern Africa"
        ]
    }


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler with structured logging."""
    logger.error(
        "Unhandled exception",
        method=request.method,
        path=request.url.path,
        error=str(exc),
        error_type=type(exc).__name__
    )
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred",
            "request_id": getattr(request.state, 'request_id', None)
        }
    )


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.ENVIRONMENT == "development",
        log_config=None  # Use our custom logging
    )

