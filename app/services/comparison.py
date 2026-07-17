from app.database.database import SessionLocal
from app.database.models import DocumentSection


def compare_versions(version1_id, version2_id):
    """
    Compare two document versions using content hashes.
    """

    db = SessionLocal()

    try:
        sections_v1 = db.query(DocumentSection).filter(
            DocumentSection.version_id == version1_id
        ).all()

        sections_v2 = db.query(DocumentSection).filter(
            DocumentSection.version_id == version2_id
        ).all()

        map_v1 = {section.heading: section for section in sections_v1}
        map_v2 = {section.heading: section for section in sections_v2}

        added = []
        removed = []
        modified = []

        # Added & Modified
        for heading, section in map_v2.items():

            if heading not in map_v1:
                added.append(heading)

            elif section.content_hash != map_v1[heading].content_hash:
                modified.append(heading)

        # Removed
        for heading in map_v1:

            if heading not in map_v2:
                removed.append(heading)

        return {
            "added": added,
            "removed": removed,
            "modified": modified,
        }

    finally:
        db.close()