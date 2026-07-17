from app.models.document_node import DocumentNode


def node_to_dict(node: DocumentNode):
    """
    Convert a DocumentNode tree into a JSON-serializable dictionary.
    """

    return {
        "heading": node.heading,
        "level": node.level,
        "body": node.body,
        "page_number": node.page_number,
        "children": [
            node_to_dict(child)
            for child in node.children
        ]
    }