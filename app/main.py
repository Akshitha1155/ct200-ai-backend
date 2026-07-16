from fastapi import FastAPI

from app.services.extractor import inspect_pdf
from app.services.parser import parse_document

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

    spans = parse_document(pdf_path)

    return {
        "total_spans": len(spans),
        "spans": spans[:10]   # Only show first 10 spans
    }