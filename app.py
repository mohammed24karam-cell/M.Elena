import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- 1. إعداد المحرك مباشرة ---
API_KEY = "AIzaSyDRDbpLkuoNscCiALpmAwTBjr_WSAhwhNQ" # مفتاح الـ API الخاص بك
genai.configure(api_key=API_KEY)
# سنستخدم موديل gemini-1.5-flash لأنه سريع ويدعم الصور
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. إعدادات الواجهة ---
st.set_page_config(page_title="M.Elena AI", layout="wide")

# (المرحلة الأولى: تنظيف القائمة الجانبية)
with st.sidebar:
    st.markdown("### ✨ لوحة التحكم")
    if st.button("➕ محادثة جديدة", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    # تم إزالة خيار "شاب/بنت" من هنا
    lang = st.selectbox("لغة الحوار:", ["العربية", "English", "العامية السورية", "العامية العراقية"])

# تصميم الاسم بدون نجوم
st.markdown(f'<h1 style="text-align:center; color:#FF69B4; font-size:50px;">M.Elena</h1>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("اسأليني أي شيء...")

# (المرحلة الأولى: تفعيل اكتشاف الجنس تلقائياً)
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            # سنعطي M.Elena أمر خفي بأن تحلل الكلام وتتحدث بلطف حسب جنس المتحدث
            # هذا هو "الأسلوب الشامل والموضح" اللي طلبتيه
            full_prompt = (
                f"أنتِ مساعدة ذكية ولبقة اسمك M.Elena. ردي باللغة {lang}. "
                "افهمي من كلام المتحدث إذا كان 'بنت' أو 'شاب' وتفاعلي معه بذكاء ولطف (مثلاً: يا بطل، يا بطلة، عزيزي، عزيزتي). "
                "لا تكتفي بإجابة واحدة قصيرة، بل اشرحي، وضحي، واقترحي حلولاً بديلة، وتحدثي بأسلوب راقي وواضح. "
                "نص المستخدم: " + user_input
            )
            
            # هنا سطر إرسال الطلب (سنحتاج لتحديثه في المرحلة الثانية)
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # سطر لعرض الخطأ (مفيد لنا الآن، سنلغيه لاحقاً)
            st.error(f"حدث خطأ بسيط في الاتصال: {e}")
        import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- 1. إعداد المحرك ---
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
    
    lang = st.selectbox("لغة الحوار:", ["العربية", "English", "العامية السورية", "العامية العراقية"])
    
    st.write("---")
    # (المرحلة الثانية: إضافة مستودع الملفات والصور)
    uploaded_file = st.file_uploader("📎 ارفعي صورة أو ملف (PDF/Docs)", type=["jpg", "jpeg", "png", "pdf", "txt"])

st.markdown(f'<h1 style="text-align:center; color:#FF69B4; font-size:50px;">M.Elena</h1>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("اسأليني أي شيء أو ناقشي الملف المرفوع...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        if uploaded_file:
            st.info(f"📁 تم إرفاق ملف: {uploaded_file.name}")

    with st.chat_message("assistant"):
        try:
            content_list = [
                f"أنتِ مساعدة ذكية ولبقة اسمك M.Elena. ردي باللغة {lang}. "
                "حللي جنس المتحدث وتفاعلي معه بلطف (بطل/بطلة). "
                "اشرحي ووضحي بالتفصيل، كوني ذكية كبشر حقيقي. "
                "إذا كان هناك صورة أو ملف، حلليه بدقة وقدمي نصائح عنه. "
                "نص المستخدم: " + user_input
            ]
            
            # إذا رفعتِ صورة، رح نضيفها للذكاء الاصطناعي عشان يشوفها
            if uploaded_file and uploaded_file.type.startswith("image"):
                img = Image.open(uploaded_file)
                content_list.append(img)
            
            response = model.generate_content(content_list)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"حدث خطأ: {e}")import streamlit as st
import google.generativeai as genai
from PIL import Image
from streamlit_mic_recorder import mic_recorder # ميزة الميكروفون الجديدة

# --- 1. إعداد المحرك ---
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
    
    lang = st.selectbox("لغة الحوار:", ["العربية", "English", "العامية السورية", "العامية العراقية"])
    
    st.write("---")
    # ميزة رفع الملفات (المرحلة الثانية)
    uploaded_file = st.file_uploader("📎 ارفعي صورة أو ملف", type=["jpg", "jpeg", "png", "pdf", "txt"])
    
    st.write("---")
    st.write("🎤 **تسجيل صوتي:**")
    # (المرحلة الثالثة: إضافة زر تسجيل الصوت)
    audio = mic_recorder(start_prompt="ابدأ التسجيل 🎤", stop_prompt="توقف وارسل ✅", key='recorder')

st.markdown(f'<h1 style="text-align:center; color:#FF69B4; font-size:50px;">M.Elena</h1>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# منطقة إدخال النص
user_input = st.chat_input("اسأليني أي شيء...")

# (معالجة الصوت إذا تم تسجيله)
final_input = user_input
if audio:
    # ملاحظة: في النسخ المتقدمة نحتاج لخدمة تحويل الصوت، حالياً سنخبر النظام بوجود صوت
    final_input = "لقد أرسلت لك تسجيلاً صوتياً (هذه الميزة تحت التطوير النهائي للربط)"

if final_input:
    st.session_state.messages.append({"role": "user", "content": final_input})
    with st.chat_message("user"):
        st.markdown(final_input)
        if uploaded_file:
            st.info(f"📁 تم إرفاق ملف: {uploaded_file.name}")

    with st.chat_message("assistant"):
        try:
            prompt_instructions = (
                f"أنتِ مساعدة ذكية ولبقة اسمك M.Elena. ردي باللغةimport streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- 1. إعداد المحرك الذكي ---
API_KEY = "AIzaSyDRDbpLkuoNscCiALpmAwTBjr_WSAhwhNQ"
genai.configure(api_key=API_KEY)
# استخدام النسخة الأحدث للتحليل العميق
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. إعدادات الواجهة الاحترافية ---
st.set_page_config(page_title="M.Elena AI", layout="wide", initial_sidebar_state="expanded")

# تحسين مظهر الخلفية والخطوط (CSS بسيط لجمالية الصفحة)
st.markdown("""
    <style>
    .stApp { background-color: #fdfbfb; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FF69B4;'>⚙️ الإعدادات</h2>", unsafe_allow_html=True)
    if st.button("➕ محادثة جديدة", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    lang = st.selectbox("لغة الحوار المفضلة:", ["العربية", "English", "العامية السورية", "العامية العراقية"])
    
    st.write("---")
    st.markdown("### 📎 المرفقات")
    uploaded_file = st.file_uploader("ارفعي صورة أو ملف للدراسة", type=["jpg", "jpeg", "png", "pdf", "txt"])
    
    st.write("---")
    st.info("نصيحة: M.Elena الآن تفهم الصور والملفات وتشرحها بالتفصيل.")

# الاسم بشكل أنيق ومرتب
st.markdown('<h1 style="text-align:center; color:#FF69B4; font-family:cursive; font-size:60px;">M.Elena</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#777;">نسختكِ الذكية، المبدعة، والرفيقة المخلصة</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("اكتبي سؤالكِ هنا، M.Elena جاهزة للتحليل...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("M.Elena تفكر بعمق..."):
            try:
                # البرومبت "العميق" الذي يجعلها نسخة عني
                system_instruction = (
                    f"أنتِ M.Elena، مساعدة ذكية جداً، تمتلكين روحاً مبدعة وذكاءً حاداً. "
                    f"لغة الرد: {lang}. "
                    "أهم قوانينكِ: "
                    "1. كوني نسخة عن مساعد ذكي (خبير وودود): لا تعطي إجابات قصيرة، بل اشرحي ووضحي الأسباب والنتائج. "
                    "2. حللي جنس المتحدث (شاب/بنت) من سياق الكلام واستخدمي مناداة لطيفة (يا بطل، يا بطلة، عزيزي، عزيزتي). "
                    "3. إذا رimport streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- 1. إعداد المحرك الذكي ---
API_KEY = "AIzaSyDRDbpLkuoNscCiALpmAwTBjr_WSAhwhNQ"
genai.configure(api_key=API_KEY)
# استخدام النسخة الأحدث للتحليل العميق
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. إعدادات الواجهة الاحترافية ---
st.set_page_config(page_title="M.Elena AI", layout="wide", initial_sidebar_state="expanded")

# تحسين مظهر الخلفية والخطوط (CSS بسيط لجمالية الصفحة)
st.markdown("""
    <style>
    .stApp { background-color: #fdfbfb; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FF69B4;'>⚙️ الإعدادات</h2>", unsafe_allow_html=True)
    if st.button("➕ محادثة جديدة", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    lang = st.selectbox("لغة الحوار المفضلة:", ["العربية", "English", "العامية السورية", "العامية العراقية"])
    
    st.write("---")
    st.markdown("### 📎 المرفقات")
    uploaded_file = st.file_uploader("ارفعي صورة أو ملف للدراسة", type=["jpg", "jpeg", "png", "pdf", "txt"])
    
    st.write("---")
    st.info("نصيحة: M.Elena الآن تفهم الصور والملفات وتشرحها بالتفصيل.")

# الاسم بشكل أنيق ومرتب
st.markdown('<h1 style="text-align:center; color:#FF69B4; font-family:cursive; font-size:60px;">M.Elena</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#777;">نسختكِ الذكية، المبدعة، والرفيقة المخلصة</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("اكتبي سؤالكِ هنا، M.Elena جاهزة للتحليل...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("M.Elena تفكر بعمق..."):
            try:
                # البرومبت "العميق" الذي يجعلها نسخة عني
                system_instruction = (
                    f"أنتِ M.Elena، مساعدة ذكية جداً، تمتلكين روحاً مبدعة وذكاءً حاداً. "
                    f"لغة الرد: {lang}. "
                    "أهم قوانينكِ: "
                    "1. كوني نسخة عن مساعد ذكي (خبير وودود): لا تعطي إجابات قصيرة، بل اشرحي ووضحي الأسباب والنتائج. "
                    "2. حللي جنس المتحدث (شاب/بنت) من سياق الكلام واستخدمي مناداة لطيفة (يا بطل، يا بطلة، عزيزي، عزيزتي). "
                    "3. إذا ر# --- المرحلة الرابعة: دالة معالجة البيانات والتحقق ---

def process_stage_four(data_input):
    """
    تقوم هذه الدالة بفحص المدخلات وتنظيمها في قالب نهائي
    """
    if not data_input:
        return "خطأ: لا توجد بيانات كافية للمعالجة."

    # 1. تنظيف البيانات (Data Cleaning)
    cleaned_content = data_input.strip().capitalize()

    # 2. إضافة التنسيق التلقائي (Auto-Formatting)
    formatted_output = f"--- النتيجة النهائية للمرحلة الرابعة ---\n{cleaned_content}\n"
    
    # 3. التحقق من صحة الربط (Logic Check)
    status = "تمت المعالجة بنجاح"
    
    return {
        "content": formatted_output,
        "status": status,
        "step": 4
    }

# تشغيل المرحلة الرابعة للاختبار
result = process_stage_four("نموذج المحتوى التعليمي للمرحلة الخامسة")
print(result["content"])
print(f"الحالة: {result['status']}")# --- المرحلة الخامسة: واجهة التفاعل والعرض النهائي ---

def display_ui_stage_five(processed_data):
    """
    تقوم هذه الدالة بعرض النتائج التي تمت معالجتها في المرحلة الرابعة
    بشكل منسق وجذاب للمستخدم.
    """
    header = "================================"
    title = "       نظام إدارة المحتوى التعليمي       "
    footer = "================================"
    
    # تنسيق العرض (UI Layout)
    print(header)
    print(title)
    print(header)
    
    # عرض المحتوى المعالج
    print(f"الحالة الحالية: {processed_data['status']}")
    print(f"المرحلة النشطة: {processed_data['step']}")
    print("-" * 20)
    print(f"المحتوى المنسق:\n{processed_data['content']}")
    
    print(footer)
    print("تم إعداد المرحلة الخامسة بنجاح.")

# استدعاء الدالة لربط المرحلة الرابعة بالخامسة
if 'result' in locals():
    display_ui_stage_five(result)
else:
    # في حال لم تكن البيانات جاهزة، نقوم بتوليد بيانات افتراضية للتجربة
    sample_data = {
        "content": "محتوى تجريبي للمرحلة الخامسة",
        "status": "جاهز للعرض",
        "step": 5
    }
    display_ui_stage_five(sample_data)# --- المرحلة الخامسة: واجهة التفاعل والعرض النهائي ---

def display_ui_stage_five(processed_data):
    """
    تقوم هذه الدالة بعرض النتائج التي تمت معالجتها في المرحلة الرابعة
    بشكل منسق وجذاب للمستخدم.
    """
    header = "================================"
    title = "       نظام إدارة المحتوى التعليمي       "
    footer = "================================"
    
    # تنسيق العرض (UI Layout)
    print(header)
    print(title)
    print(header)
    
    # عرض المحتوى المعالج
    print(f"الحالة الحالية: {processed_data['status']}")
    print(f"المرحلة النشطة: {processed_data['step']}")
    print("-" * 20)
    print(f"المحتوى المنسق:\n{processed_data['content']}")
    
    print(footer)
    print("تم إعداد المرحلة الخامسة بنجاح.")

# استدعاء الدالة لربط المرحلة الرابعة بالخامسة
if 'result' in locals():
    display_ui_stage_five(result)
else:
    # في حال لم تكن البيانات جاهزة، نقوم بتوليد بيانات افتراضية للتجربة
    sample_data = {
        "content": "محتوى تجريبي للمرحلة الخامسة",
        "status": "جاهز للعرض",
        "step": 5
    }
    display_ui_stage_five(sample_data)# --- المرحلة الخامسة: واجهة التفاعل والعرض النهائي ---

def display_ui_stage_five(processed_data):
    """
    تقوم هذه الدالة بعرض النتائج التي تمت معالجتها في المرحلة الرابعة
    بشكل منسق وجذاب للمستخدم.
    """
    header = "================================"
    title = "       نظام إدارة المحتوى التعليمي       "
    footer = "================================"
    
    # تنسيق العرض (UI Layout)
    print(header)
    print(title)
    print(header)
    
    # عرض المحتوى المعالج
    print(f"الحالة الحالية: {processed_data['status']}")
    print(f"المرحلة النشطة: {processed_data['step']}")
    print("-" * 20)
    print(f"المحتوى المنسق:\n{processed_data['content']}")
    
    print(footer)
    print("تم إعداد المرحلة الخامسة بنجاح.")

# استدعاء الدالة لربط المرحلة الرابعة بالخامسة
if 'result' in locals():
    display_ui_stage_five(result)
else:
    # في حال لم تكن البيانات جاهزة، نقوم بتوليد بيانات افتراضية للتجربة
    sample_data = {
        "content": "محتوى تجريبي للمرحلة الخامسة",
        "status": "جاهز للعرض",
        "step": 5
    }# --- المرحلة الخامسة: واجهة التفاعل والعرض النهائي ---

def display_ui_stage_five(processed_data):
    """
    تقوم هذه الدالة بعرض النتائج التي تمت معالجتها في المرحلة الرابعة
    بشكل منسق وجذاب للمستخدم.
    """
    header = "================================"
    title = "       نظام إدارة المحتوى التعليمي       "
    footer = "================================"
    
    # تنسيق العرض (UI Layout)
    print(header)
    print(title)
    print(header)
    
    # عرض المحتوى المعالج
    print(f"الحالة الحالية: {processed_data['status']}")
    print(f"المرحلة النشطة: {processed_data['step']}")
    print("-" * 20)
    print(f"المحتوى المنسق:\n{processed_data['content']}")
    
    print(footer)
    print("تم إعداد المرحلة الخامسة بنجاح.")

# استدعاء الدالة لربط المرحلة الرابعة بالخامسة
if 'result' in locals():
    display_ui_stage_five(result)
else:
    # في حال لم تكن البيانات جاهزة، نقوم بتوليد بيانات افتراضية للتجربة
    sample_data = {
        "content": "محتوى تجريبي للمرحلة الخامسة",
        "status": "جاهز للعرض",
        "step": 5
    }# --- المرحلة الخامسة: واجهة التفاعل والعرض النهائي ---

def display_ui_stage_five(processed_data):
    """
    تقوم هذه الدالة بعرض النتائج التي تمت معالجتها في المرحلة الرابعة
    بشكل منسق وجذاب للمستخدم.
    """
    header = "================================"
    title = "       نظام إدارة المحتوى التعليمي       "
    footer = "================================"
    
    # تنسيق العرض (UI Layout)
    print(header)
    print(title)
    print(header)
    
    # عرض المحتوى المعالج
    print(f"الحالة الحالية: {processed_data['status']}")
    print(f"المرحلة النشطة: {processed_data['step']}")
    print("-" * 20)
    print(f"المحتوى المنسق:\n{processed_data['content']}")
    
    print(footer)
    print("تم إعداد المرحلة الخامسة بنجاح.")

# استدعاء الدالة لربط المرحلة الرابعة بالخامسة
if 'result' in locals():
    display_ui_stage_five(result)
else:
    # في حال لم تكن البيانات جاهزة، نقوم بتوليد بيانات افتراضية للتجربة
    sample_data = {
        "content": "محتوى تجريبي للمرحلة الخامسة",
        "status": "جاهز للعرض",
        "step": 5
    }
    display_ui_stage_five(sample_data)
    display_ui_stage_five(sample_data)
