from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

# Create dummy internship FAQ data
os.makedirs("docs", exist_ok=True)
with open("docs/internship_faq.txt", "w") as f:
    f.write(
        """
        Q: What is the duration of the internship?
        A: Internships last for 6 to 12 weeks.

        Q: Is the internship paid?
        A: Yes, a stipend is provided monthly.

        Q: Can I apply if I’m a 2nd-year student?
        A: Yes, students from 2nd year onwards can apply.

        Q: What kind of work will interns do?
        A: Interns will work on real-time projects, attend team meetings, and receive mentorship.
        """
    )

# Load and split
loader = TextLoader("docs/internship_faq.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
splits = splitter.split_documents(docs)

# Embed & store
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(),
    persist_directory="chroma_db"
)

retriever = vectorstore.as_retriever()
