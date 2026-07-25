import datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="BENTEN AI - Advanced", page_icon="🤖", layout="centered"
)

st.title("🤖 BENTEN AI - อัปเกรดเวอร์ชันพิเศษ")
st.write(
    "สวัสดีครับ! ผมคือ BENTEN AI เวอร์ชันพัฒนาใหม่ พร้อมช่วยเหลือและคุยเป็นเพื่อนคุณแล้วครับ"
)

# จัดการประวัติการแชท
if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# รับข้อความจากผู้ใช้
if prompt := st.chat_input("พิมพ์ข้อความคุยกับ AI หรือสั่งงานที่นี่..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("BENTEN AI กำลังประมวลผล..."):
      text = prompt.lower()
      now = datetime.datetime.now()

      # 1. เช็คทักทายตามเวลา
      if any(
          word in text for word in ["สวัสดี", "หวัดดี", "hi", "hello", "ดีจ้า"]
      ):
        hour = now.hour
        if 5 <= hour < 12:
          time_greet = "สวัสดีตอนเช้าครับ! ขอให้วันนี้เป็นวันที่ดีและสดใสนะครับ ☀️"
        elif 12 <= hour < 17:
          time_greet = "สวัสดีตอนบ่ายครับ สู้ๆ กับงานนะ ลุยกันต่อ! 💪"
        else:
          time_greet = (
              "สวัสดีตอนเย็น/ค่ำครับ วันนี้เหนื่อยไหม พักผ่อนเยอะๆ นะครับ 🌙"
          )
        bot_reply = f"{time_greet} มีอะไรให้ BENTEN ช่วยไหมครับ?"

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
        bot_reply = (
            f"📅 ตอนนี้เป็น {day_name} ที่ {current_date} เวลาประมาณ"
            f" {current_time} ครับ"
        )

      # 3. ถามชื่อ/ตัวตน
      elif any(
          word in text
          for word in ["ชื่ออะไร", "เธอคือใคร", "แนะนำตัว", "ระเบิด"]
      ):
        bot_reply = (
            "ผมคือ **BENTEN AI** ผู้ช่วยอัจฉริยะส่วนตัวของคุณ สร้างขึ้นมาเพื่อเป็น"
            "เพื่อนคุยและช่วยคิดไอเดียต่างๆ ครับ! 🚀"
        )

      # 4. ขอคำคม / มุกตลก
      elif any(
          word in text
          for word in ["คำคม", "ข้อคิด", "ให้กำลังใจ", "เหนื่อย", "ท้อ"]
      ):
        quotes = [
            (
                "💡 *\"ความสำเร็จไม่ได้มาจากการรอคอย แต่มาจากการลงมือทำ\"* สู้ๆ"
                "นะครับ คุณทำได้แน่นอน!"
            ),
            (
                "💡 *\"ทุกๆ วันคือโอกาสใหม่ในการเริ่มต้นใหม่\"* พักผ่อนให้เต็มที่"
                "แล้วลุยต่อครับ!"
            ),
            (
                "💡 *\"อุปสรรคมีไว้ให้ 1000 ข้อ ก็แก้ทีละข้อไปเลยครับ!\"* สู้ตาย!"
            ),
        ]
        bot_reply = random.choice(quotes)

      elif any(word in text for word in ["มุก", "ตลก", "เล่าเรื่องตลก"]):
        jokes = [
            "😂 ทำไมปลาถึงว่ายน้ำหนีฉลาม? เพราะปลาไม่อยากโดน 'ฉลาม' คาบไปทานครับแฮ่!",
            (
                "😂 กาแฟอะไรขมที่สุด? กาแฟที่ไม่มีเธอมาร่วมโต๊ะด้วยไงล่ะ (ง부"
                " ง)"
            ),
        ]
        bot_reply = random.choice(jokes)

      # 5. เรื่องอาหารการกิน
      elif any(word in text for word in ["กินอะไรดี", "หิว", "เมนู", "ของกิน"]):
        menus = [
            "🍜 ลองจัดเมนูเส้นๆ ร้อนๆ เช่น บะหมี่เกี๊ยว หรือก๋วยเตี๋ยวต้มยำดูไหมครับ?",
            "🍛 เมนูสิ้นคิดแต่อร่อยเหาะ: ข้าวกะเพราหมูสับไข่ดาว หรือข้าวผัดกุ้งครับ!",
            "🥗 หรือจะลองแนวเบาๆ สลัดอกไก่ หรือส้มตำไก่ย่าง แซ่บๆ ดีครับ?",
        ]
        bot_reply = random.choice(menus)

      # 6. คำถามทั่วไป / Default ที่ฉลาดขึ้น
      else:
        bot_reply = (
            f"ได้รับข้อความ: *\"{prompt}\"* 🧠\n\nเป็นคำถามที่น่าสนใจมากๆ"
            " ครับ! ไว้ถ้าอยากให้ผมช่วยเจาะลึกเรื่องไหนเพิ่มเติม พิมพ์เจาะจงมาได้เลยนะ"
            "ครับ พร้อมช่วยเสมอ!"
        )

    st.markdown(bot_reply)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})
