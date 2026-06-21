from app.database import (
    engine,
    Base
)

print("Removing existing tables...")

Base.metadata.drop_all(bind=engine)

print("Recreating tables...")

Base.metadata.create_all(bind=engine)

print("Database reset complete.")
