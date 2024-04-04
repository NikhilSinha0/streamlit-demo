import streamlit as st
from transformers import pipeline

pipe = pipeline("question-answering", model="Intel/dynamic_tinybert")

def main():
    st.title("Question answering using Intel's Dynamic TinyBERT")
    st.caption("Add a passage into the sidebar and ask the model questions about it. The passages that work best are factual passages, i.e. from Wikipedia")

    # We need 2 input text boxes, one for the passage and one for the query
    with st.sidebar:
        context_text = st.text_area("Enter your passage", "", height=600)
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "What would you like to know about this passage?"}]
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    query_text = st.chat_input()
    if query_text:

        st.session_state.messages.append({"role": "user", "content": query_text})
        st.chat_message("user").write(query_text)
        
        answer = pipe(question=query_text, context=context_text)["answer"]

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)

if __name__ == "__main__":
    main()