# IPFChat
## Custom knowledge chatbot
A custom knowledge chatbot is a specialised artificial intelligence program designed to interact with users and provide accurate and tailored information based on a specific domain or topic.
Unlike generic chatbots, custom knowledge chatbot is trained on a specific dataset which allows it to answer queries with higher precision and expertise in that particular area.

### Problem statement
IPF Developer Documentation, similar to most vendor product manuals, is designed to be a longish book/tutorial type read. A chatbot style Q/A utility may be better suited for rapid learning on the job.<br>
[Link to IPF documentation:](https://docs.ipfdev.co.uk/home/RELEASE-IPF-2023.1.0/home.html)
### Objective:
1) Integrate the IPF Developer Documentation into a Chatbot model, allowing it to access and utilize the information for answering specific queries related to IPF development.
2) Enhance the model's natural language understanding capabilities to accurately interpret user queries, even when they are complex or contain technical terms related to IPF development.
3) The model should be capable of understanding the intent behind the question and retrieving the most appropriate information from the knowledge base.


#### There are 3 main steps in developing a custom knowledge chatbot

1) Data collection - Web page scraping
2) Data processing -
   i) Generating embeddings
   ii) Saving embeddings to local DB

3) Inference - Use embedding to answer queries
