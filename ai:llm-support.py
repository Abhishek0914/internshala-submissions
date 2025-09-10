from openai import OpenAI

client = OpenAI()

def classify_with_llm(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or other suitable model
        messages=[
            {"role": "system", "content": "Classify the question as factual, opinion, or math."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content.strip().lower()
