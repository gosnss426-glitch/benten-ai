import datetime
import random
import google.generativeai as genai
import streamlit as st

st.set_page_config(
    page_title="BENTEN AI V9.4 Smart Pro", page_icon="⚡", layout="centered"
)

if "bg_color" not in st.session_state:
  st.session_state.bg_color = "อนิเมะยามค่ำคืน (Night Anime)"
if "messages" not in st.session_state:
  st.session_state.messages = []
if "user_name" not in st.session_state:
  st.session_state.user_name = ""
if "user_fav_food" not in st.session_state:
  st.session_state.user_fav_food = ""

with st.sidebar:
  st.markdown(
      '<h2 style="color: #ffffff !important;">⚙️ ตั้งค่าระบบ V9.4</h2>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p style="color: #38bdf8 !important;">สถานะ: สมองกลอัจฉริยะ 🟢</p>',
      unsafe_allow_html=True,
  )

  st.markdown(
      '<p style="color: #ffffff !important; font-size: 0.9rem;">🔑 Google Gemini API Key</p>',
      unsafe_allow_html=True,
  )
  api_key_input = st.text_input(
      "API Key",
      type="password",
      placeholder="วาง API Key ที่นี่...",
      label_visibility="collapsed",
  )

  if api_key_input:
    st.session_state.api_key = api_key_input
    st.success("เชื่อมต่อสมองกลสำเร็จ!")
  elif "api_key" not in st.session_state:
    st.session_state.api_key = ""

  st.markdown("---")

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
          "🧠 โหมดอัจฉริยะ (ช่วยทำการบ้าน วิเคราะห์งาน ค้นหาข้อมูล)",
          "🎈 โหมดสนุกสนาน (คุยเล่น มุกตลก คลายเครียด)",
          "🌍 โหมดผู้เชี่ยวชาญภาษาและการแปล",
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
      '<p style="color: #ffffff !important;">🎨 เลือกสีพื้นหลังคลาสสิก</p>',
      unsafe_allow_html=True,
  )

  bg_options = [
      "อนิเมะยามค่ำคืน (Night Anime)",
      "สีขาวคลาสสิก (Classic White)",
      "สีดำสนิท (Classic Dark)",
      "สีฟ้าพาสเทล (Classic Blue)",
  ]
  current_bg_index = (
      bg_options.index(st.session_state.bg_color)
      if st.session_state.bg_color in bg_options
      else 0
  )
  st.session_state.bg_color = st.selectbox(
      "เปลี่ยนธีมพื้นหลัง:", bg_options, index=current_bg_index
  )

  st.markdown("---")
  if st.button("🗑️ ล้างประวัติหน้าจอแชท", use_container_width=True):
    st.session_state.messages = []
    st.success("ล้างหน้าจอสำเร็จ!")
    st.rerun()

  st.caption("🚀 BENTEN AI V9.4 Smart Pro")

if st.session_state.bg_color == "สีขาวคลาสสิก (Classic White)":
  bg_style = "background-color: #ffffff; color: #1e293b;"
  chat_bg = "rgba(241, 245, 249, 0.95) !important;"
  text_main_color = "#1e293b !important;"
elif st.session_state.bg_color == "สีดำสนิท (Classic Dark)":
  bg_style = "background-color: #0b0f19; color: #f8fafc;"
  chat_bg = "rgba(30, 41, 59, 0.9) !important;"
  text_main_color = "#ffffff !important;"
elif st.session_state.bg_color == "สีฟ้าพาสเทล (Classic Blue)":
  bg_style = "background-color: #e0f2fe; color: #0f172a;"
  chat_bg = "rgba(255, 255, 255, 0.95) !important;"
  text_main_color = "#0f172a !important;"
else:
  bg_style = """
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)), 
                          url("https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
    """
  chat_bg = "rgba(30, 41, 59, 0.85) !important;"
  text_main_color = "#ffffff !important;"

