import pathlib
import sqlite3
from typing import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from api.main import app
from api.models.db_models import Base
# Ensure models are registered with Base before create_all
from api.models.db_models import bot_user_db, adk_session_db, contractor_db, agent_db
from api.dependencies.dependencies import get_contractor_repository
from api.repositories.alchemy_contractor_repository import AlchemyContractorRepository

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

@pytest.fixture(scope="session")
def sqlite_engine() -> Iterator:
    """
    Fixture to provide a SQLite database for easier testing.
    Test DB created once and used for all tests. After test run completes, SQLite test DB is torn down
    """
    db_path = REPO_ROOT / ".test-db.sqlite"
    
    # Why we set check_same_thread to False: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-an-engine
    engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False})
    
    # Create tables from SQLAlchemy models
    Base.metadata.create_all(engine)

    # Seed using raw SQL script adapted for SQLite
    seed_sql_path = REPO_ROOT / "sql" / "insert-data.sql"
    if seed_sql_path.exists():
        # Execute SQL statements in a transaction
        with engine.begin() as conn:
            # SQLite accepts the same timestamp literal format used in the seed
            sql_text = seed_sql_path.read_text(encoding="utf-8")
            # Split on semicolons while keeping simple (seed file is straightforward)
            for statement in [s.strip() for s in sql_text.split(";") if s.strip()]:
                conn.execute(text(statement))

    try:
        yield engine
    finally:
        # Drop all tables after test session
        Base.metadata.drop_all(engine)
        # Remove db file
        try:
            db_path.unlink(missing_ok=True)
        except Exception:
            pass


@pytest.fixture()
def sqlite_session(sqlite_engine):
    """
    Fixture to provide access to sqlite session for unit testing purposes
    
    After the test run completes, the session is closed and the database is torn down
    """
    TestingSessionLocal = sessionmaker(bind=sqlite_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture()
def client(sqlite_session):
    # Override FastAPI repositories to use SQLite-backed repository
    def override_repo():
        return AlchemyContractorRepository(sqlite_session)

    app.dependency_overrides[get_contractor_repository] = override_repo
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()


