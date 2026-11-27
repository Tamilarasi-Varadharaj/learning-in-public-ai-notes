import warnings
warnings.filterwarnings("ignore")

import streamlit as st
from llmproviders import run_llm

st.set_page_config(page_title="LLM Chat", page_icon=":robot_face:")
st.title("LLM Chat Application")

if "history" not in st.session_state:
    st.session_state["history"] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

for msg in st.session_state["history"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state["history"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("...")

        response = run_llm(st.session_state["history"])
        message_placeholder.markdown(response)

        st.session_state["history"].append({"role": "assistant", "content": response})
        st.chat_message("assistant").markdown(response)

if(st.button("♻️ Reset Chat")):
    st.session_state["history"] = [{"role": "assistant", "content": "Conversation Reset! How can I assist you today?"}]
    st.rerun()