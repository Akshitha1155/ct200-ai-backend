import fitz
def inspect_pdf(pdf_path):
 
    document = fitz.open(pdf_path)

    for page_number, page in enumerate(document):

        print(f"\n========== PAGE {page_number + 1} ==========\n")

        blocks = page.get_text("dict")["blocks"]

        for block in blocks:

            if "lines" not in block:
                continue

            for line in block["lines"]:

                for span in line["spans"]:

                    print(f"Text: {span['text']}")
                    print(f"Font Size: {span['size']}")
                    print(f"Font: {span['font']}")
                    print("-" * 40)

    document.close()


def extract_spans(pdf_path):
    """
    Extract all text spans along with formatting metadata.
    """

    document = fitz.open(pdf_path)

    spans = []

    for page_number, page in enumerate(document):

        blocks = page.get_text("dict")["blocks"]

        for block in blocks:

            if "lines" not in block:
                continue

            for line in block["lines"]:

                for span in line["spans"]:

                    text = span["text"].strip()

                    if not text:
                        continue

                    spans.append({
                        "text": text,
                        "font_size": span["size"],
                        "font": span["font"],
                        "page": page_number + 1,
                        "bbox": span["bbox"]
                    })

    document.close()

    return spans