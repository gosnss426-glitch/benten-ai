import datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="BENTEN AI -V5", page_icon="💎", layout="centered"
)

# ตกแต่ง CSS หน้าต่างให้สวยงามและพรีเมียม
st.markdown(
    """
    <style>
    /* เปลี่ยนสีพื้นหลังภาพรวมแอป */
    .stApp {
        background-color: #f7f9fc;
    }
    
    /* กล่องหัวข้อหลักแบบไล่ระดับสีและมีเงา */
    .main-header {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(79, 70, 229, 0.2);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 5px 0 0 0;
        font-size: 1rem;
        opacity: 0.9;
    }

    /* ตกแต่งแถบ Sidebar ด้านข้าง */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# แถบเมนูด้านข้าง (Sidebar) สุดหรู
with st.sidebar:
  st.image(
      "https://img.icons8.com/fluency/96/bot.png", width=80
  )  # ไอคอนหุ่นยนต์น่ารักๆ
  st.title("⚙️ แผงควบคุม")
  st.write("สถานะระบบ: **ออนไลน์ 🟢**")

  # เมนูเลือกโหมดการทำงาน
  bot_mode = st.selectbox(
      "🎯 เลือกคาแรคเตอร์ AI",
      ["ผู้ช่วยทั่วไป (Friendly)", "สายฮาอารมณ์ดี (Funny)", "นักให้คำปรึกษา (Wise)"],
  )

  st.markdown("---")
  # ปุ่มเคลียร์แชท
  if st.button("🗑️ ล้างประวัติการสนทนา", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

  st.markdown("---")
  st.caption("🚀 พัฒนาด้วย Streamlit & Python")

# หัวข้อหลักตรงกลางหน้าจอ
st.markdown(
    """
    <div class="main-header">
        <h1>💎 BENTEN AI Pro</h1>
        <p>ระบบผู้ช่วยอัจฉริยะ ดีไซน์ล้ำสมัย พร้อมช่วยเหลือคุณตลอด 24 ชั่วโมง</p>
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
    with st.spinner("กำลังประมวลผลความฉลาด..."):
      text = prompt.lower()

      # ตอบกลับตามโหมดที่เลือกใน Sidebar
      if "สายฮา" in bot_mode:
        bot_reply = f"😂 อุ้ยถามว่า '{prompt}' หรอครับ เอาเป็นว่าขำไว้ก่อน โลกสดใสแน่นอน!"
      elif "นักให้คำปรึกษา" in bot_mode:
        bot_reply = f"🧘‍♂️ จากเรื่อง '{prompt}' ที่คุณกังวล ผมแนะนำให้ค่อยๆ คิดทีละสเตปนะครับ ทุกปัญหามีทางออกเสมอ"
      else:
        bot_reply = f"✨ รับทราบครับ! สำหรับเรื่อง '{prompt}' ผมพร้อมช่วยคุณจัดการเต็มที่เลยครับ มีอะไรให้เจาะลึกเพิ่มไหมครับ?"

    st.markdown(bot_reply)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})
