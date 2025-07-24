
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = []
    for doc in docs:
        for chunk in splitter.split_text(doc["text"]):
            chunks.append({
                "text": chunk,
                "metadata": {"source": doc["file"]}
            })
    return chunks
            