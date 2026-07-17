from app.models.document_node import DocumentNode
def node_to_dict(node: DocumentNode):
    return {
        "heading": node.heading,
        "level": node.level,
        "body": node.body,
        "page_number": node.page_number,
        "content_hash": node.content_hash,
        "children": [
            node_to_dict(child)
            for child in node.children
        ]
    }