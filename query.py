from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def main():
    print("Loading embedding model and vector database...")
    try:
        # Step 1: Load embeddings (must be same as when you saved)
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Step 2: Load FAISS index (allow deserialization for files you created)
        db = FAISS.load_local("html_faiss_index", embeddings, allow_dangerous_deserialization=True)
        
        print("\n✅ Vector database loaded successfully!")
        print("-" * 50)
        print("Personal RAG Query System")
        print("Type 'exit' or 'quit' to end the session")
        print("-" * 50)
        
        # Interactive query loop
        while True:
            # Get user input
            query = input("\nEnter your question: ").strip()
            
            # Exit condition
            if query.lower() in ['exit', 'quit', 'q']:
                print("\nThank you for using the Personal RAG Query System. Goodbye!")
                break
                
            if not query:
                print("Please enter a valid question.")
                continue
                
            # Step 3: Do similarity search
            results = db.similarity_search_with_score(query, k=5)  # k is the number of most relevant chunks to return
            
            # Step 4: Print results
            if not results:
                print("\nNo relevant results found. Try a different question.")
                continue
                
            print(f"\nFound {len(results)} relevant results:")
            print("-" * 50)
            
            for i, (doc, score) in enumerate(results):
                relevance = round(100 * (1 - score / 2), 2)  # Convert distance score to a relevance percentage
                print(f"Result {i+1} (Relevance: {relevance}%):")
                print(f"Content: {doc.page_content}")
                
                # Print metadata if available
                if hasattr(doc, 'metadata') and doc.metadata:
                    if 'source' in doc.metadata:
                        print(f"Source: {doc.metadata['source']}")
                
                print("-" * 50)
                
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nPossible solutions:")
        print("1. Make sure you have run embedding.py to create the vector database")
        print("2. Verify that the embedding model is available")
        print("3. Check if 'html_faiss_index' directory exists with the index files")
        raise e  # Re-raise to see the full stacktrace

if __name__ == "__main__":
    main()