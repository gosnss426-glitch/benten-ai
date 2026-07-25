import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="BENTEN AI V6.8 Pro", page_icon="⚡", layout="centered"
)

if "theme" not in st.session_state:
  st.session_state.theme = "อนิเมะยามค่ำคืน (Night Anime)"
if "text_color" not in st.session_state:
  st.session_state.text_color = "สีขาวคลาสสิก (White)"
if "sound_effect" not in st.session_state:
  st.session_state.sound_effect = True
if "auto_clear" not in st.session_state:
  st.session_state.auto_clear = False
if "messages" not in st.session_state:
  st.session_state.messages = []

with st.sidebar:
  st.markdown(
      '<h2 style="color: #ffffff !important;">⚙️ ตั้งค่าระบบ V6.8</h2>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p style="color: #38bdf8 !important;">สถานะ: อัปเกรดระบบอาหาร 🟢</p>',
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

  if "ท้องฟ้าและหมู่ดาว" in st.session_state.theme:
    bg_url = "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=1920&auto=format&fit=crop"
  elif "เมืองนีออนไซเบอร์" in st.session_state.theme:
    bg_url = "https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=1920&auto=format&fit=crop"
  elif "ปาสเทลหวานๆ" in st.session_state.theme:
    bg_url = "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1920&auto=format&fit=crop"
  else:
    bg_url = "https://images.unsplash.com/photo-1578632767115-351597cf2477?q=80&w=1920&auto=format&fit=crop"

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

  st.caption("🚀 BENTEN AI V6.8 Pro Edition")

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
    [data-testid="stChatMessage"]:nth-child(odd) p {{
        color: #38bdf8 !important;
    }}
    [data-testid="stChatMessage"] {{
        background-color: rgba(30, 41, 59, 0.85) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
    }}
    [data-testid="stChatInput"] textarea {{
        color: #ffffff !important;
        background-color: rgba(30, 41, 59, 0.9) !important;
        -webkit-text-fill-color: #ffffff !important;
    }}
    [data-testid="stChatInput"] {{
        background-color: transparent !important;
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
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] p, .stSelectbox label, .stCheckbox label {{
        color: #ffffff !important;
    }}
    div[data-baseweb="select"] > div {{
        background-color: #334155 !important;
        color: #ffffff !important;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="main-header">
        <h1>⚡ BENTEN AI V6.8 Pro</h1>
        <p>ระบบอัจฉริยะ พร้อมแนะนำเมนูอาหารอร่อยๆ และพูดคุยได้ทุกสไตล์!</p>
    </div>
""",
    unsafe_allow_html=True,
)

if st.session_state.auto_clear and len(st.session_state.messages) > 10:
  st.warning(
      "⚠️ แชทเริ่มเยอะแล้ว ระบบแนะนำให้กดปุ่ม 'ล้างประวัติการสนทนา' ด้านซ้าย"
      " เพื่อความลื่นไหล!"
  )

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"], unsafe_allow_html=True)

if prompt := st.chat_input("พิมพ์ข้อความคุยกับ AI หรือถามเรื่องของกินที่นี่..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  if st.session_state.sound_effect:
    st.toast("🔔 ส่งข้อความสำเร็จ! ระบบกำลังประมวลผล...", icon="⚡")

  with st.chat_message("assistant"):
    with st.spinner("กำลังเฟ้นหาเมนูเด็ดเวอร์ชัน V6.8..."):
      text = prompt.lower()
      now = datetime.datetime.now()

      # คาแรคเตอร์: สายกวนบาทา
      if "สายกวน" in bot_mode:
        if any(w in text for w in ["หิว", "กิน", "อาหาร", "เมนู", "ข้าว"]):
          bot_reply = f"😏 หิวแล้วหรอจ๊ะพ่อคุณ/แม่คุณ ถามหาของกินเก่งนัก ทำไมไม่กินลมชมวิวแทนล่ะ แฮ่! อะเอาไปเมนูสิ้นคิด: **กะเพราไข่ดาว** สั่งโลด!<br><br><img src='https://media.giphy.com/media/3o7TKSjRrfIPjeiOkM/giphy.gif' width='130'>"
        else:
          gwan_replies = [
              f"😏 หูยยย ถามมาได้ว่า '{prompt}' นึกว่าฉลาด ที่แท้ก็ถามแบบนี้นี่เอง 😜<br><br><img src='https://media.giphy.com/media/3o7TKSjRrfIPjeiOkM/giphy.gif' width='130'>",
              f"🙄 โอ้ยคุณพี่! เรื่อง '{prompt}' เนี่ย ถ้าผมตอบไป เดี๋ยวผมจะดูฉลาดเกินหน้าเกินตาคุณเอาซะเปล่าๆ แฮ่!<br><br><img src='https://media.giphy.com/media/9Jvj4u8w7nL2M/giphy.gif' width='130'>",
              f"🤭 แหม... พิมพ์มาซะยาว แค่จะบอกว่า 'ไม่รู้' แบบมีสไตล์สินะครับ สำหรับเรื่อง '{prompt}' เนี่ย<br><br><img src='https://media.giphy.com/media/13CoXHa88I7v5W/giphy.gif' width='130'>",
          ]
          bot_reply = random.choice(gwan_replies)

      # คาแรคเตอร์: นักให้คำปรึกษา
      elif "นักให้คำปรึกษา" in bot_mode:
        if any(w in text for w in ["หิว", "กิน", "อาหาร", "เมนู", "ข้าว"]):
          bot_reply = f'🧘‍♂️ การเลือกทานอาหารที่ดีต่อสุขภาพและถูกปาก จะช่วยเยียวยาจิตใจและร่างกายได้เป็นอย่างดีเลยนะครับ สำหรับวันนี้ผมขอแนะนำเมนู **"แกงจืดเต้าหู้หมูสับ"** หรือ **"ปลาลวกจิ้ม"** ทานอุ่นๆ สบายท้องแน่นอนครับ ❤️<br><br><img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width="130">'
        else:
          bot_reply = f'🧘‍♂️ จากเรื่อง *"{prompt}"* ที่คุณเล่ามา ผมเข้าใจความรู้สึกเลยนะครับ อยากให้ลองใจเย็นๆ ค่อยๆ คิดทีละสเตปนะครับ มีอะไรผมพร้อมรับฟังและซัพพอร์ตเสมอครับ ❤️<br><br><img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width="130">'

      # คาแรคเตอร์: ผู้ช่วยทั่วไป (แนะนำอาหารเด็ดๆ เพิ่มเติมตรงนี้)
      else:
        if any(w in text for w in ["หิว", "กินอะไรดี", "เมนู", "อาหาร", "ข้าว", "มื้อเที่ยง", "มื้อเย็น", "มื้อเช้า"]):
          food_suggestions = [
              "🍲 **ชาบู / หมูกระทะ:** เยียวยาได้ทุกสิ่ง! นั่งกินเพลินๆ กับคนรู้ใจ ฟินสุดๆ ไปเลย",
              "🍛 **ข้าวผัดกุ้ง / ข้าวคลุกกะปิ:** เมนูจานเดียวทำง่าย หอมอร่อย ครบเครื่อง!",
              "🍜 **ก๋วยเตี๋ยวต้มยำน้ำข้น:** แซ่บถึงใจ ซดน้ำร้อนๆ คล่องคอดีแท้",
              "🥗 **สลัดอกไก่ / อะโวคาโด:** สายสุขภาพต้องจัด เบาท้อง ไม่อ้วน!",
              "🍗 **ส้มตำ ไก่ย่าง ข้าวเหนียว:** อาหารประจำชาติ แซ่บนัวถึงใจ!",
          ]
          chosen_food = random.choice(food_suggestions)
          bot_reply = f"😋 หิวแล้วใช่ไหมครับ! วันนี้ผมขอแนะนำเมนูนี้ให้เลย:\n\n{chosen_food}\n\nอยากให้ผมช่วยหาพิกัดสูตรทำอาหารหรือเมนูอื่นเพิ่มบอกได้เลยนะคร้าบ! 🍳✨<br><br><img src='https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif' width='130'>"
        elif any(w in text for w in ["สวัสดี", "หวัดดี", "hi", "hello", "ดีจ้า"]):
          bot_reply = '🤗 สวัสดีครับคนดี! วันนี้หิวไหม หรือมีเรื่องอะไรเล่าให้ฟังไหม หรืออยากให้ผมช่วยแนะนำเมนูอาหารอ