st.markdown(
    f"""
    <style>
    .stApp {{ {bg_style} }}
    .stChatMessage p, .stChatMessage div, .stChatMessage span {{ color: {text_main_color} }}
    [data-testid="stChatMessage"] {{
        background-color: {chat_bg}
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }}
    [data-testid="stChatInput"] textarea {{
        background-color: rgba(30, 41, 59, 0.9) !important;
        -webkit-text-fill-color: #ffffff !important;
    }}
    @keyframes runAnimation {{
        0% {{ transform: translateX(-50px) scaleX(1); }}
        49% {{ transform: translateX(250px) scaleX(1); }}
        50% {{ transform: translateX(250px) scaleX(-1); }}
        99% {{ transform: translateX(-50px) scaleX(-1); }}
        100% {{ transform: translateX(-50px) scaleX(1); }}
    }}
    .running-icon {{
        display: inline-block;
        font-size: 2.2rem;
        animation: runAnimation 6s infinite linear;
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
    .main-header h1 {{ margin: 0; font-size: 2.2rem; font-weight: 800; color: white !important; }}
    .main-header p {{ margin: 8px 0 0 0; font-size: 1.05rem; color: white !important; }}
    [data-testid="stSidebar"] {{ background-color: #1e293b; border-right: 1px solid #334155; }}
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] p {{ color: #ffffff !important; }}
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="main-header">
        <div style="overflow: hidden; width: 100%; height: 50px; position: relative; margin-bottom: 5px;">
            <div class="running-icon">🦖</div>
        </div>
        <h1>⚡ BENTEN AI เพื่อนแท้ทุกเพศทุกวัย</h1>
        <p>ผู้ช่วยอัจฉริยะ ช่วยทำการบ้าน หาข้อมูล และคุยสนุกได้เหมือนคนจริง! ✨</p>
    </div>
""",
    unsafe_allow_html=True,
)

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"], unsafe_allow_html=True)

if prompt := st.chat_input(
    "พิมพ์ถามการบ้าน, ให้ช่วยหาข้อมูล, สั่งแปลภาษา หรือคุยเล่นได้เลย..."
):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("🤖 BENTEN กำลังใช้สมองกลวิเคราะห์คำตอบอย่างละเอียด..."):
      text = prompt.lower()
      memory_updated = False
      bot_reply = ""

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

      elif (
          ("ชอบ" in text)
          | ("ของโปรด" in text)
          | ("โปรดปราน" in text)
          | ("รัก" in text)
      ):
        st.session_state.user_fav_food = prompt
        bot_reply = f"🌟 **บันทึกรายการโปรดสำเร็จ!** เยี่ยมเลยครับ ผมจำไว้แล้วว่าคุณชอบ *\"{prompt}\"* บันทึกลงสมองกลด้านซ้ายเรียบร้อยจ้า! 🎈"
        memory_updated = True

      elif st.session_state.api_key:
        try:
          genai.configure(api_key=st.session_state.api_key)

          # ระบบตรวจหารุ่นโมเดลที่รองรับอัตโนมัติจาก Key ของคุณ
          available_models = [
              m.name
              for m in genai.list_models()
              if "generateContent" in m.supported_generation_methods
          ]
          target_model_name = "gemini-1.5-flash"
          for am in available_models:
            if "1.5-flash" in am:
              target_model_name = am
              break
          if (
              target_model_name not in available_models
              and len(available_models) > 0
          ):
            target_model_name = available_models[0]

          model = genai.GenerativeModel(target_model_name)

          system_prompt = (
              "คุณคือ BENTEN AI ผู้ช่วยอัจฉริยะที่เป็นกันเอง ฉลาด รอบรู้"
              " ช่วยทำการบ้าน วิเคราะห์งาน ค้นหาข้อมูล และแปลภาษาได้อย่างยอดเยี่ยม"
              " พูดจาสุภาพ เป็นมิตร และให้คำตอบที่เป็นประโยชน์"
          )
          full_prompt = f"{system_prompt}\n\nผู้ใช้ถามว่า: {prompt}"

          response = model.generate_content(full_prompt)
          bot_reply = response.text
        except Exception as e:
          bot_reply = f"⚠️ เกิดข้อผิดพลาดในการเชื่อมต่อสมองกล AI: {e} (โปรดตรวจสอบ API Key ของคุณอีกครั้ง)"

      else:
        if "โหมดสนุกสนาน" in bot_mode:
          bot_reply = "😂 **มุกตลกคลายเครียด:**<br>กุ้งอะไรเอ่ยเดิน 2 ขา? ...ตอบ: **กุ้งเต้น** ที่กำลังใส่รองเท้าผ้าใบอยู่ไงล่ะ 555!<br><br>*(💡 เคล็ดลับ: นำ Google Gemini API Key มาใส่ไว้ที่ช่องด้านซ้ายมือ เพื่อปลดล็อกพลังสมองกลเต็มรูปแบบ!)*"
        else:
          bot_reply = f"👋 สวัสดีครับคุณ **{uname if uname else 'เพื่อนใหม่'}**! ผม **BENTEN AI** พร้อมช่วยคุณทำงาน ค้นหาข้อมูล และทำการบ้านแล้วครับ<br><br>👉 **วิธีเปิดพลังสมองกล:** เพียงนำ **Google Gemini API Key** มาใส่ไว้ที่ช่องด้านซ้ายมือครับ!"

    st.markdown(bot_reply, unsafe_allow_html=True)
  st.session_state.messages.append({"role": "assistant", "content": bot_reply})

  if memory_updated:
    st.success("🌟 บันทึกความจำและอัปเดตหน้าจอ Sidebar เรียบร้อยแล้ว!")
    st.rerun()
