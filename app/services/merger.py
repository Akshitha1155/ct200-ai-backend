def merge_spans(spans):
    """
    Merge consecutive spans that belong to the same logical text block.
    """

    if not spans:
        return []

    merged = []
    current = spans[0].copy()

    for span in spans[1:]:

        same_page = current["page"] == span["page"]

        same_font = current["font"] == span["font"]

        same_size = abs(current["font_size"] - span["font_size"]) < 0.1

        current_bottom = current["bbox"][3]
        next_top = span["bbox"][1]

        close_vertically = abs(next_top - current_bottom) < 15

        if same_page and same_font and same_size and close_vertically:

            current["text"] += " " + span["text"]

            current["bbox"] = (
                current["bbox"][0],
                current["bbox"][1],
                max(current["bbox"][2], span["bbox"][2]),
                span["bbox"][3],
            )

        else:

            merged.append(current)

            current = span.copy()

    merged.append(current)

    return merged