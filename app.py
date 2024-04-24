## streamlit 웹앱 URL: https://newmid-cspuaempw6jmke2bikh8km.streamlit.app/
## Github: https://github.com/wooseungw/new_mid
import streamlit as st
import openai
from datetime import datetime


if "OPEN_API" not in st.session_state:
    st.session_state["OPEN_API"] = ""

if "chat" not in st.session_state:
    st.session_state["chat"] = []
    
if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "system", "content": "You are a helpful assistant. speak Korean"},]

def gpt(prompt,apikey):
    client = openai.OpenAI(api_key=st.session_state["OPEN_API"])
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["message"] + [{"role": "user", "content": prompt}],
        )
    return response.choices[0].message.content

now = datetime.now().strftime("%H:%M")

with st.sidebar.title("Chatbot"):
    st.session_state["OPEN_API"] = st.text_input("API Key", st.session_state["OPEN_API"])


col1, col2 = st.columns([1,1])
with col1:
    st.header("입력하기")
    user_input = st.text_input("User Input")
    if user_input:
        st.session_state["chat"] =  st.session_state["chat"]+ [("user",now, user_input)]

    response = gpt(user_input, st.session_state["OPEN_API"])
    if response:
        st.session_state["chat"] =  st.session_state["chat"]+ [("bot", now, response)]

with col2:
    st.header("채팅 기록")
    for sender, time,message in st.session_state["chat"]:

        if sender == "user":
            st.write(f'<div style="display:flex;align-items:center;"><div style="background-color:#007AFF;color:white;border-radius:12px;padding:8px 12px;margin-right:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
            st.write("")
        elif sender == "bot":
            st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;"><div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
            st.write("")

