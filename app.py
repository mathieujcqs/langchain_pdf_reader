import yaml
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain

def get_chunks_from_pages(pages, CONFIG):
    """
    Creates chunks of text from the pdf pages
    """

    text = ""
    for page in pages:
        text += page.extract_text()

    #split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=CONFIG['chunk_size'],
        chunk_overlap=CONFIG['chunk_overlap'],
        length_function=len
    )

    return text_splitter.split_text(text=text)

def hanlde_user_question(user_question, knowledge_base):
    """
    Returns the response of the user's question
    """
    docs = knowledge_base.similarity_search(user_question)
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type='stuff')
    response = chain.run(input_documents=docs, question=user_question)

    return response
def main(CONFIG):
    load_dotenv()
    st.set_page_config(page_title=CONFIG['page_title'])
    st.header(CONFIG['header_text'])

    pdf = st.file_uploader(CONFIG['file_uploader_text'], type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        chunks = get_chunks_from_pages(pdf_reader.pages, CONFIG)

        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        
        user_question = st.text_input(CONFIG['question_placeholder'])
    
        if user_question:
            response = hanlde_user_question(user_question, knowledge_base)
            
            st.write(response)


if __name__ == '__main__':
    with open('main.yml', 'r') as config:
        CONFIG = yaml.load(config, Loader=yaml.FullLoader,)
        main(CONFIG)