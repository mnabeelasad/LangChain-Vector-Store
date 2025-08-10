from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create LangChain documents for IPL players

doc1 = Document(
    page_content="Shubman Gill is one of the most promising young batsmen in IPL, known for his elegant stroke play and consistency at the top of the order.",
    metadata={"team": "Gujarat Titans"}
)

doc2 = Document(
    page_content="Sanju Samson is a dynamic wicketkeeper-batsman and captain of Rajasthan Royals, admired for his aggressive batting and leadership skills.",
    metadata={"team": "Rajasthan Royals"}
)

doc3 = Document(
    page_content="KL Rahul is an accomplished opener for Lucknow Super Giants, recognized for his calm demeanor and ability to anchor big chases.",
    metadata={"team": "Lucknow Super Giants"}
)

doc4 = Document(
    page_content="Rashid Khan, the Afghan leg-spinner, is celebrated for his exceptional bowling economy and match-winning performances in the IPL.",
    metadata={"team": "Gujarat Titans"}
)

doc5 = Document(
    page_content="Andre Russell is a powerful all-rounder for Kolkata Knight Riders, feared for his explosive batting and ability to change games with both bat and ball.",
    metadata={"team": "Kolkata Knight Riders"}
)

docs = [doc1, doc2, doc3, doc4, doc5]

vector_store = Chroma.from_documents(
    embedding=OpenAIEmbeddings(),
    persist_directory="chroma_db",
    collection_name="sample",
    documents=docs
)

data = vector_store.get(include=["embeddings", "documents", "metadatas"])


hits = vector_store.similarity_search(
    query="", 
    filter={"team": "Gujarat Titans"}
)
print("Gujarat Titans Players:")
for hit in hits:
    print(hit.page_content)


hits = vector_store.similarity_search_with_score(
    query="", 
    filter={"team": "Gujarat Titans"},
    k=5
)

print("Gujarat Titans Players with scores:")
for doc, score in hits:
    print(f"{doc.page_content} (score: {score})")


hits = vector_store.similarity_search(
    query="In which team Russell play?", 
    k=1
)
for d in hits:
    print(d.page_content, d.metadata)

