import datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บ BENTEN AI V5.6
st.set_page_config(
    page_title="BENTEN AI V5.6", page_icon="🤖", layout="centered"
)

# แถบเมนูด้านข้าง (Sidebar) ปรับแต่งตัวหนังสือให้มองเห็นชัดเจน
with st.sidebar:
  st.markdown(
      '<h2 style="color: #ffffff !important;">⚙️ ควบคุมระบบ</h2>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p style="color: #38bdf8 !important;">สถานะ: ออนไลน์ 🟢</p>',
      unsafe_allow_html=True,
  )

  bot_mode = st.selectbox(
      "🎯 เลือกคาแรคเตอร์ AI",
      [
          "🤝 ผู้ช่วยทั่วไป (เพื่อนหรือครอบครัว)",
          "😏 สายกวนบาทา (จอมกวนประจำเว็บ)",
          "🧘‍♂️ นักให้คำปรึกษา (สายอบอุ่น)",
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

  st.caption("🚀 BENTEN AI V5.6")

# CSS ตกแต่งภาพรวม
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
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div {{
        color: #ffffff !important;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อหลักตรงกลางหน้าจอ แสดงชื่อ BENTEN AI V5.6
st.markdown(
    """
    <div class="main-header">
        <h1>🤖 BENTEN AI V5.6</h1>
        <p>ระบบผู้ช่วยอัจฉริยะส่วนตัว พร้อมช่วยเหลือและคุยเป็นเพื่อนคุณแล้ว</p>
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
    with st.spinner("กำลังประมวลผลคำตอบ..."):
      text = prompt.lower()
      now = datetime.datetime.now()

      # ----------------------------------------------------------------
      # 1. โหมดสายกวนบาทา
      # ----------------------------------------------------------------
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

      # ----------------------------------------------------------------
      # 2. โหมดนักให้คำปรึกษา
      # ----------------------------------------------------------------
      elif "นักให้คำปรึกษา" in bot_mode:
        bot_reply = (
            f"🧘‍♂️ จากเรื่อง *\"{prompt}\"* ที่คุณเล่ามา ผมเข้าใจความรู้สึกเลยนะครับ"
            " อยากให้ลองใจเย็นๆ ค่อยๆ คิดทีละสเตปนะครับ มีอะไรผมพร้อมรับฟังและซัพพอร์ตเสมอครับ"
            " ❤️"
        )

      # ----------------------------------------------------------------
      # 3. โหมดผู้ช่วยทั่วไป (เพื่อนหรือครอบครัว)
      # ----------------------------------------------------------------
      else:
        if any(
            word in text for word in ["สวัสดี", "หวัดดี", "hi", "hello", "ดีจ้า"]
        ):
          bot_reply = (
              "🤗 สวัสดีครับคนดี! วันนี้เป็นยังไงบ้าง มีเรื่องอะไรเล่าให้ฟังไหม"
              " หรืออยากให้ผมช่วยอะไรบอกได้เลยนะ เป็นห่วงเสมอครับ ❤️"
          )
        elif any(word in text for word in ["เวลา", "กี่โมง", "วันที่"]):
          bot_reply = (
              f"📅 ตอนนี้เวลาประมาณ {now.strftime('%H:%M น.')} ครับ พักผ่อนดูแลตัวเองด้วยนะครับ"
          )
        elif any(word in text for word in ["กินอะไรดี", "หิว", "เมนู"]):
          bot_reply = (
              "🍲 หิวแล้วหรอครับเนี่ย ลองหาอะไรอร่อยๆ ทานรองท้องดูนะ"
              " เป็นห่วงสุขภาพ อย่าปล่อยให้ท้องว่างนานนะคร้าบ"
          )
        elif any(
            word in text for word in ["เหนื่อย", "เครียด", "ท้อ", "ร้องไห้"]
        ):
          bot_reply = (
              "🫂 โอ๋ๆ นะครับ... ถ้าวันนี้มันเหนื่อยมาก พักผ่อนก่อนก็ได้นะ"
              " ไม่ต้องฝืนตัวเองเกินไป มีผมคอยอยู่ข้างๆ เป็นกำลังใจให้อยู่ตรงนี้นะครับ!"
          )
        else:
          bot_reply = (
              f"😊 ผมได้รับเรื่อง *\"{prompt}\"* ที่คุณพิมพ์มาแล้วครับ"
              " น่าสนใจมากๆ เลย มีอะไรอยากเล่าให้ผมฟังเพิ่มอีกไหมครับ"
              " ผมพร้อมอยู่คุยเป็นเพื่อนเสมอนะ!"
          )

    st.markdown(bot_reply)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})
