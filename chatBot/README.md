# Chatbot-using-OpenAi
This is a chatbot implementation in Streamlit using OpenAI ChatGPT and ChromaDB which is a vector database.

## Implementation

1) Upload the necessary pdfs in the data folder
2) If changes are made to the pdfs other than the default ones,delete all files and folders inside the 'db' directory
3) The default pdfs inside data folder contains information about the IPF documentation(Core and Learn IPF)
4) Create an environment file(.env) inside which the openai api key is stored in the format:```OPENAI_API_KEY='YOUR_API_KEY_HERE'```
5) Create a virtual environment if required.
6) Open the terminal and run the following command for installing the packages inside requirements.txt file :
   ```Python
   pip install -r requirements.txt
   ```
7) Run the ```ingest.py``` file in the terminal using the command :
   
   ```Python
   python ingest.py
   ```
8) Check whether embeddings are stored in the db folder in the default format.
9) Run the ```app.py``` file in the terminal using the following command :
    
   ```Python
   streamlit run app.py
   ```
10) Open the url mentioned in the terminal in the browser(if not done automatically) and check the result.
   
## Tech Stack
<ul>
  <li> Interpreter: Python</li>
  <li>Text Editor: Notepad / Visual Studio Code</li>
  <li>To run the model:
    <ol>
      <li>Command Prompt</li>
        <li> Anaconda Shell</li>
        <li>Visual Studio Code terminal / Your preferred text editor terminal.</li>
    </ol>
  </li>
</ul>






     
      
