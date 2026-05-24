import uuid

import chromadb
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection(
    name="documents"
)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def add_document_to_vector_db(text: str, filename: str = "uploaded_document") -> int:
    chunks = chunk_text(text)

    if not chunks:
        return 0

    embeddings = embedding_model.encode(chunks).tolist()

    ids = [
        f"{filename}_{uuid.uuid4()}"
        for _ in chunks
    ]

    metadatas = [
        {"source": filename, "chunk_index": i}
        for i in range(len(chunks))
    ]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    return len(chunks)


def retrieve_relevant_chunks(query: str, top_k: int = 3) -> list[str]:
    query_embedding = embedding_model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results.get("documents", [[]])

    if not documents or not documents[0]:
        return []

    return documents[0]