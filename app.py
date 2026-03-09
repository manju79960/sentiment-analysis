import streamlit as st
from sentiment import analyze_sentiment

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="AI Emotion & Sentiment Analyzer",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# UI Styling
# -------------------------

st.markdown("""
<style>

body {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.main-title{
font-size:50px;
font-weight:800;
text-align:center;
background: linear-gradient(90deg,#00f2fe,#4facfe);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.sub-title{
text-align:center;
font-size:18px;
color:#cbd5f5;
}

.result-card{
padding:25px;
border-radius:18px;
text-align:center;
font-size:28px;
font-weight:bold;
margin-top:20px;
box-shadow:0px 0px 25px rgba(0,0,0,0.3);
}

.metric-box{
background:#1e293b;
padding:18px;
border-radius:12px;
text-align:center;
font-size:20px;
box-shadow:0px 0px 10px rgba(0,0,0,0.4);
}

.footer{
text-align:center;
font-size:16px;
color:#94a3b8;
margin-top:25px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.markdown('<p class="main-title">🤖 Emotion & Sentiment Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Analyze emotions instantly using NLP</p>', unsafe_allow_html=True)

st.write("")

# -------------------------
# Input
# -------------------------

st.write("### ✍ Enter your text")

text = st.text_area("Type a sentence or paragraph", height=150)

# -------------------------
# Analyze
# -------------------------

if st.button("🔍 Analyze Sentiment"):

    if text.strip() == "":
        st.warning("Please enter some text")

    else:

        sentiment, color, compound, pos, neg, neu, emotion = analyze_sentiment(text)

        # Result Card
        st.markdown(
        f'<div class="result-card" style="background:{color}; color:white;">{sentiment}</div>',
        unsafe_allow_html=True)

        st.write("### 🎭 Detected Emotion")
        st.info(emotion)

        st.write("### 📊 Sentiment Strength")

        st.progress((compound + 1) / 2)

        st.write(f"Compound Score: **{compound:.2f}**")

        st.write("### 📈 Sentiment Breakdown")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
            f'<div class="metric-box">😊 Positive<br><b>{pos*100:.1f}%</b></div>',
            unsafe_allow_html=True)

        with col2:
            st.markdown(
            f'<div class="metric-box">😐 Neutral<br><b>{neu*100:.1f}%</b></div>',
            unsafe_allow_html=True)

        with col3:
            st.markdown(
            f'<div class="metric-box">😞 Negative<br><b>{neg*100:.1f}%</b></div>',
            unsafe_allow_html=True)

# Footer

st.markdown("""
<hr>

<div class="footer">
🚀 Built with NLP  
<br>
<b>DSCE | AI & ML</b>
</div>
""", unsafe_allow_html=True)