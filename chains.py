from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from prompts import CONDENSE_QUESTION_PROMPT
from prompts import SUPPORT_QA_PROMPT

import streamlit as st
from load_data import load_text_file, load_pdf_file, load_website
from index_data import create_index

@st.cache_resource
def load_chain(file_name: str, file_type: str):
    if file_type == "text/plain":
        docs = load_text_file(file_name)
    elif file_type == "application/pdf":
        docs = load_pdf_file(file_name)
    elif file_type == "text/html":
        docs = load_website(file_name)
    else:
        st.write("File type is not supported!")
        st.stop()

    retriever = create_index(docs)
    

    chain = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(model_name="gpt-4", temperature=0),
        retriever,
        condense_question_llm=ChatOpenAI(model_name="gpt-4"),
        condense_question_prompt=PromptTemplate.from_template(CONDENSE_QUESTION_PROMPT),
        verbose=True,
        combine_docs_chain_kwargs={"prompt": PromptTemplate.from_template(SUPPORT_QA_PROMPT)}
    )
    return chain
