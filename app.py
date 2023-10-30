import os
import streamlit as st
from chains import load_chain
from memory import load_memory


st.set_page_config(layout="wide")
st.title("💬 SUPPORT Chatbot")

# Get a file
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])
st.header("Or you can give a url")
url = st.text_input("Url to parse")

if uploaded_file is not None or url:
    if uploaded_file:
        # Save the file
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        chain = load_chain(uploaded_file.name, uploaded_file.type)
    else:
        chain = load_chain(url, "text/html")
    st.write("## 🤖 Chatbot is ready to answer your questions!")
    memory = load_memory(st)

    if question := st.chat_input():
        # Get and save the question
        st.session_state.messages.append({"role": "user", "content": question})
        st.chat_message("user").write(question)
        
        # Get an answer using question and the conversation history
        response = chain(
            {
                "question": question,
                "chat_history": memory.load_memory_variables({})["history"],
            }
        )
        answer = response["answer"]
        # Save the answer
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
