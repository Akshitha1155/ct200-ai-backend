import re

from app.models.document_types import DocumentElementType


def is_bold(font_name: str) -> bool:
    """
    Returns True if the font appears to be bold.
    """
    return "bold" in font_name.lower()


def has_section_number(text: str) -> bool:
    """
    Detects section numbers like:
    1.
    1.1
    2.3.4
    2.1.1.1
    """

    pattern = r'^\d+(\.\d+)*\.?'

    return re.match(pattern, text.strip()) is not None

def get_section_level(text: str):
    """
    Returns the depth of the section number.

    Examples:
    1           -> 1
    1.1         -> 2
    2.1.1       -> 3
    2.1.1.1     -> 4
    """

    match = re.match(r'^(\d+(?:\.\d+)*)', text.strip())

    if not match:
        return 0

    number = match.group(1)

    return len(number.split("."))
def classify_span(span):
    """
    Classify a single merged span.
    """

    text = span["text"]
    font = span["font"]
    font_size = span["font_size"]
    page = span["page"]

    # -----------------------------
    # Rule 1: Document Title
    # -----------------------------
    if (
        page == 1
        and is_bold(font)
        and font_size >= 20
        and not has_section_number(text)
    ):
        return DocumentElementType.DOCUMENT_TITLE

    # -----------------------------
    # Rule 2: Numbered Headings
    # -----------------------------
    if has_section_number(text) and is_bold(font):

        level = get_section_level(text)

        if level == 1:
            return DocumentElementType.MAIN_HEADING

        elif level == 2:
            return DocumentElementType.SUB_HEADING

        else:
            return DocumentElementType.SUB_SUB_HEADING

    # -----------------------------
    # Rule 3: Paragraph
    # -----------------------------
    return DocumentElementType.PARAGRAPH