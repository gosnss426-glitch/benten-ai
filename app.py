import datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บ BENTEN AI V5.6
st.set_page_config(
    page_title="BENTEN AI V5.6", page_icon="🤖", layout="centered"
)

# แถบเมนูด้านข้าง (Sidebar) พร้อมเมนูเลือกพื้นหลัง
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
      '<p style="color: #ffffff !important;">🖼️ เลือกภาพพื้นหลัง</p>',
      unsafe_allow_html=True,
  )

  bg_choice = st.selectbox(
      "เลือกธีมพื้นหลังการ์ตูน:",
      [
          "อนิเมะยามค่ำคืน (Night Anime)",
          "ท้องฟ้าและหมู่ดาว (Starry Sky)",
          "เมืองนีออนไซเบอร์ (Cyberpunk City)",
          "ปาสเทลหวานๆ (Sweet Pastel)",
      ],
  )

  st.markdown("---")
  st.markdown(
      '<p style="color: #ffffff !important;">🎨 ปรับแต่งสีตัวหนังสือ</p>',
      unsafe_allow_html=True,
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

  # กำหนดลิงก์ภาพพื้นหลังตามที่เลือก
  if "ท้องฟ้าและหมู่ดาว" in bg_choice:
    bg_url = "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=1920&auto=format&fit=crop"
  elif "เมืองนีออนไซเบอร์" in bg_choice:
    bg_url = "https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=1920&auto=format&fit=crop"
  elif "ปาสเทลหวานๆ" in bg_choice:
    bg_url = "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1920&auto=format&fit=crop"
  else:
    bg_url = "https://images.unsplash.com/photo-1578632767115-351597cf2477?q=80&w=1920&auto=format&fit=crop"

  # แปลงค่าสีตัวหนังสือเป็น CSS Hex
  if "สีดำเข้ม" in text_color:
    selected_hex = "#000000"
  elif "ฟ้าสว่าง" in text_color:
    selected_hex = "#38bdf8"
  elif "เหลืองทอง" in text_color:
    selected_hex = "#fbbf24"
  else:
    selected_hex = "#ffffff"

  st.markdown("---")
  if st.button("🗑️ ล้างประวัติการสนทนา", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

  st.caption("🚀 BENTEN AI V5.6")

# CSS ใส่พื้นหลังที่ผู้ใช้เลือก พร้อมสติกเกอร์เก๋ๆ
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(15, 23, 42, 0.82), rgba(15, 23, 42, 0.82)), 
                          url("{bg_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
    }}
    
    .stChatMessage p, .stChatMessage div, .stChatMessage span {{
        color: {selected_hex} !important;
    }}
    
    [data-testid="stChatMessage"] {{
        background-color: rgba(30, 41, 59, 0.75) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
    }}
    
    .main-header {{
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.9) 0%, rgba(139, 92, 246, 0.9) 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
        backdrop-filter: blur(5px);
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
        <p>ระบบผู้ช่วยอัจฉริยะส่วนตัว เลือกเปลี่ยนธีมพื้นหลังการ์ตูนได้ตามใจคุณ!</p>
    </div>
""",
    unsafe_allow_html=True,
)

# จัดการประวัติการแชท
if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"], unsafe_allow_html=True)

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
            (
                f"😏 หูยยย ถามมาได้ว่า '{prompt}' นึกว่าฉลาด ที่แท้ก็ถามแบบนี้นี่เอง"
                " 😜\n\n<img"
                ' src="https://media.giphy.com/media/3o7TKSjRrfIPjeiOkM/giphy.gif"'
                ' width="120">'
            ),
            (
                f"🙄 โอ้ยคุณพี่! เรื่อง '{prompt}' เนี่ย ถ้าผมตอบไป"
                " เดี๋ยวผมจะดูฉลาดเกินหน้าเกินตาคุณเอาซะเปล่าๆ แฮ่!\n\n<img"
                ' src="https://media.giphy.com/media/9Jvj4u8w7nL2M/giphy.gif"'
                ' width="120">'
            ),
            (
                f"🤭 แหม... พิมพ์มาซะยาว แค่จะบอกว่า 'ไม่รู้' แบบมีสไตล์สินะครับ"
                f" สำหรับเรื่อง '{prompt}' เนี่ย\n\n<img"
                ' src="https://media.giphy.com/media/13CoXHa88I7v5W/giphy.gif"'
                ' width="120">'
            ),
            (
                f"🤔 อืมมม... คำถามระดับจักรวาลแบบ '{prompt}' นี่ยังต้องคิดอีก"
                " 3 ชาติครึ่งครับถึงจะตอบได้ ฮ่าๆๆ\n\n<img"
                ' src="https://media.giphy.com/media/hvRJCLFzcasvR4ia7z/giphy.gif"'
                ' width="120">'
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
            " ❤️\n\n<img"
            ' src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif"'
            ' width="120">'
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
              " หรืออยากให้ผมช่วยอะไรบอกได้เลยนะ เป็นห่วงเสมอครับ ❤️\n\n<img"
              ' src="https://media.giphy.com/media/xT1XGv8L1E763Bv584/giphy.gif"'
              ' width="120">'
          )
        elif any(word in text for word in ["เวลา", "กี่โมง", "วันที่"]):
          bot_reply = (
              f"📅 ตอนนี้เวลาประมาณ {now.strftime('%H:%M น.')} ครับ พักผ่อนดูแลตัวเองด้วยนะครับ\n\n<img"
              ' src="https://media.giphy.com/media/l0HlRnAWXxn0MhOBK/giphy.gif"'
              ' width="120">'
          )
        elif any(word in text for word in ["กินอะไรดี", "หิว", "เมนู"]):
          bot_reply = (
              "🍲 หิวแล้วหรอครับเนี่ย ลองหาอะไรอร่อยๆ ทานรองท้องดูนะ"
              " เป็นห่วงสุขภาพ อย่าปล่อยให้ท้องว่างนานนะคร้าบ\n\n<img"
              ' src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif"'
              ' width="120">'
          )
        elif any(
            word in text for word in ["เหนื่อย", "เครียด", "ท้อ", "ร้องไห้"]
        ):
          bot_reply = (
              "🫂 โอ๋ๆ นะครับ... ถ้าวันนี้มันเหนื่อยมาก พักผ่อนก่อนก็ได้นะ"
              " ไม่ต้องฝืนตัวเองเกินไป มีผมคอยอยู่ข้างๆ เป็นกำลังใจให้อยู่ตรงนี้นะครับ!\n\n<img"
              ' src="https://media.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif"'
              ' width="120">'
          )
        else:
          bot_reply = (
              f"😊 ผมได้รับเรื่อง *\"{prompt}\"* ที่คุณพิมพ์มาแล้วครับ"
              " น่าสนใจมากๆ เลย มีอะไรอยากเล่าให้ผมฟังเพิ่มอีกไหมครับ"
              " ผมพร้อมอยู่คุยเป็นเพื่อนเสมอนะ!\n\n<img"
              ' src="https://media.giphy.com/media/10Vx9XbXG6w7mU/giphy.gif"'
              ' width="120">'
          )

    st.markdown(bot_reply, unsafe_allow_html=True)

  st.session_state.messages.append({"role": "assistant", "content": bot_reply})
