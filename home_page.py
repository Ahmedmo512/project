import streamlit as st
import time
from PIL import Image

# إعداد صفحة Streamlit
st.set_page_config(
    page_title="WEQAYA - Home",
    page_icon="🩺",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        font-weight: bold;
        color: #D71313;
        text-align: center;
    }
    .subtitle {
        font-size: 24px;
        color: #555;
        text-align: center;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .highlight {
        color: #D71313;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">Welcome to WEQAYA 🩺</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your intelligent healthcare companion for early detection & prevention</p>', unsafe_allow_html=True)

# ---------- IMAGE ----------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    image = Image.open("weqaya.jpg")
    st.image(image, use_container_width=True, caption="**Weqaya: Where Prevention Begins.**")

# ---------- ABOUT SECTION ----------
st.markdown('<div class="info-box">', unsafe_allow_html=True)
about_text = """
**About WEQAYA (وقاية)** 🏥

Weqaya is an intelligent healthcare platform designed to help individuals detect chronic diseases early — such as **hypertension, diabetes, and stroke** — using advanced **artificial intelligence**.

By analyzing user health data, the system provides **instant, data-driven predictions and recommendations**, aiming to raise awareness and support preventive care.

**وقاية** هي منصة رعاية صحية ذكية تهدف إلى مساعدة الأفراد على اكتشاف الأمراض المزمنة مبكرًا — مثل ارتفاع ضغط الدم، والسكري، والسكتة الدماغية — باستخدام تقنيات الذكاء الاصطناعي.

من خلال تحليل بيانات المستخدم الصحية، تقدم المنصة **تنبؤات فورية وتوصيات قائمة على البيانات**، بهدف **تعزيز الوعي ودعم الوقاية.**
"""
st.markdown(about_text)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- BUTTONS ----------
colA, colB, colC = st.columns(3)
with colA:
    st.page_link("pages/hypertension.py", label="🔴 Hypertension Prediction", icon="⚠️")
with colB:
    st.page_link("pages/stroke.py", label="🧠 Stroke Prediction", icon="🧠")
with colC:
    st.page_link("pages/diabetes.py", label="🩸 Diabetes Prediction", icon="💉")

# ---------- FOOTER ANIMATION ----------
st.write("\n")
with st.spinner("Loading platform insights..."):
    time.sleep(1.5)

st.success("Ready to explore predictive healthcare! 🚀")

st.markdown("---")
st.markdown("© 2025 WEQAYA - All rights reserved.", unsafe_allow_html=True)

