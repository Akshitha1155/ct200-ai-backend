from app.services.extractor import extract_spans


def parse_document(pdf_path):
    """
    Main parser pipeline.

    Currently:
        PDF -> Extract Spans

    Later:
        PDF -> Extract Spans
            -> Classify Headings
            -> Build Hierarchy
            -> Generate Document Nodes
            -> Compute Hashes
    """

    spans = extract_spans(pdf_path)

    return spans