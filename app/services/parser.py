from app.services.extractor import extract_spans
from app.services.merger import merge_spans
from app.services.classifier import classify_span
from app.services.hierarchy import build_hierarchy
from app.services.serializer import node_to_dict
from app.services.hashing import hash_document

def parse_document(pdf_path):
    """
    Complete parser pipeline.

    PDF
      ↓
    Extract Spans
      ↓
    Merge Related Spans
      ↓
    Classify
    """

    spans = extract_spans(pdf_path)

    merged_spans = merge_spans(spans)

    classified_spans = []

    for span in merged_spans:

        span["type"] = classify_span(span)

        classified_spans.append(span)
        
    document_tree = build_hierarchy(classified_spans)
    
    hash_document(document_tree)

    return document_tree