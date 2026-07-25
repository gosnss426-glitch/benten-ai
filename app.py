import datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บเวอร์ชัน 5
st.set_page_config(
    page_title="BENTEN AI - Version 5.0", page_icon="🚀", layout="centered"
)

# แถบเมนูด้านข้าง (Sidebar) พร้อมเมนูเปลี่ยนสีหน้าต่างและสีตัวหนังสือ
with st.sidebar:
  st.title("⚙️ ควบคุมระบบ v5")
  st.write("สถานะ: **ออนไลน์ 🟢**")

  bot_mode = st.selectbox(
      "🎯 เลือกคาแรคเตอร์ AI",
      ["ผู้ช่วยทั่วไป (Friendly)", "สายฮาอารมณ์ดี (Funny)", "นักให้คำปรึกษา (Wise)"],
  )

  st.markdown("---")
  st.subheader("🎨 ปรับแต่งสีหน้าต่างและตัวหนังสือ")

  # ให้เลือกสีพื้นหลังหน้าต่างแอป
  bg_theme = st.selectbox(
      "เลือกสีพื้นหลังหน้าต่าง:",
      [
          "ดาร์กมืดเข้ม (Dark Navy)",
          "สว่างสะอาด (Clean White)",
          "เทาโมเดิร์น (Modern Gray)",
          "ชมพูพาสเทลอ่อน (Soft Pink)",
      ],
  )

  # ให้เลือกสีตัวหนังสือ
  text_color = st.selectbox(
      "เลือกสีข้อความแชท:",
      [
          "สีขาวคลาสสิก (White)",
          "สีดำเข้มคมชัด (Solid Black)",
          "สีฟ้าสว่างนีออน (Neon Blue)",
          "สีเขียวมิ้นท์ (Mint Green)",
          "สีเหลืองทอง (Gold)",
      ],
  )

  # แปลงค่าพื้นหลังหน้าต่างเป็น CSS Hex
  if "สว่างสะอาด" in bg_theme:
    bg_hex = "#ffffff"
    main_text_default = "#1e293b"
  elif "เทาโมเดิร์น" in bg_theme:
    bg_hex = "#f1f5f9"
    main_text_default = "#0f172a"
  elif "ชมพูพาสเทล" in bg_theme:
    bg_hex = "#fdf2f8"
    main_text_default = "#831843"
  else:
    bg_hex = "#0f172a"
    main_text_default = "#f8fafc"

  # แปลงค่าสีตัวหนังสือเป็น CSS Hex
  if "สีดำเข้ม" in text_color:
    selected_hex = "#000000"
  elif "ฟ้าสว่าง" in text_color:
    selected_hex = "#38bdf8"
  elif "เขียวมิ้นท์" in text_color:
    selected_hex = "#34d399"
  elif "เหลืองทอง" in text_color:
    selected_hex = "#fbbf24"
  else:
    selected_hex = main_text_default

  st.markdown("---")
  if st.button("🗑️ ล้างประวัติการสนทนา", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

  st.caption("🚀 BENTEN AI v5.0 Ultimate Edition")

# นำค่าสีพื้นหลังและสีตัวหนังสือไปใช้ใน CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_hex};
        color: {main_text_default};
    }}
    
    /* ควบคุมสีตัวหนังสือในกล่องแชท */
    .stChatMessage p, .stChatMessage div, .stChatMessage span {{
        color: {selected_hex} !important;
    }}
    
    .main-header {{
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
    }}
    
    .main-header h1 {{
        margin: 0;
        font-size: 2.2rem;
        font-weight: 800;
        color: white !important;
    }}
    
    .main-header p {{
        margin: 8px 0 0 0;
        font-size: 1.05rem;
        opacity: 0.95;
        color: white !important;
    }}

    [data-testid="stSidebar"] {{
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }}
    [data-testid="stSidebar"] * {{
        color: #f8fafc !important;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อหลักตรงกลางหน้าจอ
st.markdown(
    """
    <div class="main-header">
        <h1>🚀 BENTEN AI - v5.0</h1>
        <p>ระบบผู้ช่วยอัจฉริยะ ปรับแต่งสีหน้าต่างและสีตัวหนังสือได้ตามใจชอบ</p>
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
        if any(
            word in text for word in ["สวัสดี", "หวัดดี", "hi", "hello"]
        ):
          bot_reply = "👋 สวัสดีครับ! หากมองไม่เห็นตัวหนังสือ สามารถไปเปลี่ยนสีพื้นหลังหน้าต่างหรือสีตัวหนังสือได้ที่เมนูด้านซ้ายเลยครับ!"
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
          bot_reply = f"✨ ได้รับข้อความเวอร์ชัน v5 แล้ว: *\"{prompt}\"* ปรับสีหน้าต่างอ่านง่ายสบายตาขึ้นไหมครับ!"

    st.markdown(bot_reply)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})

