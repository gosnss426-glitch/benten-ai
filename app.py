iimport datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บเวอร์ชัน 5.5
st.set_page_config(
    page_title="BENTEN AI - Ultimate Gwan Edition",
    page_icon="😏",
    layout="centered",
)

# แถบเมนูด้านข้าง (Sidebar) แก้ไขให้ตัวหนังสือมองเห็นชัดเจน (บังคับเป็นสีขาว)
with st.sidebar:
  st.markdown(
      '<h2 style="color: #ffffff !important;">⚙️ ควบคุมระบบ</h2>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p style="color: #38bdf8 !important;">สถานะ: พร้อมกวนตลอด 24 ชม. 🟢</p>',
      unsafe_allow_html=True,
  )

  bot_mode = st.selectbox(
      "🎯 เลือกคาแรคเตอร์ AI",
      [
          "สายกวนบาทา (Super Trolling)",
          "สายฮาขำกลิ้ง (Funny)",
          "ผู้ช่วยทั่วไป (Friendly)",
      ],
  )

  st.markdown("---")
  st.markdown(
      '<p style="color: #ffffff !important;">🎨 ปรับแต่งสีหน้าต่าง & ตัวหนังสือ</p>',
      unsafe_allow_html=True,
  )

  bg_theme = st.selectbox(
      "เลือกสีพื้นหลังหน้าต่าง:",
      [
          "ดาร์กมืดเข้ม (Dark Navy)",
          "สว่างสะอาด (Clean White)",
          "เทาโมเดิร์น (Modern Gray)",
      ],
  )

  text_color = st.selectbox(
      "เลือกสีข้อความแชท:",
      [
          "สีขาวคลาสสิก (White)",
          "สีดำเข้มคมชัด (Solid Black)",
          "สีฟ้าสว่างนีออน (Neon Blue)",
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
  else:
    bg_hex = "#0f172a"
    main_text_default = "#f8fafc"

  # แปลงค่าสีตัวหนังสือเป็น CSS Hex
  if "สีดำเข้ม" in text_color:
    selected_hex = "#000000"
  elif "ฟ้าสว่าง" in text_color:
    selected_hex = "#38bdf8"
  elif "เหลืองทอง" in text_color:
    selected_hex = "#fbbf24"
  else:
    selected_hex = main_text_default

  st.markdown("---")
  if st.button("🗑️ ล้างประวัติการสนทนา", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

  st.caption("🚀 BENTEN AI v5.5 - Ultimate Gwan")

# CSS ตกแต่งภาพรวมและบังคับให้ข้อความใน Sidebar เป็นสีขาวทั้งหมดเพื่อให้อ่านง่าย
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_hex};
        color: {main_text_default};
    }}
    
    .stChatMessage p, .stChatMessage div, .stChatMessage span {{
        color: {selected_hex} !important;
    }}
    
    .main-header {{
        background: linear-gradient(135deg, #f43f5e 0%, #8b5cf6 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(244, 63, 94, 0.3);
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

    /* บังคับตัวหนังสือใน Sidebar ทั้งหมดให้เป็นสีขาวและมองเห็นชัดเจน */
    [data-testid="stSidebar"] {{
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }}
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div {{
        color: #ffffff !important;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อหลักตรงกลางหน้าจอ
st.markdown(
    """
    <div class="main-header">
        <h1>😏 BENTEN AI - สายกวนขั้นสุด</h1>
        <p>ผู้ช่วยอัจฉริยะที่พร้อมกวนประสาทคุณได้ตลอดเวลา ฮ่าๆๆ</p>
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
if prompt := st.chat_input("พิมพ์ข้อความมาคุย (หรือมาหาเรื่อง) กับ AI..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("😏 กำลังคิดคำตอบกวนๆ ใส่คุณ..."):
      text = prompt.lower()
      now = datetime.datetime.now()

      # ระบบตอบกลับตามโหมด (เน้นความกวนและฮา)
      if "สายกวน" in bot_mode:
        gwan_replies = [
            f"😏 หูยยย ถามมาได้ว่า '{prompt}' นึกว่าฉลาด ที่แท้ก็ถามแบบนี้นี่เอง 😜",
            (
                f"🙄 โอ้ยคุณพี่! เรื่อง '{prompt}' เนี่ย ถ้าผมตอบไป เดี๋ยวผมจะดูฉลาดเกินหน้าเกินตาคุณ"
                "เอาซะเปล่าๆ แฮ่!"
            ),
            (
                f"🤭 แหม... พิมพ์มาซะยาว แค่จะบอกว่า 'ไม่รู้' แบบมีสไตล์สินะครับ"
                f" สำหรับเรื่อง '{prompt}' เนี่ย"
            ),
            (
                f"🤔 อืมมม... คำถามระดับจักรวาลแบบ '{prompt}' นี่ยังต้องคิดอีก 3 ชาติครึ่งครับถึงจะตอบได้"
                " ฮ่าๆๆ"
            ),
        ]
        bot_reply = random.choice(gwan_replies)

      elif "สายฮา" in bot_mode:
        bot_reply = (
            f"😂 โถถถ นึกว่าเรื่องอะไร ที่แท้ก็เรื่อง '{prompt}' นี่เอง"
            " เอาไป 3 ผ่านความฮาครับคุณพี่!"
        )
      else:
        if any(
            word in text for word in ["สวัสดี", "หวัดดี", "hi", "hello"]
        ):
          bot_reply = "👋 สวัสดีครับคุณผู้ใช้! วันนี้พกความกวนมามากแค่ไหน ปล่อยออกมาให้หมดเลยครับ!"
        elif any(word in text for word in ["เวลา", "กี่โมง"]):
          bot_reply = (
              f"⏰ จะรีบรู้เวลาไปไหนครับเนี่ย ตอนนี้เพิ่งจะ"
              f" {now.strftime('%H:%M น.')} รีบไปนอนหรือจะรีบไปไหนค้าบ?"
          )
        elif any(word in text for word in ["กินอะไรดี", "หิว"]):
          bot_reply = (
              "🍜 หิวก็ไปกินข้าวสครับ มากวนถามผมทำไม เดี๋ยวผมกินแทนแล้วอ้วนนะ"
              " ฮ่าๆๆ!"
          )
        else:
          bot_reply = (
              f"😎 ได้รับข้อความ: *\"{prompt}\"* เรียบร้อยครับผม! "
              "มีอะไรกวนๆ กว่านี้อีกไหม จัดมาได้เลย สู้ตายอยู่แล้ว!"
          )

    st.markdown(bot_reply)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})
