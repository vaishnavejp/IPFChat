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
from langchain import PromptTemplate
from PIL import Image

#customise frontend
st.set_page_config(page_title="ChatBot")
image = Image.open('logo.png')

st.image(image, width=100)

load_dotenv()
#set open api key from .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
#load chromadb embeddings from disk
persist_dir = "db"
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

# caching function for repeated use
@st.cache_resource
def search_db():
    #instruct the gpt-turbo-3.5 model to answer only from embeddings by using a prompt
    prompt_template = """If the context is not relevant, 
    please say Im sorry, but I currently dont have enough context to answer your question. 
    
    {context}
    
    Question: {question}
    """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain_type_kwargs = {"prompt": PROMPT}
    retriever = db.as_retriever()
    #cosine similarity as distance metric of vectors
    retriever.search_kwargs["distance_metric"] = "cos"
    #top 100 results are taken from embedding
    retriever.search_kwargs["fetch_k"] = 100
    # selects embeddings based on a combination of which embeddings are most similar to the inputs, while also optimizing for diversity
    retriever.search_kwargs["maximal_marginal_relevance"] = True
    #top 10 results are fetched
    retriever.search_kwargs["k"] = 10
    model = ChatOpenAI(model="gpt-3.5-turbo")
    # retrivalAQ instance , retrievalQA part of langchain chain library, used for question answering
    qa = RetrievalQA.from_chain_type(model, retriever=retriever, return_source_documents=True, chain_type_kwargs=chain_type_kwargs)
    return qa


qa = search_db()


# Display conversation history using Streamlit messages
def display_conversation(history):
    for i in range(len(history["generated"])):
        message(
            history["past"][i],
            is_user=True,
            key=str(i) + "_user",
        )
        message(history["generated"][i], key=str(i), avatar_style="initials", seed="AI")


def main():
    # Initialize Streamlit app with a title
    st.title("IPF Developer Chatbot")

    with st.expander("About the Chatbot"):
        st.markdown(
            """
            ### You can ask questions about the IPF documentation to this Generative AI powered Chatbot.
            *The better the prompt, the better the answer.*\n
            Examples : 
            - what is a connector? 
            - how to create a project?\n
            You can refer to this [https://docs.ipfdev.co.uk/home/RELEASE-IPF-2023.1.0/home.html] for further information.
            """
        )

    # Get user input from text input
    user_input = st.text_input("", placeholder="Enter your prompt here", key="input")


    # Initialize session state for generated responses and past messages
    if "generated" not in st.session_state:
        st.session_state["generated"] = ["Ask away any questions you have about the IPF documentation."]
    if "past" not in st.session_state:
        st.session_state["past"] = ["Hey there!"]

    # Search the database for a response based on user input and update session state
    if user_input:
        output = qa({"query": user_input})
        print(output["source_documents"])
        #adding the current query and response to appropriate lists
        st.session_state.past.append(user_input)
        response = str(output["result"])
        st.session_state.generated.append(response)

    # Display conversation history using Streamlit messages
    if st.session_state["generated"]:
        display_conversation(st.session_state)


if __name__ == "__main__":
    main()
