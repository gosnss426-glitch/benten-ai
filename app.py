import datetime
import random
import streamlit as st

# ตั้งค่าหน้าเว็บ BENTEN AI V6.0 (Ultimate Pro Edition)
st.set_page_config(
    page_title="BENTEN AI V6.0 Pro", page_icon="⚡", layout="centered"
)

# จัดการสถานะการตั้งค่า (State Management) ให้ใช้งานได้จริงทุกปุ่ม
if "theme" not in st.session_state:
  st.session_state.theme = "อนิเมะยามค่ำคืน (Night Anime)"
if "text_color" not in st.session_state:
  st.session_state.text_color = "สีขาวคลาสสิก (White)"
if "sound_effect" not in st.session_state:
  st.session_state.sound_effect = True
if "auto_clear" not in st.session_state:
  st.session_state.auto_clear = False

# แถบเมนูด้านข้าง (Sidebar) สำหรับตั้งค่าที่ใช้งานได้จริง
with st.sidebar:
  st.markdown(
      '<h2 style="color: #ffffff !important;">⚙️ ตั้งค่าระบบ V6.0</h2>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p style="color: #38bdf8 !important;">สถานะ: อัปเกรดเต็มระบบ 🟢</p>',
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

  theme_list = [
      "อนิเมะยามค่ำคืน (Night Anime)",
      "ท้องฟ้าและหมู่ดาว (Starry Sky)",
      "เมืองนีออนไซเบอร์ (Cyberpunk City)",
      "ปาสเทลหวานๆ (Sweet Pastel)",
  ]
  current_theme_index = (
      theme_list.index(st.session_state.theme)
      if st.session_state.theme in theme_list
      else 0
  )
  st.session_state.theme = st.selectbox(
      "เลือกธีมพื้นหลังการ์ตูน:", theme_list, index=current_theme_index
  )

  st.markdown("---")
  st.markdown(
      '<p style="color: #ffffff !important;">🎨 ปรับแต่งสีตัวหนังสือ</p>',
      unsafe_allow_html=True,
  )

  color_list = [
      "สีขาวคลาสสิก (White)",
      "สีดำเข้มคมชัด (Solid Black)",
      "สีฟ้าสว่างนีออน (Neon Blue)",
      "สีเหลืองทอง (Gold)",
  ]
  current_color_index = (
      color_list.index(st.session_state.text_color)
      if st.session_state.text_color in color_list
      else 0
  )
  st.session_state.text_color = st.selectbox(
      "เลือกสีข้อความแชท:", color_list, index=current_color_index
  )

  st.markdown("---")
  st.markdown(
      '<p style="color: #ffffff !important;">🛠️ ลูกเล่นเพิ่มเติม</p>',
      unsafe_allow_html=True,
  )
  st.session_state.sound_effect = st.checkbox(
      "✨ เปิดเอฟเฟกต์เสียงจำลองตอนส่งข้อความ",
      value=st.session_state.sound_effect,
  )
  st.session_state.auto_clear = st.checkbox(
      "🧹 แจ้งเตือนอวยาก็ล้างแชทอัตโนมัติ",
      value=st.session_state.auto_clear,
  )

  # กำหนดลิงก์ภาพพื้นหลังตามค่าที่เลือกจริง
  if "ท้องฟ้าและหมู่ดาว" in st.session_state.theme:
    bg_url = "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=1920&auto=format&fit=crop"
  elif "เมืองนีออนไซเบอร์" in st.session_state.theme:
    bg_url = "https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=1920&auto=format&fit=crop"
  elif "ปาสเทลหวานๆ" in st.session_state.theme:
    bg_url = "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1920&auto=format&fit=crop"
  else:
    bg_url = "https://images.unsplash.com/photo-1578632767115-351597cf2477?q=80&w=1920&auto=format&fit=crop"

  # แปลงค่าสีตัวหนังสือเป็น CSS Hex
  if "สีดำเข้ม" in st.session_state.text_color:
    selected_hex = "#000000"
  elif "ฟ้าสว่าง" in st.session_state.text_color:
    selected_hex = "#38bdf8"
  elif "เหลืองทอง" in st.session_state.text_color:
    selected_hex = "#fbbf24"
  else:
    selected_hex = "#ffffff"

  st.markdown("---")
  if st.button("🗑️ ล้างประวัติการสนทนา", use_container_width=True):
    st.session_state.messages = []
    st.success("ล้างประวัติสำเร็จ!")
    st.rerun()

  st.caption("🚀 BENTEN AI V6.0 Pro Edition")

# CSS นำค่าตั้งค่ามาใช้งานจริงแบบไดนามิก
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)), 
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
        background-color: rgba(30, 41, 59, 0.8) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
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

# หัวข้อหลักตรงกลางหน้าจอ แสดงชื่อ BENTEN AI V6.0 Pro
st.markdown(
    """
    <div class="main-header">
        <h1>⚡ BENTEN AI V6.0 Pro</h1>
        <p>ระบบอัปเกรดใหม่ ตั้งค่าใช้งานได้จริง พร้อมลูกเล่นเสียงเอฟเฟกต์และสติกเกอร์สุดล้ำ!</p>
    </div>
""",
    unsafe_allow_html=True,
)

# จัดการประวัติการแชท
if "messages" not in st.session_state:
  st.session_state.messages = []

