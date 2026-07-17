from app.services.llm import generate_qa

result = generate_qa(
    "1.1 Intended Use",
    "The CT-200 is intended to measure blood pressure and pulse rate in adults."
)

print(result)