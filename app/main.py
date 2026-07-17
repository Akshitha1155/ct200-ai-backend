from fastapi import FastAPI

from app.services.extractor import inspect_pdf
from app.services.parser import parse_document
from app.services.serializer import node_to_dict
from app.services.storage import save_document_tree
from app.services.comparison import compare_versions
from app.services.qa_generator import generate_qa_for_version
from app.services.stale_detector import mark_stale_qas

app = FastAPI(
    title="CT200 AI Backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "CT200 AI Backend is running successfully!"
    }


@app.get("/inspect")
def inspect():

    pdf_path = "data/ct200_manual.pdf"

    inspect_pdf(pdf_path)

    return {
        "message": "Inspection completed. Check the terminal."
    }
@app.get("/parse")
def parse():

    pdf_path = "data/ct200_manual.pdf"

    document_tree = parse_document(pdf_path)

    save_document_tree(
    document_tree,
    document_name="CT-200 Manual")

    return node_to_dict(document_tree)

@app.get("/compare")
def compare(version1: int, version2: int):

    result = compare_versions(version1, version2)

    return result

@app.post("/generate-qa")
def generate(version_id: int):

    return generate_qa_for_version(version_id)

@app.post("/mark-stale")
def mark_stale(old_version_id: int, new_version_id: int):
    return mark_stale_qas(old_version_id, new_version_id)