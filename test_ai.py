from ai.ollama_client import generate_ai_response

print("Sending request to Ollama...\n")

response = generate_ai_response(
    "Explain Cloud Computing in one short paragraph."
)

print("\nAI Response:\n")
print(response)