# แสดงข้อความแจ้งเตือนถ้าเปิดฟีเจอร์ Auto Clear
if st.session_state.auto_clear and len(st.session_state.messages) > 10:
  st.warning(
      "⚠️ แชทเริ่มเยอะแล้ว ระบบแนะนำให้กดปุ่ม 'ล้างประวัติการสนทนา' ด้านซ้าย"
      " เพื่อความลื่นไหล!"
  )

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"], unsafe_allow_html=True)

# ช่องพิมพ์ข้อความ
if prompt := st.chat_input("พิมพ์ข้อความคุยกับ AI ที่นี่..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # เล่นเอฟเฟกต์เสียงจำลองผ่าน Streamlit ถ้าตั้งค่าไว้
  if st.session_state.sound_effect:
    st.toast("🔔 ส่งข้อความสำเร็จ! ระบบกำลังประมวลผล...", icon="⚡")

  with st.chat_message("assistant"):
    with st.spinner("กำลังประมวลผลคำตอบเวอร์ชัน V6.0..."):
      text = prompt.lower()
      now = datetime.datetime.now()

      # ----------------------------------------------------------------
      # 1. โหมดสายกวนบาทา
      # ----------------------------------------------------------------
      if "สายกวน" in bot_mode:
        gwan_replies = [
            f"😏 หูยยย ถามมาได้ว่า '{prompt}' นึกว่าฉลาด ที่แท้ก็ถามแบบนี้นี่เอง 😜<br><br><img src='https://media.giphy.com/media/3o7TKSjRrfIPjeiOkM/giphy.gif' width='130'>",
            f"🙄 โอ้ยคุณพี่! เรื่อง '{prompt}' เนี่ย ถ้าผมตอบไป เดี๋ยวผมจะดูฉลาดเกินหน้าเกินตาคุณเอาซะเปล่าๆ แฮ่!<br><br><img src='https://media.giphy.com/media/9Jvj4u8w7nL2M/giphy.gif' width='130'>",
            f"🤭 แหม... พิมพ์มาซะยาว แค่จะบอกว่า 'ไม่รู้' แบบมีสไตล์สินะครับ สำหรับเรื่อง '{prompt}' เนี่ย<br><br><img src='https://media.giphy.com/media/13CoXHa88I7v5W/giphy.gif' width='130'>",
            f"🤔 อืมมม... คำถามระดับจักรวาลแบบ '{prompt}' นี่ยังต้องคิดอีก 3 ชาติครึ่งครับถึงจะตอบได้ ฮ่าๆๆ<br><br><img src='https://media.giphy.com/media/hvRJCLFzcasvR4ia7z/giphy.gif' width='130'>",
        ]
        bot_reply = random.choice(gwan_replies)

      # ----------------------------------------------------------------
      # 2. โหมดนักให้คำปรึกษา
      # ----------------------------------------------------------------
      elif "นักให้คำปรึกษา" in bot_mode:
        bot_reply = f'🧘‍♂️ จากเรื่อง *"{prompt}"* ที่คุณเล่ามา ผมเข้าใจความรู้สึกเลยนะครับ อยากให้ลองใจเย็นๆ ค่อยๆ คิดทีละสเตปนะครับ มีอะไรผมพร้อมรับฟังและซัพพอร์ตเสมอครับ ❤️<br><br><img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width="130">'

      # ----------------------------------------------------------------
      # 3. โหมดผู้ช่วยทั่วไป (เพื่อนหรือครอบครัว)
      # ----------------------------------------------------------------
      else:
        if any(
            word in text for word in ["สวัสดี", "หวัดดี", "hi", "hello", "ดีจ้า"]
        ):
          bot_reply = '🤗 สวัสดีครับคนดี! วันนี้เป็นยังไงบ้าง มีเรื่องอะไรเล่าให้ฟังไหม หรืออยากให้ผมช่วยอะไรบอกได้เลยนะ เป็นห่วงเสมอครับ ❤️<br><br><img src="https://media.giphy.com/media/xT1XGv8L1E763Bv584/giphy.gif" width="130">'
        elif any(word in text for word in ["เวลา", "กี่โมง", "วันที่"]):
          bot_reply = (
              f"📅 ตอนนี้เวลาประมาณ {now.strftime('%H:%M น.')}"
              " ครับ พักผ่อนดูแลตัวเองด้วยนะครับ<br><br><img"
              ' src="https://media.giphy.com/media/l0HlRnAWXxn0MhOBK/giphy.gif"'
              ' width="130">'
          )
        elif any(word in text for word in ["กินอะไรดี", "หิว", "เมนู"]):
          bot_reply = '🍲 หิวแล้วหรอครับเนี่ย ลองหาอะไรอร่อยๆ ทานรองท้องดูนะ เป็นห่วงสุขภาพ อย่าปล่อยให้ท้องว่างนานนะคร้าบ<br><br><img src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif" width="130">'
        elif any(
            word in text for word in ["เหนื่อย", "เครียด", "ท้อ", "ร้องไห้"]
        ):
          bot_reply = '🫂 โอ๋ๆ นะครับ... ถ้าวันนี้มันเหนื่อยมาก พักผ่อนก่อนก็ได้นะ ไม่ต้องฝืนตัวเองเกินไป มีผมคอยอยู่ข้างๆ เป็นกำลังใจให้อยู่ตรงนี้นะครับ!<br><br><img src="https://media.giphy.com/media/3oEdv4hwWTzBhWvaU
