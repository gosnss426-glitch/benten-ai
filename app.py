import google.generativeai as genai
import streamlit as st

st.title("🤖 BENTEN AI - ที่ปรึกษาส่วนตัว")
st.write(
    "เชื่อมต่อสมองกล AI ของจริงแล้ว! ถามอะไรก็ได้ที่คุณอยากรู้เลยครับ"
)

GEMINI_API_KEY = "AQ.Ab8RN6LsRgHNBMFR3rur-Ptp2XNCX1hxGibSFWx9NU6hMr6pTQ"

if GEMINI_API_KEY == "วางรหัส API Key ของคุณที่นี่":
  st.warning(
      "⚠️ กรุณานำ Google Gemini API Key มาใส่ในโค้ดบรรทัดที่ 8 ก่อนใช้งานครับ"
  )
else:
  genai.configure(api_key=GEMINI_API_KEY)
  model = genai.GenerativeModel("gemini-1.5-flash")

  if "messages" not in st.session_state:
    st.session_state.messages = []

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if prompt := st.chat_input("พิมพ์ข้อความคุยกับ AI ที่นี่..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
      st.markdown(prompt)

    with st.chat_message("assistant"):
      with st.spinner("กำลังคิดคำตอบ..."):
        try:
          response = model.generate_content(prompt)
          bot_reply = response.text
          st.markdown(bot_reply)
        except Exception as e:
          bot_reply = f"เกิดข้อผิดพลาด: {e}"
          st.error(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

