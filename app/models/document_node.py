from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class DocumentNode:
    """
    Represents one section of the document.
    """

    heading: str
    level: int
    body: str = ""

    parent: Optional["DocumentNode"] = None

    children: List["DocumentNode"] = field(default_factory=list)

    page_number: int = 0

    content_hash: str = ""