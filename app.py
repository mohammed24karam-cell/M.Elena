import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- 1. إعداد المحرك مباشرة ---
API_KEY = "AIzaSyDRDbpLkuoNscCiALpmAwTBjr_WSAhwhNQ"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. إعدادات الواجهة ---
st.set_page_config(page_title="M.Elena AI", layout="wide")

with st.sidebar:
    st.markdown("### ✨ لوحة التحكم")
    if st.button("➕ محادثة جديدة", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    gender = st.radio("من المتحدث الآن؟", ["بنت", "شاب"], index=0)
    lang = st.selectbox("لغة الحوار:", ["العربية الفصحى", "العامية السورية", "العامية العراقية", "English"])

# تصميم الشعار الوردي الكيوت
accent = "#FF69B4" if gender == "بنت" else "#1A237E"
st.markdown(f'<h1 style="text-align:center; color:{accent}; font-size:50px;">✨ M.Elena ✨</h1>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("اسأليني أي شيء...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            # هنا السطر اللي كان فيه المشكلة وصلحته
            response = model.generate_content(f"أنت مساعدة ذكية اسمك M.Elena، ردي بـ {lang}: " + user_input)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except:
            st.error("أهلاً بكِ! جربي مراسلتي مرة أخرى.")
