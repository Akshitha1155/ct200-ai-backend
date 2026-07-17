from fastapi import FastAPI

from app.services.extractor import inspect_pdf
from app.services.parser import parse_document
from app.services.serializer import node_to_dict
from app.services.storage import save_document_tree

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
        document_name="CT-200 Manual",
        version_name="v1"
    )

    return node_to_dict(document_tree)