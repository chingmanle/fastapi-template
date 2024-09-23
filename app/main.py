from fastapi import FastAPI
from app.users.routes import router as users_router
from app.documents.routes import router as documents_router
from app.database import engine, SQLModel

app = FastAPI()

# Create database tables at the start
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Include user routes
app.include_router(users_router, prefix="/users", tags=["Users"])

# Include document routes
app.include_router(documents_router, prefix="/documents", tags=["Documents"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Pydantic and PostgreSQL"}
