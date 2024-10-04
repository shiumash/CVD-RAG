gitfrom langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

DATA_PATH = "data"

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {5len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)
    return chunks

def main():
    documents = load_documents()
    chunks = split_text(documents)

    return chunks

main()