from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st


my_key = st.secrets["GOOGLE_API_KEY"]
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=my_key)


st.header("Chat with Tech Gini")

if "messages" not in st.session_state:
    st.session_state["messages"] = []


for message in st.session_state["messages"]:
    with st.chat_message(message['role']):
        st.write(message["content"])

user_input = st.chat_input('Ask Gini 👻', key="chatbot_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)



    with st.chat_message("assistant", avatar="👻"):
        result = st.write_stream(model.stream(user_input))
    st.session_state.messages.append({"role": "assistant", "content": result})
elif not st.session_state.messages:
        st.info("Waiting for your message!")
    