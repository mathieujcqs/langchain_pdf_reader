# Ask your PDF #

This short project's aim is to ask questions about a PDF using ChatGPT.

As you may know, ChatGPT (3.5 or 4) input is limited in terms of tokens. Therefore, giving ChatGPT an entire PDF file and asking questions about it is not easy. You may face issues regarding text segmentation or summarization. Both of the latest techniques lead to a lack of context in the end.

That is why this project leverages the power of *Langchain* and *FAISS*.
Using Langchain, this application is able to parse the entire PDF create a knowledge base using FAISS, and then make a semantic search on the knowledge base using the user's query.

## The Knowledge Base
To create the knowledge base we need two things. First, split the text into chunks that are long enough to keep the context of the PDF. Then, an algorithm that transforms those chunks into vectors which enables the semantic/similarity search.

The first is done using *Lagchain text_splitter* and the last via *FAISS*.

## The Semantic Search
Once the text chunks are translated into vectors and stored in the knowledge base, we can leverage this with the user's query. This means that if we convert the query into a vector then we can compare the vectors of the knowledge base to the one of the query. 

The comparison is done using mathematical tools such as the Euclidean distance.

This comparison then gives us the text chunks that are the most relevant to the user's query. Then those text chunks are provided to ChatGPT along with the query.

## How to use the app
First, you need to clone the repo in a local folder. Make sure that you have an environment with `Python` and `pip` installed.

Then load the project dependencies via `pip install -r requirements.txt`.

Don't forget to create a `.env` file in your folder that will contain your OpenAI API key with the variable name: `OPENAI_API_KEY`

After that, you can launch the app via `streamlit run app.py`.
