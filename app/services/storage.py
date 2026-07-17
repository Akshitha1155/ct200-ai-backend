from app.database.database import SessionLocal
from app.database.models import (
    Document,
    DocumentVersion,
    DocumentSection,
)


def save_document_tree(root_node, document_name, version_name):
    """
    Save a parsed document tree into the database.
    """

    db = SessionLocal()

    try:
        # -----------------------------
        # Find or create document
        # -----------------------------
        document = (
            db.query(Document)
            .filter(Document.name == document_name)
            .first()
        )

        if document is None:
            document = Document(name=document_name)
            db.add(document)
            db.commit()
            db.refresh(document)

        # -----------------------------
        # Create version
        # -----------------------------
        version = DocumentVersion(
            document_id=document.id,
            version_name=version_name,
        )

        db.add(version)
        db.commit()
        db.refresh(version)

        # -----------------------------
        # Save sections recursively
        # -----------------------------
        save_node(db, version.id, root_node)

        db.commit()

    finally:
        db.close()


def save_node(db, version_id, node, parent_heading=None):
    """
    Recursively save one DocumentNode and its children.
    """

    section = DocumentSection(
        version_id=version_id,
        heading=node.heading,
        level=node.level,
        body=node.body,
        content_hash=node.content_hash,
        page_number=node.page_number,
        parent_heading=parent_heading,
    )

    db.add(section)

    for child in node.children:
        save_node(
            db,
            version_id,
            child,
            parent_heading=node.heading,
        )