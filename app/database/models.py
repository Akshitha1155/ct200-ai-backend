from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime,
    Boolean
)
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
    
    qa_pairs = relationship(
    "QuestionAnswer",
    back_populates="section",
    cascade="all, delete")
    
class QuestionAnswer(Base):
    __tablename__ = "question_answers"

    id = Column(Integer, primary_key=True, index=True)

    section_id = Column(
        Integer,
        ForeignKey("document_sections.id")
    )

    question = Column(Text)

    answer = Column(Text)

    is_stale = Column(
    Boolean,
    default=False)
    
    section = relationship(
    "DocumentSection",
    back_populates="qa_pairs"
)