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

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
#os.environ['ACTIVELOOP_TOKEN'] = os.getenv('ACTIVELOOP_TOKEN')
#os.environ['DEEPLAKE_ACCOUNT_NAME']= os.getenv('DEEPLAKE_ACCOUNT_NAME')

persist_dir="db"

@st.cache_data
def doc_preprocessing():
    loader = DirectoryLoader(
        'data/',
        glob='**/*.pdf',     # only the PDFs
        show_progress=True
    )
    docs = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=0
    )
    docs_split = text_splitter.split_documents(docs)
    return docs_split

@st.cache_resource
def embeddings_store():
    embeddings = OpenAIEmbeddings()
    print(embeddings)
    texts = doc_preprocessing()
    persist_dir='db'
    db = Chroma.from_documents(documents=texts,embedding=embeddings,persist_directory=persist_dir)
    print(db)
    db.persist()
    db=None
    #db = DeepLake(
    #dataset_path=f"hub://aianytime07/text_embedding",
    #read_only=True,
    #embedding_function=embeddings,
    #)

def main():
    embeddings_store()
    
if __name__ == "__main__":
    main()

