import os 
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv 
import streamlit as st 
from streamlit_chat import message

load_dotenv()
#set open api key from .env
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
# directory to store embedding
persist_dir="db"

@st.cache_data
def doc_preprocessing():
    #loading data from pdfs
    loader = DirectoryLoader(
        'data/',
        glob='**/*.pdf',     # only the PDFs
        show_progress=True
    )
    docs = loader.load()
    # initialising chunk size to 1000 and chunk overlap to 0
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=0
    )
    # splitting the documents into chunks and returning them
    docs_split = text_splitter.split_documents(docs)
    return docs_split

@st.cache_resource
def embeddings_store():
    #embedding using open ai api
    embeddings = OpenAIEmbeddings()
    texts = doc_preprocessing()
    persist_dir='db'
    #generating the embeddings and storing it in 'db' directory
    db = Chroma.from_documents(documents=texts,embedding=embeddings,persist_directory=persist_dir)
    db.persist()
    db=None

def main():
    embeddings_store()
    
if __name__ == "__main__":
    main()
