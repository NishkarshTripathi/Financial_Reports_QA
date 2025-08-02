import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA


# Load the API key from .env file
load_dotenv()

'''
# Load the document (replace with your file)
file_path = "TCS_AnnualReport_2023-2024.pdf"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} was not found. Please place your document in the project directory.")

loader = PyPDFLoader(file_path)
documents = loader.load()

# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)

# Create embeddings and store them in ChromaDB
print("Creating embeddings and storing in ChromaDB...")
embedding_model = OpenAIEmbeddings()

# This will create and save the vector store in the 'db' folder
vector_store = Chroma.from_documents(
    chunks,
    embedding=embedding_model,
    persist_directory="db"
)

print("Embeddings successfully created and saved.")
'''

# Load the vector store from disk
print("Loading vector store from disk...")
# The 'db' folder must exist from the previous step
if not os.path.exists("db"):
    raise FileNotFoundError("The 'db' directory was not found. Please run the previous step to create it.")

embedding_model = OpenAIEmbeddings()
vector_store = Chroma(
    persist_directory="db",
    embedding_function=embedding_model
)

# Define the retriever
retriever = vector_store.as_retriever()

# Initialize the LLM
llm = ChatOpenAI(temperature=0) # temperature=0 for consistent, factual answers

# Create the RAG chain
print("Building the RAG chain...")
qa_chain = RetrievalQA.from_chain_type(
    llm,
    chain_type="stuff",
    retriever=retriever,
)

# Interactive Q&A loop
print("\nReady! Ask me a question about your Document.")
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    response = qa_chain.invoke({"query": query})
    print(f"AI: {response['result']}")