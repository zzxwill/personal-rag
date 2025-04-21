import os
from pathlib import Path
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Config: Path to your HTML folder
html_folder = 'sources'

# Check if the path exists
html_folder_path = Path(html_folder)
if not html_folder_path.exists() or not html_folder_path.is_dir():
    raise ValueError(f"❌ The specified path {html_folder} does not exist or is not a directory. Please check!")

# 1. Load files (HTML and Markdown)
documents = []
html_files = list(html_folder_path.glob("**/*.html")) + list(html_folder_path.glob("**/*.htm"))
md_files = list(html_folder_path.glob("**/*.md")) + list(html_folder_path.glob("**/*.markdown"))
all_files = html_files + md_files

if not all_files:
    raise ValueError(f"❌ No HTML or Markdown files found in the folder {html_folder}!")

for file_path in all_files:
    try:
        # Load file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Process based on file type
        if file_path.suffix.lower() in ['.html', '.htm']:
            # HTML files: use BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.extract()
            # Extract text
            text = soup.get_text(separator=' ', strip=True)
        else:
            # Markdown files: use content as is (could add a Markdown parser if needed)
            text = content
        
        # Create a Document object
        doc = Document(
            page_content=text,
            metadata={"source": str(file_path)}
        )
        documents.append(doc)
        print(f"✅ Loaded {file_path.name}: {len(text)} characters")
    except Exception as e:
        print(f"⚠️ Error loading {file_path}: {e}")

print(f"✅ Loaded {len(documents)} documents.")

# 2. Split documents into smaller chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

print(f"✅ After splitting, got {len(docs)} chunks.")

# Check if we have any chunks to process
if len(docs) == 0:
    print("⚠️ No chunks were created. The document might be too small or there might be issues with the text extraction.")
    # Create a simple document with the original content to ensure we have at least one document
    if len(documents) > 0:
        print("👉 Using original documents without chunking instead.")
        docs = documents
    else:
        print("❌ No documents to process. Please check your files.")
        exit(1)

# Print first chunk to verify content (for debugging)
if len(docs) > 0:
    print(f"\nFirst chunk content sample (first 100 chars): \n{docs[0].page_content[:100]}...\n")

# 3. Create local embeddings
try:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    print(f"✅ Embedding model loaded successfully.")
except Exception as e:
    raise RuntimeError(f"❌ Failed to load embedding model: {e}")

# 4. Store documents into a local vector database (FAISS)
try:
    db = FAISS.from_documents(docs, embeddings)
    print(f"✅ Created vector database with {len(docs)} documents.")
except Exception as e:
    raise RuntimeError(f"❌ Failed to build the vector database: {e}")

# 5. Save FAISS index locally
output_dir = "html_faiss_index"
try:
    db.save_local(output_dir)
except Exception as e:
    raise RuntimeError(f"❌ Failed to save the vector database: {e}")

print(f"🎉 Vector database saved successfully to folder {output_dir}!")