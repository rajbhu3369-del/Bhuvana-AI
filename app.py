
import streamlit as st
import google.generativeai as genai

# தலைப்பு
st.title("⚖️ Buvana AI - சட்ட உதவியாளர்")
st.write("வணக்கம் புவனா! உங்கள் சட்ட ரீதியான சந்தேகங்களை இங்கே கேளுங்கள்.")

# API Key செட்டிங்ஸ் (இதை Streamlit Secrets-ல் வைப்போம்)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# மெசேஜ் பெட்டி
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("இங்கே டைப் செய்யவும்..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
