from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://postgres:password@db/postgres"

engine = create_engine(DATABASE_URL)

# Dependency that provides a database session
def get_db():
    with Session(engine) as session:
        yield session
