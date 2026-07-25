import datetime
import random
import streamlit as st

st.title("🤖 BENTEN AI v3.0")
st.write("ยินดีต้อนรับสู่เว็บแชตบอต BENTEN AI ครับ! อยากคุยอะไรพิมพ์มาได้เลย")

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("พิมพ์ข้อความของคุณที่นี่..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  msg_clean = prompt.strip()
  msg_lower = msg_clean.lower()

  if msg_lower == "เป็นใคร":
    bot_reply = "ผมคือ AI ที่เขียนด้วยภาษา Python ครับ"
  elif msg_lower == "เวลา":
    current_time = datetime.datetime.now().strftime("%H:%M:%S (%d/%m/%Y)")
    bot_reply = f"เวลาปัจจุบันคือ {current_time}"
  elif msg_lower == "สุ่ม":
    quotes = [
      "ความพยายามอยู่ที่ไหน ความสำเร็จอยู่ที่นั่น",
      "สู้ๆ ครับ วันนี้ต้องเป็นวันของเรา",
      "เก่งมากเลยที่พัฒนา AI ด้วยตัวเอง!",
    ]
    bot_reply = random.choice(quotes)
  elif msg_lower == "help":
    bot_reply = "คำสั่งที่ใช้ได้: 'เป็นใคร', 'เวลา', 'สุ่ม', 'help'"
  else:
    bot_reply = f"BENTEN AI : ขออภัย ผมยังไม่เข้าใจคำว่า '{prompt}'"

  with st.chat_message("assistant"):
    st.markdown(bot_reply)
  st.session_state.messages.append(
      {"role": "assistant", "content": bot_reply}
  )

