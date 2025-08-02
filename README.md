# Financial Report Q&A System

### RAG System Architecture Diagram:
User -> App -> LLM & Vector DB -> Response.

### 📝 Overview

This project implements a Retrieval-Augmented Generation (RAG) system capable of answering natural language questions about a provided financial PDF document. The system processes the document, creates a searchable knowledge base, and then uses a Large Language Model (LLM) to generate accurate, context-aware answers.

This project serves as a practical, end-to-end demonstration of a RAG pipeline, covering data ingestion, chunking, embedding, vector search, and final response generation.

### 🚀 Features

* **Document Ingestion:** Loads and processes PDF files as a knowledge source.
* **Intelligent Chunking:** Uses a recursive text splitter to break down documents into semantically coherent chunks.
* **Vector Database:** Creates and persists a vector store using **ChromaDB** for efficient semantic search.
* **Context-Aware Q&A:** Retrieves relevant document chunks and provides them as context to a powerful LLM (**OpenAI's GPT**), ensuring grounded and accurate responses.
* **Scalable Architecture:** Built with a modular approach using **LangChain**, demonstrating principles that extend to production-grade systems.

### 🛠️ Technologies Used

* **Python 3.x**
* **LangChain:** For building the RAG pipeline.
* **OpenAI API:** For text embeddings (`OpenAIEmbeddings`) and the Language Model (`ChatOpenAI`).
* **ChromaDB:** As the local vector store for development.
* **python-dotenv:** For secure management of API keys.
* **pypdf:** For loading PDF documents.

### ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Financial_Reports_QA.git](https://github.com/your-username/Financial_Report_QA.git)
    cd Financial_Reports_QA
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Don't forget to create a `requirements.txt` file by running `pip freeze > requirements.txt`)*

4.  **Configure your API key:**
    * Create a file named `.env` in the root of the project.
    * Add your OpenAI API key to the file:
        ```
        OPENAI_API_KEY="your-api-key-here"
        ```

5.  **Place your document:**
    * Add your financial PDF document to the project's root directory.
    * Update the `file_path` variable in the `rag_system.py` script to match your document's filename.

### 🏃 How to Run the Application

Run the main script from your terminal:

```bash
python rag_system.py
   ```


#### The script will:

* Load and chunk the PDF.

* Create a vector store in the db/ directory.

* Start an interactive command-line interface.

You can then ask questions about the document and receive grounded answers.