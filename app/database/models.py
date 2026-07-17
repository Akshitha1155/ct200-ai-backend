from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    versions = relationship(
        "DocumentVersion",
        back_populates="document",
        cascade="all, delete"
    )


class DocumentVersion(Base):
    __tablename__ = "document_versions"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    version_name = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    document = relationship(
        "Document",
        back_populates="versions"
    )

    sections = relationship(
        "DocumentSection",
        back_populates="version",
        cascade="all, delete"
    )


class DocumentSection(Base):
    __tablename__ = "document_sections"

    id = Column(Integer, primary_key=True, index=True)

    version_id = Column(
        Integer,
        ForeignKey("document_versions.id")
    )

    heading = Column(String)
    level = Column(Integer)

    body = Column(Text)

    content_hash = Column(String)

    page_number = Column(Integer)

    parent_heading = Column(String)

    version = relationship(
        "DocumentVersion",
        back_populates="sections"
    )