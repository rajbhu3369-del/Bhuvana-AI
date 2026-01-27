import streamlit as st

# ஆப் தலைப்பு மற்றும் பக்கம் அமைப்பு
st.set_page_config(page_title="Buvana AI", layout="centered")

st.title("⚖️ Buvana AI - சட்ட உதவியாளர்")
st.write("வணக்கம் புவனா! உங்கள் சட்ட ரீதியான சந்தேகங்களை இங்கே கேளுங்கள்.")

# மெசேஜ் பெட்டி
if "messages" not in st.session_state:
    st.session_state.messages = []

# பழைய உரையாடல்களைக் காட்டுதல்
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# பயனர் கேள்வி கேட்கும் இடம்
if prompt := st.chat_input("இங்கே டைப் செய்யவும்..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI-ன் பதில் (உதாரணத்திற்கு)
    response = f"உங்கள் கேள்வி: '{prompt}'. இதற்கான விரிவான பதிலை நான் தயார் செய்கிறேன்..."
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
