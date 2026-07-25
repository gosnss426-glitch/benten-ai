import random
import streamlit as st

st.title("🤖 BENTEN AI - ที่ปรึกษาส่วนตัว")
st.write("สวัสดีครับ! มีอะไรให้ BENTEN AI ช่วยวันนี้ พิมพ์มาได้เลยครับ")

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
    # คลังคำตอบแบบสุ่มและแยกตามหมวดหมู่คำถาม
    text = prompt.lower()

    if "สวัสดี" in text or "หวัดดี" in text:
      bot_reply = random.choice([
          "สวัสดีครับ! วันนี้มีอะไรให้ผมช่วยดูแลเป็นพิเศษไหมครับ 😊",
          "สวัสดีครับคุณผู้ใช้! พร้อมลุยงานกันต่อเลยไหมครับ",
      ])
    elif "ชื่ออะไร" in text or "เธอคือใคร" in text:
      bot_reply = "ผมคือ BENTEN AI ผู้ช่วยอัจฉริยะส่วนตัวของคุณเองครับ!"
    elif "ทำอะไรได้บ้าง" in text or "ช่วยอะไร" in text:
      bot_reply = (
          "ผมช่วยคุยเป็นเพื่อน ค้นหาไอเดีย ทักทาย หรือตอบคำถามทั่วไปได้ครับ!"
      )
    elif "หิว" in text or "กินอะไรดี" in text:
      bot_reply = random.choice([
          "แนะนำข้าวกะเพราไก่ไข่ดาว หรือส้มตำไก่ย่างเลยครับ กำลังน่ากิน!",
          "ลองหาอะไรร้อนๆ ซดให้ชื่นใจดูสครับ เช่น ก๋วยเตี๋ยวหรือต้มยำ",
      ])
    elif "ขอบใจ" in text or "ขอบคุณ" in text:
      bot_reply = "ด้วยความยินดีเลยครับ มีอะไรให้ช่วยเพิ่มบอกได้เสมอนะครับ! 👍"
    else:
      bot_reply = (
          f"อืม... น่าสนใจมากครับสำหรับเรื่อง '{prompt}'"
          " ไว้ผมจะหาข้อมูลมาเพิ่มให้นะครับ! มีเรื่องอื่นอยากคุยอีกไหมครับ?"
      )

    st.markdown(bot_reply)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})
