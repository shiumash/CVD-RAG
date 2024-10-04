from doc_parser import load_documents, split_text

def main():
    documents = load_documents()
    chunks = split_text(documents)

    return chunks

if "__name__" == "__main__":
    main()