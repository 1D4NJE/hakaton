import streamlit as st
from datetime import datetime



class Message:
    def __init__(self, sender, content, group_name):
        self.sender = sender
        self.content = content
        self.group_name = group_name
        self.timestamp = datetime.now().strftime("%H:%M")
        self.full_date = datetime.now().strftime("%d/%m/%Y")

    def check_for_bad_words(self, forbidden_words):
        return any(word.lower() in self.content.lower() for word in forbidden_words)


class User:
    def __init__(self, gender, age, nickname, username, number, user_id):
        self.gender = gender
        self.age = age
        self.nickname = nickname
        self.username = username
        self.number = number
        self.user_id = user_id



if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

forbidden_list = ["badword1", "badword2"]
users_db = {
    "Alon": User("M", 17, "alon123", "Alon", "0501111111", 1),
    "Elihav": User("M", 17, "elihav456", "Elihav", "0502222222", 2),
    "Idan": User("M", 17, "idan789", "Idan", "0503333333", 3)
}


st.set_page_config(page_title="Streamlit WhatsApp Clone", layout="centered")

# CSS לעיצוב בועות צ'אט
st.markdown("""
    <style>
    .chat-bubble {
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 10px;
        max-width: 70%;
    }
    .user-bubble {
        background-color: #DCF8C6;
        align-self: flex-end;
        margin-left: auto;
        text-align: right;
    }
    .other-bubble {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        align-self: flex-start;
    }
    .metadata {
        font-size: 0.7em;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 צ'אט קבוצתי: Movie Night")

with st.sidebar:
    st.header("הגדרות משתמש")
    user_choice = st.selectbox("בחר משתמש:", list(users_db.keys()))
    st.session_state.current_user = users_db[user_choice]
    st.info(f"מחובר כ: {st.session_state.current_user.nickname}")

chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        is_me = False
        if msg.sender == st.session_state.current_user.username:
            is_me=True
        bubble_class = "user-bubble" if is_me else "other-bubble"

        # בדיקת מילים אסורות
        display_content = "🚫 [הודעה נחסמה עקב שפה לא נאותה]" if msg.check_for_bad_words(forbidden_list) else msg.content

        st.markdown(f"""
            <div class="chat-bubble {bubble_class}">
                <div style="font-weight: bold; font-size: 0.8em;">{msg.sender}</div>
                <div>{display_content}</div>
                <div class="metadata">{msg.timestamp}</div>
            </div>
        """, unsafe_allow_html=True)

with st.form("send_message_form", clear_on_submit=True):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        user_input = st.text_input("", placeholder="הקלד הודעה...", label_visibility="collapsed")
    with col2:
        submit = st.form_submit_button("שלח")

    if submit and user_input:
        new_msg = Message(
            sender=st.session_state.current_user.username,
            content=user_input,
            group_name="Movie Night"
        )
        st.session_state.messages.append(new_msg)
        st.rerun()  # רענון הדף כדי להציג את ההודעה החדשה