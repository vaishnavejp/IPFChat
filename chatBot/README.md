# Chatbot-using-OpenAi
This is a chatbot implementation in Streamlit using OpenAI ChatGPT and ChromaDB which is a vector database.

## Implementation
<ol>
  <li>Upload the necessary pdfs in the data folder.</li>
  <li>If changes are made to the pdfs other than the default ones,delete all files and folders inside the 'db' directory.</li>
  <li>The default pdfs inside data folder contains information about the IPF documentation(Core and Learn IPF)</li>
  <li>Create an environment file(.env) inside which the openai api key is stored in the format:
     OPENAI_API_KEY='<i>YOUR_API_KEY_HERE</i>'</li>
  <li>Create a virtual environment if required.</li>
  <li>Open the terminal and run the following command for installing the packages inside requirements.txt file : <i>pip install -r requirements.txt</i></li>
  <li>Run the ingest.py file in the terminal using the command : <i>python ingest.py</i></li>
  <li>Check whether embeddings are stored in the db folder in the default format</li>
  <li>Run the app.py file in the terminal using the following command : <i>streamlit run app.py</i></li>
  <li>Open the url mentioned in the terminal in the browser(if not done automatically) and check the result.</li>
</ol>

## Tech Stack



     
      
