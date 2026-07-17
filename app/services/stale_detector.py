from app.database.database import SessionLocal
from app.database.models import DocumentSection, QuestionAnswer
from app.services.comparison import compare_versions


def mark_stale_qas(old_version_id, new_version_id):
    """
    Mark QA pairs as stale when a section changes
    between two document versions.
    """

    db = SessionLocal()

    try:
        comparison = compare_versions(old_version_id, new_version_id)

        modified = comparison["modified"]

        stale_count = 0

        for heading in modified:

            section = (
                db.query(DocumentSection)
                .filter(
                    DocumentSection.version_id == old_version_id,
                    DocumentSection.heading == heading
                )
                .first()
            )

            if section is None:
                continue

            qa_pairs = (
                db.query(QuestionAnswer)
                .filter(
                    QuestionAnswer.section_id == section.id
                )
                .all()
            )

            for qa in qa_pairs:
                qa.is_stale = True
                stale_count += 1

        db.commit()

        return {
            "modified_sections": len(modified),
            "qa_marked_stale": stale_count
        }

    finally:
        db.close()