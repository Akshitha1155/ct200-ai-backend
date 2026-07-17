from app.database.database import SessionLocal
from app.database.models import DocumentSection, QuestionAnswer
from app.services.llm import generate_qa


def generate_qa_for_version(version_id):
    """
    Generate one QA pair for each document section in a version.
    """

    db = SessionLocal()

    try:
        # Fetch one non-empty section (for testing)
        sections = (
            db.query(DocumentSection)
            .filter(DocumentSection.version_id == version_id)
            .filter(DocumentSection.body != "")
            .all()
        )

        generated = 0

        for section in sections:

            # Skip empty body
            if not section.body or not section.body.strip():
                print("Skipped: Empty body")
                continue

            # Generate QA using Mistral
            response = generate_qa(
                section.heading,
                section.body
            )

            print(response)

            question = ""
            answer = ""

            # Parse response
            for line in response.splitlines():

                line = line.strip()

                if line.lower().startswith("question:"):
                    question = line[len("Question:"):].strip()

                elif line.lower().startswith("answer:"):
                    answer = line[len("Answer:"):].strip()


            if question and answer:

                qa = QuestionAnswer(
                    section_id=section.id,
                    question=question,
                    answer=answer,
                    is_stale=False
                )

                db.add(qa)
                generated += 1

                print("QA Saved Successfully!")

            else:
                print("Failed to parse QA.")

        db.commit()

        return {
            "generated": generated
        }

    except Exception as e:
        db.rollback()
        print("ERROR:", str(e))
        return {
            "error": str(e)
        }

    finally:
        db.close()