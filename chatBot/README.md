# Chatbot-using-OpenAi
This is a chatbot implementation in Streamlit using OpenAI ChatGPT and ChromaDB which is a vector database.

## Implementation

1) Upload the necessary pdfs to data folder.
2) If changes are made to the pdfs other than the default ones,delete all files and folders inside the 'db' directory.
3) The default pdfs inside the data folder has files containing information about IPF Documentation(CORE and LEARN IPF).
4) Create an environment file(.env) inside where the openai api key is stored in the following format:```OPENAI_API_KEY='YOUR_API_KEY_HERE'```
5) Create a virtual environment to run if needed.
6) Open terminal and run the following command to install the packages in requirements.txt file :
   ```Python
   pip install -r requirements.txt
   ```
7) Run the ```ingest.py``` file in the terminal using the command :
   
   ```Python
   python ingest.py
   ```
8) Check if the embeddings are stored in 'db' folder in the required format.
9) Run the ```app.py``` file in the terminal using the following command :
    
   ```Python
   streamlit run app.py
   ```
10) Open the url mentioned in the terminal of the text editor and open it(if not done automatically) in the browser.
   
## Tech Stack
1) Interpreter: ```Python```
2) Text Editor: ```Notepad / Visual Studio Code / Preferred text editor```
  <p>To run the model:</p> 
1) Command Prompt
<br>
2) Anaconda Shell
<br>
3) Visual Studio Code terminal / Your preferred text editor terminal
    





     
      
