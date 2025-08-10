# 🏏 IPL Players Vector Search with ChromaDB & OpenAI Embeddings

This project demonstrates how to use **LangChain**, **ChromaDB**, and **OpenAI embeddings** to store and query IPL players’ profiles using **vector similarity search** and **metadata filtering**.

## 🚀 Features
- **Document Creation** – Store IPL player data with metadata (e.g., team names).
- **Vector Store with ChromaDB** – Persistent local vector database.
- **OpenAI Embeddings** – Convert player descriptions into vector representations.
- **Similarity Search** – Find the most relevant players based on a query.
- **Metadata Filtering** – Query players based on specific attributes (e.g., team).

---

## 📂 Project Structure
.
├── vectore_store.py # Main script to create, store, and search documents
├── chroma_db/ # Persistent ChromaDB storage
├── .env # Stores your OpenAI API key
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Clone the repository
git clone https://github.com/mnabeelasad/LangChain-Vector-Store.git

## Create a virtual environment
python -m venv venv
source venv/bin/activate 

## Install dependencies
pip install -r requirements.txt


## Set your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here