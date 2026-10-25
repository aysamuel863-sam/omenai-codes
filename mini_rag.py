import os
from openai import OpenAI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
print(f"Key exists: {os.getenv("NVIDIA_API_KEY")}")
client = OpenAI(
    base_url = "https://integrate/api.nvidia.com/v1",
    api_key = os.getenv("NVIDIA_API_KEY")
)
"""
documents = [
    "Python is a popular programming language used in artificial intelligence, automation, web development, and data science.",
    "Machine learning is a branch of artificial intelligence where computers learn patterns from data.",
    "SQL is a language used to communicaated with relational databases and retrieve structured information.",
    "Large language models process text as tokens and can perform tasks such as summarization, question answering and rewriting.",
    "Embeddings represent text as numerical vectors that can be compared for semantic similarity."
]

while True:
    vectorizer = TfidfVectorizer()
    document_vectors = vectorizer.fit_transform(documents)

    question = input("Ask a question: ")
    if question == "exit":
        break
    question_vector = vectorizer.transform([question])
    similarities = cosine_similarity(question_vector, document_vectors)
    best_index = similarities.argmax()
    best_document = documents[best_index]
    print("\nRetrieved information:")
    print(best_document)

prompt = f
You are a helpful general-purpose AI assistant.
Retrieved Context:
{best_document}
User Question:
{question}
Use the context when it is relevant to the question.
You can also use your general knowledge to answer.
Do not assume the context is the only source of information.
response = client.chat.completions.create(
    model = "nvidia/nemotron-3-super-120b-a12b",
    messages = [{
        "role": "user",
        "content": prompt
    }],
    max_tokens = 500
)

answer = response.choice[0].message.content

print("\nAI:")
print(answer)
text = "Python is useful for artificial intelligence."
"""
try:
    response = client.embeddings.create(
        model = "nvidia/nemotron-3-embed-1b",
        input = ["Python is useful for AI."],
        extra_body = {
            "input_type": "passage",
            "modality": "text"
        }
        #input_type = "passage"
    )
    embedding = response.data[0].embedding
    print("Embedding created!")
    print(f"Number of values: {len(embedding)}")
    print(f"First 10 values: {embedding[:10]}")
except Exception as e:
    print("ERROR:")
    print(type(e).__name__)
    print(e)