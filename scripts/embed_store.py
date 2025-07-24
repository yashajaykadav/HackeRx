
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

def embed_chunks(chunks):
    embeddings = OpenAIEmbeddings()
    documents = [Document(page_content=c["text"], metadata=c["metadata"]) for c in chunks]
    db = FAISS.from_documents(documents, embeddings)
    db.save_local("index")
    return db
            