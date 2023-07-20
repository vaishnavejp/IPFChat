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

st.set_page_config(page_title="ChatBot")

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

persist_dir = "db"
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)


@st.cache_resource
def search_db():
    retriever = db.as_retriever()
    retriever.search_kwargs["distance_metric"] = "cos"
    retriever.search_kwargs["fetch_k"] = 100
    retriever.search_kwargs["maximal_marginal_relevance"] = True
    retriever.search_kwargs["k"] = 10
    model = ChatOpenAI(model="gpt-3.5-turbo")
    qa = RetrievalQA.from_llm(model, retriever=retriever, return_source_documents=True)
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
        # message(history["generated"][i], key=str(i), avatar_style="initials", seed="AI")
        with st.chat_message("assisstant", avatar="./logo.png"):
            st.markdown(
                "<font size='+2'>" + history["generated"][i],
                unsafe_allow_html=True,
            )


def main():
    query = "how to use an icon provided aws environment?"
    output = qa({"query": query})
    print(output["result"])

    # Initialize Streamlit app with a title
    st.title("IPF Documentation Chatbot")

    with st.expander("About the Chatbot"):
        st.markdown(
            """
            ### You can ask questions about the IPF documentation to this Generative AI powered Chatbot.
            *The better the prompt, the better the answer.*\n
            Examples : 
            - what is a connector? 
            - how to create a project from scratch?\n
            You can refer to this [https://docs.ipfdev.co.uk/home/RELEASE-IPF-2023.1.0/home.html] for further information.
            """
        )

    # Get user input from text input
    user_input = st.text_input("", placeholder="Enter your prompt here", key="input")

    # Initialize session state for generated responses and past messages
    if "generated" not in st.session_state:
        st.session_state["generated"] = ["I am ready to help you"]
    if "past" not in st.session_state:
        st.session_state["past"] = ["Hey there!"]

    # Search the database for a response based on user input and update session state
    if user_input:
        output = qa({"query": user_input})
        print(output["source_documents"])
        st.session_state.past.append(user_input)
        response = str(output["result"])
        st.session_state.generated.append(response)

    # Display conversation history using Streamlit messages
    if st.session_state["generated"]:
        display_conversation(st.session_state)


if __name__ == "__main__":
    main()
