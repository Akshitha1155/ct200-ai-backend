from app.models.document_node import DocumentNode
from app.models.document_types import DocumentElementType


def get_level(element_type):
    """
    Convert document element type into hierarchy level.
    """

    if element_type == DocumentElementType.DOCUMENT_TITLE:
        return 0

    elif element_type == DocumentElementType.MAIN_HEADING:
        return 1

    elif element_type == DocumentElementType.SUB_HEADING:
        return 2

    elif element_type == DocumentElementType.SUB_SUB_HEADING:
        return 3

    return -1


def build_hierarchy(spans):
    """
    Build a document tree from classified spans.
    """

    root = None
    stack = []

    for span in spans:

        span_type = span["type"]

        # -----------------------------
        # Heading / Title
        # -----------------------------
        if span_type != DocumentElementType.PARAGRAPH:

            level = get_level(span_type)

            node = DocumentNode(
                heading=span["text"],
                level=level,
                page_number=span["page"]
            )

            while stack and stack[-1].level >= level:
                stack.pop()

            if stack:
                node.parent = stack[-1]
                stack[-1].children.append(node)
            else:
                root = node

            stack.append(node)

        # -----------------------------
        # Paragraph
        # -----------------------------
        else:

            if stack:

                if stack[-1].body:
                    stack[-1].body += "\n\n"

                stack[-1].body += span["text"]

    return root