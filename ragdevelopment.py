text = """
Artificial intelligence is changing education. 
AI tutors can provide personalized explanations to students. 

Machine learning allows computers to learn patterns from data. 
Teachers remain important because they provide human guidance. 

Students can use AI to understand difficult topics more easily.
"""

paragraphs = text.strip().split("\n\n")
#words = text.split()
chunk_size = 20
overlap = 5
step = chunk_size - overlap
chunks = []
current_chunk = []
for paragraph in paragraphs:
    paragraph_words = paragraph.split()

current_chunk.extend(paragraph_words)

if len(current_chunk) >= chunk_size:
    chunks.append(" ".join(current_chunk))

current_chunk = current_chunk[-overlap:]
"""
for i in range(0, len(words), step):
    chunk = words[i:i + chunk_size]
    chunks.append(" ".join(chunk))
"""
for number, chunk in enumerate(chunks, start = 1):
    print(f"Chunk {number}:")
    print(chunk)
    print()
 