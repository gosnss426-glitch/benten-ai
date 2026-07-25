import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="BENTEN AI V8.4 Kids & Fun", page_icon="⚡", layout="centered"
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
      '<h2 style="color: #ffffff !important;">⚙️ โหมดเด็กสนุกสนาน</h2>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p style="color: #38bdf8 !important;">สถานะ: พร้อมสร้างรอยยิ้ม 🟢</p>',
      unsafe_allow_html=True,
  )

  bot_mode = st.selectbox(
      "🎯 เลือกความสนุกของ AI",
      [
          "🎈 เพื่อนซี้วัยเด็ก (สนุกสนาน + มุกตลก + เกม)",
          "🚀 นักผจญภัยอวกาศ (ตื่นเต้น ผจญภัย)",
          "🦄 ยูนิคอร์นใจดี (อบอุ่น นุ่มฟู น่ารัก)",
      ],
  )

  st.markdown("---")
  st.markdown(
      '<p style="color: #ffffff !important;">🧠 ความจำของเพื่อนซี้</p>',
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
      f"<p style='color: #ffffff;'>👤 ชื่อเพื่อน: {uname}<br>🍕 ของโปรด: {ufav}</p>",
      unsafe_allow_html=True,
  )

  if st.button("🔄 เริ่มความทรงจำใหม่", use_container_width=True):
    st.session_state.user_name = ""
    st.session_state.user_fav_food = ""
    st.success("ล้างความจำสำเร็จ!")
    st.rerun()

  st.markdown("---")
  st.markdown(
      '<p style="color: #ffffff !important;">🖼️ เลือกธีมการ์ตูน</p>',
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
      "เลือกฉากหลัง:", theme_list, index=current_theme_index
  )

  st.markdown("---")
  if st.button("🗑️ ล้างหน้าจอแชท", use_container_width=True):
    st.session_state.messages = []
    st.success("เคลียร์แชทเรียบร้อย!")
    st.rerun()

  st.caption("🚀 BENTEN AI V8.4 Kids Edition")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)), 
                          url("https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
    }}
    .stChatMessage p, .stChatMessage div, .stChatMessage span {{
        color: #ffffff !important;
    }}
    [data-testid="stChatMessage"]:nth-child(odd) p {{
        color: #38bdf8 !important;
    }}
    [data-testid="stChatMessage"] {{
        background-color: rgba(30, 41, 59, 0.85) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
    }}
    [data-testid="stChatInput"] textarea {{
        color: #ffffff !important;
        background-color: rgba(30, 41, 59, 0.9) !important;
        -webkit-text-fill-color: #ffffff !important;
    }}
    .main-header {{
        background: linear-gradient(135deg, rgba(236, 72, 153, 0.9) 0%, rgba(139, 92, 246, 0.9) 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(236, 72, 153, 0.4);
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
        color: white !important;
    }}
    [data-testid="stSidebar"] {{
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }}
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] p {{
        color: #ffffff !important;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="main-header">
        <h1>🎈 BENTEN AI เพื่อนซี้วัยเด็กสุดป่วน!</h1>
        <p>พิมพ์คุยเล่น ทายปัญหา เล่าเรื่องสนุกๆ หรือบอกของโปรดกันเถอะ! ✨</p>
    </div>
""",
    unsafe_allow_html=True,
)

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"], unsafe_allow_html=True)

if prompt := st.chat_input(
    "พิมพ์บอกชื่อ (เช่น ฉันชื่อ...) หรือของโปรด (เช่น ชอบกิน...) หรือชวนคุยได้เลย!"
):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("🚀 กำลังคิดมุกและเรื่องสนุกๆ มาเล่าให้ฟัง..."):
      text = prompt.lower()
      memory_updated = False
      bot_reply = ""

      # ระบบจดจำชื่อ
      if (
          ("ฉันชื่อ" in text)
          | ("ผมชื่อ" in text)
          | ("ชื่อ" in text)
          | ("เรียกผมว่า" in text)
      ):
        words = prompt.split()
        for i, w in enumerate(words):
          if w in ["ชื่อ", "ว่า", "คือ"] and i + 1 < len(words):
            st.session_state.user_name = (
                words[i + 1].replace("!", "").replace(".", "")
            )
            break
        if not st.session_state.user_name and len(words) > 0:
          st.session_state.user_name = words[-1]
        name_str = st.session_state.user_name
        bot_reply = f"🎉 เย้! บันทึกชื่อสำเร็จแล้วครับ! ยินดีต้อนรับสู่แก๊งนะคุณ **{name_str}** ✨ ตอนนี้ผมจำชื่อคุณไว้ที่แถบด้านซ้ายแล้วนะ! 🎈"
        memory_updated = True

      # ระบบจดจำของโปรด
      elif (
          ("ชอบกิน" in text)
          | ("ของโปรด" in text)
          | ("ชอบ" in text)
          | ("โปรดปราน" in text)
      ):
        st.session_state.user_fav_food = prompt
        bot_reply = f"🍕 ว้าว! ของโปรดอร่อยมากๆ เลย ผมจดจำไว้แล้วว่าคุณชอบ *\"{prompt}\"* บันทึกลงสมองกลเรียบร้อยจ้า! 🌟"
        memory_updated = True

      else:
        if "นักผจญภัยอวกาศ" in bot_mode:
          space_tales = [
              "🚀 ☄️ *ยานอวกาศพุ่งทะยาน!* เรากำลังเดินทางผ่านกาแล็กซี่ทางช้างเผือก ระวังอุกกาบาตกันด้วยนะเพื่อน!",
              "👽 🛸 เอเลี่ยนน้อยดาวอังคารฝากความคิดถึงมาบอกเจ้ามนุษย์โลกด้วยนะ ว่าวันนี้กินขนมอะไรรึยัง?",
              "🌟 ลอยเคว้งคว้างในห้วงอวกาศอัน 3 มิติ มีดวงดาวระยิบระยับเป็นเพื่อนแก้เหงา สนุกมั้ยล่ะ!",
          ]
          bot_reply = random.choice(space_tales)

        elif "ยูนิคอร์นใจดี" in bot_mode:
          unicorn_tales = [
              "🦄 ✨ ปิ๊งป่อง! มเวทมนตร์แห่งความสุขพุ่งใส่เธอแล้ว ขอให้วันนี้มีแต่เรื่องยิ้มได้กว้างๆ นะ!",
              "🌈 สายรุ้งเจ็ดสีทอประกายสดใส มากินขนมอร่อยๆ ดื่มนมช็อกโกแลตร้อนๆ กันเถอะ นุ่มฟูที่สุดเลย!",
              "💖 ยูนิคอร์นส่งกอดอุ่นๆ ให้หนึ่งที ปลดปล่อยความเครียดแล้วมาเล่นกันให้สนุกนะ!",
          ]
          bot_reply = random.choice(unicorn_tales)

        else:
          # โหมดเพื่อนซี้วัยเด็ก (มีมุกตลก เกมทายปัญหา และเกร็ดความรู้)
          jokes_and_fun = [
              "😂 มุกตลกประจำวัน:<br>ปลาอะไรเอ่ยอยู่ในตู้เย็น? ...**ปลา-ستิก (พลาสติก)** 555 ขำมั้ยเนี่ย!",
              "🧩 มินิเกมทายปัญหา:<br>อะไรเอ่ย ยิ่งตัดยิ่งตัวใหญ่ขึ้น? ...เฉลย: **หลุม** ไงล่ะ เก่งมั้ยเอ่ย! 😆",
              "🦖 เกร็ดความรู้ไดโนเสาร์:<br>รู้มั้ยว่า ทีเร็กซ์ (T-Rex) มีมือสั้นมากๆ จนจับหัวตัวเองไม่ได้ด้วยนะ น่าเอ็นดูสุดๆ!",
              "🪄 มนต์วิเศษประจำวัน:<br>ไม่ว่าเธอจะเจอเรื่องอะไรมา วันนี้เธอเก่งมากๆ แล้วนะ ปรบมือให้ตัวเองหน่อยแปะๆๆ! 👏",
              "🚀 ชวนคุยสนุกๆ:<br>ถ้าเธอมีพลังวิเศษบินได้ อยากจะบินไปเที่ยวที่ไหนเป็นที่แรกดีล่ะ เล่าให้ฟังหน่อยสิ!",
          ]
          bot_reply = random.choice(jokes_and_fun)

    st.markdown(bot_reply, unsafe_allow_html=True)
  st.session_state.messages.append({"role": "assistant", "content": bot_reply})

  if memory_updated:
    st.success("🌟 บันทึกความจำและอัปเดตหน้าจอสำเร็จแล้ว!")
    st.rerun()
