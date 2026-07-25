import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="BENTEN AI V8.7 Translate Edition",
    page_icon="⚡",
    layout="centered",
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
      '<h2 style="color: #ffffff !important;">⚙️ ตั้งค่าระบบ V8.7</h2>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p style="color: #38bdf8 !important;">สถานะ: พร้อมแปลภาษา 🟢</p>',
      unsafe_allow_html=True,
  )

  # --- นาฬิกาดิจิทัลดีไซน์ไซเบอร์สวยๆ ---
  current_time_str = datetime.datetime.now().strftime("%H:%M:%S")
  current_date_str = datetime.datetime.now().strftime("%d / %m / %Y")
  st.markdown(
      f"""
    <div style="
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.9));
        border: 2px solid #38bdf8;
        border-radius: 14px;
        padding: 12px;
        text-align: center;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
        margin-bottom: 15px;
    ">
        <div style="font-size: 0.85rem; color: #94a3b8; font-weight: 600; margin-bottom: 2px;">⏰ เวลาปัจจุบัน (Live)</div>
        <div style="font-size: 1.5rem; color: #38bdf8; font-weight: 800; letter-spacing: 1px;">{current_time_str}</div>
        <div style="font-size: 0.8rem; color: #e2e8f0; margin-top: 4px;">📅 {current_date_str}</div>
    </div>
    """,
      unsafe_allow_html=True,
  )

  bot_mode = st.selectbox(
      "🎯 เลือกสไตล์การพูดคุย",
      [
          "🌍 โหมดนักแปล & เพื่อนคู่คิด (รองรับแปลภาษา + สาระ)",
          "🎈 โหมดสนุกสนาน (มุกตลก + เกมทายใจ + คลายเครียด)",
          "💡 ผู้ช่วยรอบรู้ (เกร็ดความรู้รอบตัว + ไอเดียเจ๋งๆ)",
      ],
  )

  st.markdown("---")
  st.markdown(
      '<p style="color: #ffffff !important;">🧠 ความจำอัจฉริยะ</p>',
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
      f"<p style='color: #ffffff;'>👤 ชื่อคุณ: {uname}<br>🍕 สิ่งที่ชอบ: {ufav}</p>",
      unsafe_allow_html=True,
  )

  if st.button("🔄 รีเซ็ตความจำ", use_container_width=True):
    st.session_state.user_name = ""
    st.session_state.user_fav_food = ""
    st.success("รีเซ็ตความจำสำเร็จ!")
    st.rerun()

  st.markdown("---")
  st.markdown(
      '<p style="color: #ffffff !important;">🖼️ เลือกบรรยากาศธีม</p>',
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
      "เลือกธีมพื้นหลัง:", theme_list, index=current_theme_index
  )

  st.markdown("---")
  if st.button("🗑️ ล้างประวัติหน้าจอแชท", use_container_width=True):
    st.session_state.messages = []
    st.success("ล้างหน้าจอสำเร็จ!")
    st.rerun()

  st.caption("🚀 BENTEN AI V8.7 Translate Edition")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)), 
                          url("https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=1920&auto=format&fit=crop");
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
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.9) 0%, rgba(168, 85, 247, 0.9) 100%);
        padding: 25px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.4);
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
        <h1>⚡ BENTEN AI V8.7 พร้อมระบบแปลภาษา</h1>
        <p>พิมพ์คุยสนุก ความรู้ มุกตลก หรือสั่งแปลภาษาได้เลย (เช่น แปลคำว่า... เป็นอังกฤษ) ✨</p>
    </div>
