
from pdfminer.high_level import extract_text
import docx
import os

def extract_pdf_text(path):
    return extract_text(path)

def extract_docx_text(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def load_documents(folder):
    docs = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.endswith(".pdf"):
            text = extract_pdf_text(path)
        elif file.endswith(".docx"):
            text = extract_docx_text(path)
        else:
            continue
        docs.append({"file": file, "text": text})
    return docs
            