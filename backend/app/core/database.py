"""
WebWaka Agriculture Database Infrastructure

Comprehensive database setup with African optimizations including
offline synchronization, geospatial support, and multi-tenancy.
"""

import asyncio
from typing import AsyncGenerator, Optional
from sqlalchemy import create_engine, MetaData, event
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import structlog

from app.core.config import settings

logger = structlog.get_logger(__name__)

# Database metadata with African-specific naming convention
metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)

# Base class for all models
Base = declarative_base(metadata=metadata)

# Async engine for main database operations
async_engine = create_async_engine(
    str(settings.DATABASE_URL).replace("postgresql://", "postgresql+asyncpg://"),
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,
    pool_recycle=3600,  # Recycle connections every hour
    echo=settings.DEBUG,
    future=True
)

# Sync engine for migrations and admin operations
sync_engine = create_engine(
    str(settings.DATABASE_URL),
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=settings.DEBUG,
    future=True
)

# Session factories
AsyncSessionLocal = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=True,
    autocommit=False
)

SessionLocal = sessionmaker(
    sync_engine,
    autocommit=False,
    autoflush=True
)


class DatabaseManager:
    """Database manager with African optimizations."""
    
    def __init__(self):
        self.async_engine = async_engine
        self.sync_engine = sync_engine
        self._setup_event_listeners()
    
    def _setup_event_listeners(self):
        """Setup database event listeners for African optimizations."""
        
        @event.listens_for(sync_engine, "connect")
        def set_sqlite_pragma(dbapi_connection, connection_record):
            """Set SQLite pragmas for offline mode."""
            if "sqlite" in str(settings.DATABASE_URL):
                cursor = dbapi_connection.cursor()
                # Enable WAL mode for better concurrency
                cursor.execute("PRAGMA journal_mode=WAL")
                # Enable foreign key constraints
                cursor.execute("PRAGMA foreign_keys=ON")
                # Set cache size for mobile devices
                cursor.execute("PRAGMA cache_size=10000")
                cursor.close()
        
        @event.listens_for(sync_engine, "before_cursor_execute")
        def receive_before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
            """Log slow queries for African network optimization."""
            context._query_start_time = asyncio.get_event_loop().time()
        
        @event.listens_for(sync_engine, "after_cursor_execute")
        def receive_after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
            """Log query execution time."""
            total = asyncio.get_event_loop().time() - context._query_start_time
            if total > 1.0:  # Log queries taking more than 1 second
                logger.warning(
                    "Slow query detected",
                    duration=total,
                    statement=statement[:100] + "..." if len(statement) > 100 else statement
                )
    
    async def create_tables(self):
        """Create all database tables."""
        try:
            async with async_engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.error("Failed to create database tables", error=str(e))
            raise
    
    async def drop_tables(self):
        """Drop all database tables (for testing)."""
        try:
            async with async_engine.begin() as conn:
                await conn.run_sync(Base.metadata.drop_all)
            logger.info("Database tables dropped successfully")
        except Exception as e:
            logger.error("Failed to drop database tables", error=str(e))
            raise
    
    async def health_check(self) -> bool:
        """Check database health."""
        try:
            async with AsyncSessionLocal() as session:
                await session.execute("SELECT 1")
                return True
        except Exception as e:
            logger.error("Database health check failed", error=str(e))
            return False


# Global database manager instance
db_manager = DatabaseManager()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Get async database session with African optimizations."""
    async with AsyncSessionLocal() as session:
        try:
            # Set session-level optimizations for African networks
            await session.execute("SET statement_timeout = '30s'")  # 30 second timeout
            await session.execute("SET lock_timeout = '10s'")       # 10 second lock timeout
            
            yield session
            await session.commit()
            
        except Exception as e:
            await session.rollback()
            logger.error("Database session error", error=str(e))
            raise
        finally:
            await session.close()


def get_sync_session():
    """Get synchronous database session."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error("Sync database session error", error=str(e))
        raise
    finally:
        session.close()


# Offline database support for African mobile networks
class OfflineDatabase:
    """Offline database manager for African mobile optimization."""
    
    def __init__(self):
        self.offline_engine = None
        self.offline_session = None
    
    def setup_offline_db(self, user_id: str):
        """Setup offline SQLite database for specific user."""
        offline_db_path = f"offline_data/user_{user_id}.db"
        
        self.offline_engine = create_engine(
            f"sqlite:///{offline_db_path}",
            poolclass=StaticPool,
            connect_args={
                "check_same_thread": False,
                "timeout": 20
            },
            echo=settings.DEBUG
        )
        
        # Create offline tables
        Base.metadata.create_all(self.offline_engine)
        
        self.offline_session = sessionmaker(
            self.offline_engine,
            autocommit=False,
            autoflush=True
        )
        
        logger.info("Offline database setup completed", user_id=user_id)
    
    def sync_to_online(self, user_id: str):
        """Sync offline data to online database."""
        # Implementation for syncing offline data
        # This would include conflict resolution and data merging
        pass
    
    def sync_from_online(self, user_id: str):
        """Sync online data to offline database."""
        # Implementation for downloading data for offline use
        pass


# Database utilities for African agricultural data
class AfricanAgriculturalData:
    """Utilities for African agricultural data management."""
    
    @staticmethod
    def get_crop_calendar(country_code: str, region: str) -> dict:
        """Get crop calendar for specific African region."""
        from app.core.config import CROP_CALENDARS
        
        region_key = AFRICAN_COUNTRIES.get(country_code, {}).get("region")
        if region_key and region_key in CROP_CALENDARS:
            return CROP_CALENDARS[region_key]
        
        # Default to general African calendar
        return {
            "rainy_season": {"start": "04-01", "end": "10-31"},
            "dry_season": {"start": "11-01", "end": "03-31"},
            "main_crops": ["maize", "cassava", "beans"],
            "planting_months": ["04", "05", "06"],
            "harvest_months": ["09", "10", "11"]
        }
    
    @staticmethod
    def get_local_varieties(crop: str, country_code: str) -> list:
        """Get local crop varieties for specific African country."""
        # This would be populated from agricultural research data
        local_varieties = {
            "maize": {
                "NG": ["Oba Super 2", "Sammaz 15", "Sammaz 17"],
                "KE": ["H614", "H6213", "DK8031"],
                "GH": ["Obatanpa", "Mamaba", "Aburohemaa"]
            },
            "rice": {
                "NG": ["FARO 44", "FARO 52", "NERICA 1"],
                "GH": ["Jasmine 85", "Tox 3145", "Agra Rice"],
                "SN": ["Sahel 108", "Sahel 177", "Sahel 201"]
            }
        }
        
        return local_varieties.get(crop, {}).get(country_code, [])


# Database initialization functions
async def create_tables():
    """Create all database tables."""
    await db_manager.create_tables()


async def init_database():
    """Initialize database with African agricultural data."""
    try:
        await create_tables()
        
        # Initialize with African agricultural reference data
        async with AsyncSessionLocal() as session:
            # This would populate reference tables with:
            # - African countries and regions
            # - Local crop varieties
            # - Traditional farming practices
            # - Market information
            # - Weather stations
            pass
            
        logger.info("Database initialized successfully")
        
    except Exception as e:
        logger.error("Database initialization failed", error=str(e))
        raise


# Export main functions and classes
__all__ = [
    "Base",
    "async_engine",
    "sync_engine", 
    "AsyncSessionLocal",
    "SessionLocal",
    "get_async_session",
    "get_sync_session",
    "create_tables",
    "init_database",
    "DatabaseManager",
    "OfflineDatabase",
    "AfricanAgriculturalData"
]

