import datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="BENTEN AI - Premium UI", page_icon="✨", layout="centered"
)

# ตกแต่ง CSS เพิ่มความสวยงามให้กับตัวหนังสือและหน้าตาแอป
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8F00, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .chat-box {
        padding: 15px;
        border-radius: 12px;
        background-color: #f8f9fa;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 10px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# แสดงผลหัวข้อแบบสวยงาม
st.markdown(
    '<p class="main-title">🤖 BENTEN AI - v4</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="sub-title">✨ ผู้ช่วยอัจฉริยะดีไซน์สุดล้ำ พร้อมสแตนด์บายคุยกับคุณแล้ว</p>',
    unsafe_allow_html=True,
)

# จัดการประวัติการแชท
if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# รับข้อความจากผู้ใช้
if prompt := st.chat_input("พิมพ์ข้อความคุยกับ AI ที่นี่..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("✨ BENTEN กำลังรังสรรค์คำตอบ..."):
      text = prompt.lower()
      now = datetime.datetime.now()

      # 1. เช็คทักทายตามเวลา
      if any(
          word in text for word in ["สวัสดี", "หวัดดี", "hi", "hello", "ดีจ้า"]
      ):
        hour = now.hour
        if 5 <= hour < 12:
          bot_reply = "☀️ **สวัสดีตอนเช้าครับ!** ขอให้วันนี้เป็นวันที่สดใสและเต็มไปด้วยพลังบวกนะครับ"
        elif 12 <= hour < 17:
          bot_reply = "🌤️ **สวัสดีตอนบ่ายครับ!** สู้ๆ กับงานนะ ใกล้จะได้เวลาพักผ่อนแล้ว"
        else:
          bot_reply = "🌙 **สวัสดีตอนค่ำครับ!** วันนี้เหนื่อยไหม ผ่อนคลายความเครียดแล้วพักผ่อนเยอะๆ นะครับ"

      # 2. เช็คเวลาและวันที่
      elif any(word in text for word in ["เวลา", "กี่โมง", "วันที่", "วันอะไร"]):
        thai_days = [
            "วันจันทร์",
            "วันอังคาร",
            "วันพุธ",
            "วันพฤหัสบดี",
            "วันศุกร์",
            "วันเสาร์",
            "วันอาทิตย์",
        ]
        day_name = thai_days[now.weekday()]
        current_time = now.strftime("%H:%M น.")
        current_date = now.strftime("%d/%m/%Y")
        bot_reply = f"📅 แจ้งเตือนเวลาปัจจุบัน: **{day_name} ที่ {current_date}** เวลา **{current_time}** ครับ"

      # 3. ถามชื่อ/ตัวตน
      elif any(word in text for word in ["ชื่ออะไร", "เธอคือใคร", "แนะนำตัว"]):
        bot_reply = "🤖 ผมคือ **BENTEN AI** เวอร์ชันดีไซน์พรีเมียม ออกแบบมาเพื่อสร้างสีสันและช่วยเหลือคุณโดยเฉพาะเลยครับ!"

      # 4. ขอคำคม / ให้กำลังใจ
      elif any(
          word in text
          for word in ["คำคม", "ข้อคิด", "ให้กำลังใจ", "เหนื่อย", "ท้อ"]
      ):
        quotes = [
            "💡 *\"อย่ายอมแพ้ในวันนี้ เพราะพรุ่งนี้อาจเป็นวันของคุณ\"* สู้ๆ ครับ!",
            "💡 *\"ความพยายามไม่เคยทำร้ายใคร ตั้งใจทำเต็มที่ ผลลัพธ์ต้องดีแน่นอน\"*",
        ]
        bot_reply = random.choice(quotes)

      # 5. เรื่องอาหาร
      elif any(word in text for word in ["กินอะไรดี", "หิว", "เมนู"]):
        bot_reply = "🍜 **แนะนำเมนูเด็ดวันนี้:** ข้าวกะเพรากรอบไข่ดาวเยิ้มๆ หรือส้มตำไทยปูปลาร้าแซ่บๆ สักจาน รับรองฟินแน่นอนครับ!"

      # 6. ข้อความทั่วไป
      else:
        bot_reply = f"✨ ได้รับข้อความ: *\"{prompt}\"* เรียบร้อยครับ มีประเด็นไหนอยากให้ผมช่วยขยายความหรือช่วยคิดเพิ่มเติมไหมครับ ถามมาได้เลย!"

    st.markdown(bot_reply)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})
