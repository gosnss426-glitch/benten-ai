import datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บเวอร์ชัน 5
st.set_page_config(
    page_title="BENTEN AI - Version 5.0", page_icon="🚀", layout="centered"
)

# ตกแต่ง CSS หน้าต่างให้สวยงามและพรีเมียมยิ่งขึ้น
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    .main-header {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 800;
    }
    
    .main-header p {
        margin: 8px 0 0 0;
        font-size: 1.05rem;
        opacity: 0.95;
    }

    [data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# แถบเมนูด้านข้าง (Sidebar)
with st.sidebar:
  st.title("⚙️ ควบคุมระบบ v5")
  st.write("สถานะ: **ออนไลน์ 🟢 (โหมดอัจฉริยะ)**")

  bot_mode = st.selectbox(
      "🎯 เลือกคาแรคเตอร์ AI",
      ["ผู้ช่วยทั่วไป (Friendly)", "สายฮาอารมณ์ดี (Funny)", "นักให้คำปรึกษา (Wise)"],
  )

  st.markdown("---")
  if st.button("🗑️ ล้างประวัติการสนทนา", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

  st.markdown("---")
  st.caption("🚀 BENTEN AI v5.0 Ultimate Edition")

# หัวข้อหลักตรงกลางหน้าจอ
st.markdown(
    """
    <div class="main-header">
        <h1>🚀 BENTEN AI - v5.0</h1>
        <p>ระบบผู้ช่วยอัจฉริยะรุ่นล่าสุด ดีไซน์ล้ำสมัย ดาร์กโมเดลสุดเท่</p>
    </div>
""",
    unsafe_allow_html=True,
)

# จัดการประวัติการแชท
if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# ช่องพิมพ์ข้อความ
if prompt := st.chat_input("พิมพ์ข้อความคุยกับ AI ที่นี่..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("⚡ v5 กำลังประมวลผลคำตอบ..."):
      text = prompt.lower()
      now = datetime.datetime.now()

      # ระบบตอบกลับตามโหมด
      if "สายฮา" in bot_mode:
        bot_reply = f"😂 โหถามว่า '{prompt}' มาได้ไงเนี่ย เอาเป็นว่าผมให้ผ่านความกวนครับคุณพี่!"
      elif "นักให้คำปรึกษา" in bot_mode:
        bot_reply = f"🧘‍♂️ จากเรื่อง '{prompt}' ที่คุณส่งมา ผมแนะนำให้ตั้งสติ ค่อยๆ แก้ทีละเปลาะ รับรองผ่านไปได้ด้วยดีครับ"
      else:
        # ระบบอัจฉริยะทั่วไปใน v5
        if any(
            word in text for word in ["สวัสดี", "หวัดดี", "hi", "hello"]
        ):
          bot_reply = "👋 สวัสดีครับคุณผู้ใช้! ยินดีต้อนรับสู่ **BENTEN AI v5** มีอะไรให้ผมช่วยวันนี้ไหมครับ?"
        elif any(word in text for word in ["เวลา", "กี่โมง", "วันที่"]):
          bot_reply = (
              f"📅 ขณะนี้เวลา {now.strftime('%H:%M น.')} วันที่"
              f" {now.strftime('%d/%m/%Y')} ครับ"
          )
        elif any(word in text for word in ["กินอะไรดี", "หิว"]):
          bot_reply = (
              "🍜 มื้อนี้แนะนำข้าวมันไก่ หรือก๋วยเตี๋ยวรสเด็ดเลยครับ กำลังหิวพอดี!"
          )
        else:
          bot_reply = f"✨ ได้รับข้อความเวอร์ชัน v5 แล้ว: *\"{prompt}\"* แจ๋วเลยครับ มีอะไรให้ผมช่วยเพิ่มเติมอีกลุยมาได้เลย!"

    st.markdown(bot_reply)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})
