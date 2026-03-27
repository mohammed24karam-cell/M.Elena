import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- 1. إعدادات المحرك (الذكاء الاصطناعي) ---
# حطي الكود السري تبعك (الذي يبدأ بـ AIza) بين علامتي التنصيص هنا:
API_KEY = "AIzaSyDRDbpLkuoNscCiALpmAwTBjr_WSAhwhNQ" 

if API_KEY != "AIzaSyDRDbpLkuoNscCiALpmAwTBjr_WSAhwhNQ":
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.warning("AIzaSyDRDbpLkuoNscCiALpmAwTBjr_WSAhwhNQ")

# --- 2. إعدادات واجهة المستخدم والتصميم ---
st.set_page_config(page_title="M.Elena AI", layout="wide")

# القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("### ✨ لوحة التحكم")
    if st.button("➕ محادثة جديدة", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.write("---")
    gender = st.radio("من المتحدث الآن؟", ["بنت", "شاب"], index=0)
    lang = st.selectbox("لغة الحوار:", [
        "العربية الفصحى", "العامية السورية", "العامية العراقية", 
        "كوردية (سوراني)", "كوردية (باديني)", "تركماني", "تركي", "English"
    ])

# دالة لتغيير الثيم والشعار بناءً على الجنس (دمج الشعار مع التصميم)
def apply_theme_and_logo(gender):
    if gender == "بنت":
        bg, text, accent = "#FFF0F5", "#D81B60", "#FF69B4"
        logo_html = f'<h1 style="color: {accent}; text-shadow: 2px 2px 4px #FFB6C1; font-size: 50px;">✨ M.Elena ✨</h1>'
        sub_text = "رقة، ذكاء، ولباقة"
    else:
        bg, text, accent = "#F0F2F6", "#1A237E", "#000000"
        logo_html = f'<h1 style="color: {accent}; letter-spacing: 3px; font-size: 45px;">M.ELENA</h1>'
        sub_text = "الذكاء والقوة"

    st.markdown(f"""
        <style>
        .stApp {{ background-color: {bg}; color: {text}; }}
        .stButton>button {{ background-color: {text}; color: white; border-radius: 20px; }}
        </style>
        <div style="text-align: center; padding: 10px;">
            {logo_html}
            <p style="color: {text}; font-style: italic; opacity: 0.8;">{sub_text}</p>
        </div>
    """, unsafe_allow_html=True)

apply_theme_and_logo(gender)

# --- 3. نظام الذاكرة والمحادثة ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثات القديمة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إعداد الـ Prompt (تعليمات الشخصية)
persona = f"""
أنت مساعد ذكي جداً اسمك M.Elena. أسلوبك هادئ، لطيف، محترم ولبق للغاية.
أنت تتحدث الآن بـ: {lang}.
المستخدم الآن هو: {gender}. 
إذا كان المستخدم بنت: كوني رقيقة جداً في تعبيراتك.
إذا كان المستخدم شاب: كوني هادئة ومباشرة.
أنت خبيرة في كل شيء: رياضيات، كشف فبركة الصور، والعلوم الاجتماعية.
"""

# --- 4. إدخال البيانات (صوت، صورة، نص) ---
col1, col2 = st.columns(2)
with col1:
    img_input = st.file_uploader("📸 ارفع صورة (رياضيات أو تحليل)", type=['png', 'jpg', 'jpeg'])
with col2:
    audio_input = st.file_uploader("🎤 ارفع تسجيل صوتي", type=['mp3', 'wav', 'm4a'])

user_input = st.chat_input("اسأليني أي شيء في العالم...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("M.Elena تفكر..."):
            try:
                # تجميع الطلب (نص + صورة إن وجدت)
                request_parts = [persona, user_input]
                if img_input:
                    request_parts.append(Image.open(img_input))
                
                response = model.generate_content(request_parts)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("AIzaSyDRDbpLkuoNscCiALpmAwTBjr_WSAhwhNQ")

# رسالة ترحيبية إذا كانت المحادثة فارغة
if not st.session_state.messages:
    welcome = "أهلاً بكِ عزيزتي الغالية، كيف يمكنني مساعدتكِ اليوم؟" if gender == "بنت" else "أهلاً بك، أنا جاهز لمساعدتك بكل هدوء."
    st.info(welcome)
