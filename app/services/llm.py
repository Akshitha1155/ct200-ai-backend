from ollama import chat
def generate_qa(section_heading, section_body):
    """
    Generate one question-answer pair from a document section.
    """

    prompt = f"""
You are an expert technical documentation assistant.

Generate exactly ONE question and ONE answer from the following section.

Heading:
{section_heading}

Content:
{section_body}

Return ONLY in this format:

Question: ...
Answer: ...
"""

    response = chat(
        model="mistral:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]