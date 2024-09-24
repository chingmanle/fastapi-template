from app.settings import settings
from sqlmodel import SQLModel, create_engine, Session

# Configure database from singleton setting
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)

# Dependency that provides a database session
def get_db():
    with Session(engine) as session:
        yield session
