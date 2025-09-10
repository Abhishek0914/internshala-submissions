import re

def classify_question(question: str) -> str:
    """Classify question into factual, opinion, or math."""
    
    # Check if it looks like a math question (contains digits and operators)
    if re.search(r"\d+[\+\-\*/^%]|\d+\s*(plus|minus|times|divided by)", question.lower()):
        return "math"
    
    # Opinion indicators
    opinion_keywords = ["think", "feel", "opinion", "better", "like", "dislike", "prefer"]
    if any(word in question.lower() for word in opinion_keywords):
        return "opinion"
    
    # Default fallback
    return "factual"

def respond(question: str) -> str:
    """Generate response based on classification."""
    category = classify_question(question)
    
    if category == "math":
        try:
            # Extract mathematical expression safely
            expression = re.findall(r"[\d\+\-\*/\.\(\)\s]+", question)
            if expression:
                answer = eval("".join(expression))
                return f"Category: {category}\nAnswer: {answer}"
        except Exception:
            return f"Category: {category}\nI couldn’t calculate that."
    
    elif category == "opinion":
        return f"Category: {category}\nThat sounds subjective — what’s your view?"
    
    else:  # factual
        return f"Category: {category}\nI’d suggest checking reliable sources for the best answer."

# --- Example run ---
if __name__ == "__main__":
    user_question = input("Enter your question: ")
    print(respond(user_question))
