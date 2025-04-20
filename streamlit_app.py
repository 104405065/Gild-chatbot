import streamlit as st
import time
import re
from openai import OpenAI

placeholderstr = "Please input your command"
user_name = "Allen"
user_image = "https://www.w3schools.com/howto/img_avatar.png"

def stream_data(stream_str):
    for word in stream_str.split(" "):
        yield word + " "
        time.sleep(0.15)

def generate_response(prompt):
    prompt = prompt.lower()

    if "emotion of sue" in prompt:
        return ("Sue’s average sentiment is **-0.34** (mostly negative), especially in scenes 42–45.\n"
                "Example: *Dead silence. Sue can’t breathe.*")

    elif "scene 42" in prompt:
        return ("In scene 42, both Harvey and Sue are present.\n"
                "Sue reacts emotionally after Harvey announces her replacement. The overall sentiment is **-0.58**.")

    elif "plot summary" in prompt or "what is it about" in prompt:
        return ("The screenplay *The Substance (2024)* follows Sue, a rising TV host, whose sudden replacement "
                "unfolds a tense emotional journey exploring identity, fame, and agency.")

    elif "harvey personality" in prompt:
        return ("Harvey’s language is assertive, evaluative, and data-driven.\n"
                "Frequent words: *ratings, phenomenal, decision, network*. He embodies authority and media pragmatism.")

    elif "show me the arc" in prompt:
        return "![Emotional Arc](https://i.imgur.com/fake_emotion_arc.png)"

    elif re.search(r"\b(i(\'?m| am| feel| think i(\'?)?m)?\s*(so\s+)?(stupid|ugly|dumb|idiot|worthless|loser|useless))\b", prompt, re.IGNORECASE):
        return "Hey, don't be so hard on yourself. You matter ❤️"

    else:
        return f"🤖 I'm not sure how to respond to that yet. You said: {prompt}"

def main():
    st.set_page_config(
        page_title='K-Assistant - The Residemy Agent',
        layout='wide',
        initial_sidebar_state='auto',
        menu_items={
            'Get Help': 'https://streamlit.io/',
            'Report a bug': 'https://github.com',
            'About': 'About your application: **Hello world**'
            },
        page_icon="img/favicon.ico"
    )

    st.title(f"💬 {user_name}'s Chatbot")

    with st.sidebar:
        selected_lang = st.selectbox("Language", ["English", "繁體中文"], index=1)
        if 'lang_setting' in st.session_state:
            lang_setting = st.session_state['lang_setting']
        else:
            lang_setting = selected_lang
            st.session_state['lang_setting'] = lang_setting

        st.image(user_image)

    st_c_chat = st.container(border=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st_c_chat.chat_message("user", avatar=user_image).markdown(msg["content"])
        else:
            st_c_chat.chat_message("assistant").markdown(msg["content"])

    def chat(prompt: str):
        st_c_chat.chat_message("user", avatar=user_image).write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = generate_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st_c_chat.chat_message("assistant").write_stream(stream_data(response))

    if prompt := st.chat_input(placeholder=placeholderstr, key="chat_bot"):
        chat(prompt)

if __name__ == "__main__":
    main()