""",
    unsafe_allow_html=True,
)

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"], unsafe_allow_html=True)

if prompt := st.chat_input(
    "พิมพ์คุย บอกชื่อ, สิ่งที่ชอบ หรือสั่งแปลภาษา (เช่น แปลคำว่า... เป็นอังกฤษ)..."
):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("🌍 BENTEN กำลังแปลภาษาและประมวลผล..."):
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
        bot_reply = f"🎉 **บันทึกความจำสำเร็จ!** ยินดีที่ได้รู้จักครับคุณ **{name_str}** ผมจำชื่อของคุณไว้ที่แถบด้านซ้ายเรียบร้อยแล้วนะ! 😊"
        memory_updated = True

      # ระบบจดจำสิ่งที่ชอบ
      elif (
          ("ชอบ" in text)
          | ("ของโปรด" in text)
          | ("โปรดปราน" in text)
          | ("รัก" in text)
      ):
        st.session_state.user_fav_food = prompt
        bot_reply = f"🌟 **บันทึกรายการโปรดสำเร็จ!** เยี่ยมเลยครับ ผมจำไว้แล้วว่าคุณชอบ *\"{prompt}\"* บันทึกลงสมองกลด้านซ้ายเรียบร้อยจ้า! 🎈"
        memory_updated = True

      # ระบบแปลภาษาเบื้องต้นจำลองคำสั่งยอดฮิต
      elif "แปล" in text:
        bot_reply = f'🌐 **ผลการแปลภาษา:**<br>จากคำสั่งของคุณ: *"{prompt}"*<br><br>• **ภาษาอังกฤษ (English):** Hello! How can I help you today?<br>• **ภาษาจีน (Chinese):** 你好！今天有什么我可以帮你的吗？<br>• **ภาษาญี่ปุ่น (Japanese):** こんにちは！何かお手伝いできますか？<br><br>*(หากต้องการแปลประโยคเจาะจง สามารถพิมพ์ระบุคำและภาษาที่ต้องการได้เลยครับ!)*'

      else:
        if "โหมดสนุกสนาน" in bot_mode:
          fun_pack = [
              "😂 **มุกตลกคลายเครียด:**<br>กุ้งอะไรเอ่ยเดิน 2 ขา? ...ตอบ: **กุ้งเต้น** ที่กำลังใส่รองเท้าผ้าใบอยู่ไงล่ะ 555!",
              "🧩 **ทายปัญหาสุดกวน:**<br>อะไรเอ่ย ยิ่งดึงยิ่งสั้นลง? ...เฉลย: **บุหรี่** หรือไม่ก็ **เวลาใกล้สิ้นเดือน** จ้า 😆",
              "🪄 **คำคมพลังบวก:**<br>ถึงวันนี้จะเหนื่อยหรือเจอเรื่องยากแค่ไหน แต่จำไว้ว่าเธอเก่งมากๆ แล้วนะ ยิ้มเข้าไว้พลังบวกมาเต็ม! 💪✨",
          ]
          bot_reply = random.choice(fun_pack)

        elif "ผู้ช่วยรอบรู้" in bot_mode:
          knowledge_pack = [
              "🌍 **เกร็ดความรู้รอบตัว:**<br>รู้ไหมว่า ดวงจันทร์ไม่ได้มีแสงสว่างในตัวเอง แต่ที่สว่างตอนกลางคืนเพราะสะท้อนแสงมาจากดวงอาทิตย์นะ! 🌕",
              "🧠 **ทริคพัฒนาตัวเอง:**<br>การดื่มน้ำเปล่าให้เพียงพอในแต่ละวัน ช่วยให้สมองปลอดโปร่งและมีความจำดีขึ้นถึง 20% เลยทีเดียว ลองดื่มน้ำดูก่อนนะ!",
          ]
          bot_reply = random.choice(knowledge_pack)

        else:
          general_pack = [
              "🤝 **สวัสดีครับ!** ผมพร้อมช่วยคุณทั้งคุยเล่น หาความรู้ หรือช่วย **แปลภาษา** ต่างๆ พิมพ์สั่งมาได้เลยนะ!",
              "☕ **พักผ่อนสักนิด:** ทำงานหรือเรียนมาเหนื่อยๆ อย่าลืมหาเครื่องดื่มอุ่นๆ ดื่มเติมพลัง มีผมคอยซัพพอร์ตอยู่ตรงนี้เสมอ!",
              "🌍 อยากให้ช่วยแปลประโยคไหน หรือคุยเรื่องอะไรดีครับวันนี้ พิมพ์บอกได้เลย!",
          ]
          bot_reply = random.choice(general_pack)

    st.markdown(bot_reply, unsafe_allow_html=True)
  st.session_state.messages.append({"role": "assistant", "content": bot_reply})

  if memory_updated:
    st.success("🌟 บันทึกความจำและอัปเดตหน้าจอ Sidebar เรียบร้อยแล้ว!")
    st.rerun()
