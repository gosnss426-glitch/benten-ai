import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="BENTEN AI V7.8 Pro", page_icon="⚡", layout="centered"
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
if "user_name" not in st.session_state:
  st.session_state.user_name = ""
if "user_fav_food" not in st.session_state:
  st.session_state.user_fav_food = ""

with st.sidebar:
  st.markdown(
      '<h2 style="color: #ffffff !important;">⚙️ ตั้งค่าระบบ V7.8</h2>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p style="color: #38bdf8 !important;">สถานะ: แก้ไขบรรทัดขาด 🟢</p>',
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
      '<p style="color: #ffffff !important;">🧠 ข้อมูลความจำ AI</p>',
      unsafe_allow_html=True,
  )

  uname = (
      st.session_state.user_name if st.session_state.user_name else "ยังไม่ระบุ"
  )
  ufav = (
      st.session_state.user_fav_food
      if st.session_state.user_fav_food
      else "ยังไม่ระบุ"
  )
  st.markdown(
      f"<p style='color: #ffffff;'>👤 ชื่อคุณ: {uname}<br>🍽️ ของโปรด: {ufav}</p>",
      unsafe_allow_html=True,
  )

  if st.button("🔄 รีเซ็ตความจำผู้ใช้", use_container_width=True):
    st.session_state.user_name = ""
    st.session_state.user_fav_food = ""
    st.success("รีเซ็ตความจำสำเร็จ!")
    st.rerun()

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

  st.caption("🚀 BENTEN AI V7.8 Pro Edition")

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
        <h1>⚡ BENTEN AI V7.8 Pro</h1>
        <p>ระบบเสถียร พร้อมใช้งานคุยและตอบกลับปกติ 100%!</p>
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

if prompt := st.chat_input("พิมพ์คุย หรือบอกชื่อ/ของโปรด หรือถามสภาพอากาศได้เลย..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  if st.session_state.sound_effect:
    st.toast("🔔 ส่งข้อความสำเร็จ! ระบบกำลังประมวลผล...", icon="⚡")

  with st.chat_message("assistant"):
    with st.spinner("กำลังประมวลผลเวอร์ชัน V7.8..."):
      text = prompt.lower()
      now = datetime.datetime.now()

      if "ฉันชื่อ" in text or "ผมชื่อ" in text or "ชื่อ" in text:
        words = prompt.split()
        for i, w in enumerate(words):
          if w in ["ชื่อ", "คือ"] and i + 1 < len(words):
            st.session_state.user_name = words[i + 1]
            break
        name_str = (
            st.session_state.user_name if st.session_state.user_name else "คุณ"
        )
        bot_reply = f"📝 จำใส่สมองเรียบร้อย! สวัสดีครับคุณ **{name_str}** ผมจะจดจำชื่อนี้ไว้นะครับ! 😊"

      elif "ชอบกิน" in text or "ของโปรด" in text:
        st.session_state.user_fav_food = prompt
        bot_reply = "🍽️ เยี่ยมเลย! ผมบันทึกของโปรดของคุณเรียบร้อยแล้ว วันหลังหิวจะได้เลือกถูกใจ!"

      elif "อากาศ" in text or "ฝน" in text or "ร้อน" in text:
        weathers = [
            "☀️ อากาศแจ่มใส แดดค่อนข้างแรง เหมาะกับการออกไปข้างนอก แต่อย่าลืมพกครีมกันแดดนะ!",
            "🌧️ มีโอกาสฝนตกฟ้าคะนองในพื้นที่ ออกเดินทางอย่าลืมพกพกร่มหรือเสื้อกันฝนด้วยนะคร้าบ!",
            "⛅ ท้องฟ้ามีเมฆบางส่วน อากาศสบายๆ ไม่ร้อนจัด เหมาะกับการพักผ่อนหย่อนใจ",
            "🌥️ อากาศค่อนข้างครึ้มฟ้าครึ้มฝน ลมพัดเย็นสบาย ระวังสุขภาพกันด้วยนะ!",
        ]
        chosen_weather = random.choice(weathers)
        bot_reply = f"🌍 **รายงานสภาพอากาศจำลอง:**<br>{chosen_weather}"

      else:
        if "สายกวน" in bot_mode:
          if (
              "หิว" in text
              or "กิน" in text
              or "อาหาร" in text
              or "เมนู" in text
              or "ข้าว" in text
          ):
            bot_reply = "😏 หิวหรอ? จัดไป: **กะเพราไข่ดาว** สั่งด่วน!"
          else:
            bot_reply = f"😏 ถามมาได้ว่า '{prompt}' นึกว่าฉลาด 😜"

        elif "นักให้คำปรึกษา" in bot_mode:
          if (
              "หิว" in text
              or "กิน" in text
              or "อาหาร" in text
              or "เมนู" in text
              or "ข้าว" in text
          ):
            bot_reply = (
                '🧘‍♂️ แนะนำ **"แกงจืดเต้าหู้หมูสับ"** ทานอุ่นๆ สบายท้องครับ ❤️'
            )
          else:
            bot_reply = (
                f'🧘‍♂️ จากเรื่อง *"{prompt}"* ค่อยๆ คิดนะ ผมพร้อมซัพพอร์ตเสมอ ❤️'
            )

        else:
          if (
              "หิว" 
