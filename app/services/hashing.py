import hashlib

from app.models.document_node import DocumentNode


def generate_hash(text: str) -> str:
    """
    Generate SHA-256 hash for a string.
    """

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def hash_document(node: DocumentNode):
    """
    Recursively compute hashes for the document tree.
    """

    content = node.heading + "\n" + node.body

    node.content_hash = generate_hash(content)

    for child in node.children:
        hash_document(child)