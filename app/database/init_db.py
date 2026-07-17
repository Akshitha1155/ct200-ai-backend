from app.database.database import Base, engine
from app.database.models import Document, DocumentVersion, DocumentSection


def init_db():
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully!")