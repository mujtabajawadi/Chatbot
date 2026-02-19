from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
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

chat_template = ChatPromptTemplate([
     ("system", "You are a general purpose AI assistant which helps users and you remember previous details for context awareness to help the users better."),
     MessagesPlaceholder(variable_name="chat_history"),
     ("human", "{query}")
])

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)



    with st.chat_message("assistant", avatar="👻"):
        history = [] 
        for msg in st.session_state.messages:
             role = "assistant" if msg["role"] == "assistant" else "human"
             history.append((role, msg["content"]))
        
        full_prompt = chat_template.format_messages(
             chat_history = history,
             query = user_input
        )
        result = st.write_stream(model.stream(full_prompt))
    st.session_state.messages.append({"role": "assistant", "content": result})
elif not st.session_state.messages:
        st.info("Waiting for your message!")
    


print()