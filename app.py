# ตรวจสอบว่าเปิดโหมดเล่นเกมอยู่ และผู้เล่นพิมพ์ตัวเลขเข้ามา
if enable_game and prompt.isdigit():
    guess = int(prompt)
    if guess == st.session_state.secret_number:
        bot_reply = f"🎉 เย้! ถูกต้องนะคร้าบ! เลข {guess} คือเลขที่ผมซ่อนไว้เก่งมาก! 🏆 ลองเริ่มเกมใหม่ ผมสุ่มเลข 1-50 ใหม่อีกรอบแล้วนะ"
        st.session_state.secret_number = random.randint(1, 50)
    elif guess < st.session_state.secret_number:
        bot_reply = f"📈 น้อยเกินไป! เลขที่ผมซ่อนไว้ **มากกว่า** {guess} ลองใหม่อีกที!"
    else:
        bot_reply = f"📉 มากเกินไป! เลขที่ผมซ่อนไว้ **น้อยกว่า** {guess} สู้ๆ!"

# ⏰ ดึงการเช็ค "เวลา / วันที่" ขึ้นมาก่อน เพื่อให้ตอบทุกคาแรคเตอร์
elif any(w in text for w in ["เวลา", "กี่โมง", "วันที่", "date", "time"]):
    bot_reply = (
        "📅 เวลาปัจจุบัน "
        + now.strftime("%H:%M น. (วันที่ %d/%m/%Y)")
        + " ครับ มีอะไรให้ผมช่วยเพิ่มเติมไหมเอ่ย? ⏰"
    )

else:
    if "สายกวน" in bot_mode:
        if any(w in text for w in ["หิว", "กิน", "อาหาร", "เมนู", "ข้าว"]):
            bot_reply = "😏 หิวหรอ? จัดไป: **กะเพราไข่ดาว** สั่งด่วน!"
        else:
            bot_reply = f"😏 ถามมาได้ว่า '{prompt}' นึกว่าฉลาด 😜"

    elif "นักให้คำปรึกษา" in bot_mode:
        if any(w in text for w in ["หิว", "กิน", "อาหาร", "เมนู", "ข้าว"]):
            bot_reply = (
                '🧘‍♂️ แนะนำ **"แกงจืดเต้าหู้หมูสับ"** ทานอุ่นๆ สบายท้องครับ ❤️'
            )
        else:
            bot_reply = (
                f'🧘‍♂️ จากเรื่อง *"{prompt}"* ค่อยๆ คิดนะ ผมพร้อมซัพพอร์ตเสมอ ❤️'
            )

    else:
        if any(
            w in text
            for w in [
                "หิว",
                "กินอะไรดี",
                "เมนู",
                "อาหาร",
                "ข้าว",
                "มื้อเที่ยง",
                "มื้อเย็น",
            ]
        ):
            food_suggestions = [
                "🍲 **ชาบู / หมูกระทะ:** เยียวยาได้ทุกสิ่ง ฟินสุดๆ!",
                "🍛 **ข้าวผัดกุ้ง:** เมนูจานเดียวทำง่าย หอมอร่อย!",
                "🍜 **ก๋วยเตี๋ยวต้มยำ:** ซดน้ำร้อนๆ คล่องคอ!",
                "🥗 **สลัดอกไก่:** สายสุขภาพ เบาท้อง ไม่อ้วน!",
                "🍗 **ส้มตำ ไก่ย่าง:** แซ่บนัวถึงใจ!",
            ]
            chosen_food = random.choice(food_suggestions)
            bot_reply = (
                "😋 วันนี้แนะนำเมนูนี้เลย:<br><br>"
                + chosen_food
                + "<br><br>อยากให้หาพิกัดหรือสูตรเพิ่มบอกได้นะ! 🍳✨"
                + "<br><br><img src='https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif'>"
            )
        elif any(
            w in text for w in ["สวัสดี", "หวัดดี", "hi", "hello", "ดีจ้า"]
        ):
            bot_reply = (
                "🤗 สวัสดีครับ! วันนี้หิวไหม หรือมีอะไรให้ช่วยบอกได้เลยนะ ❤️"
            )
        else:
            bot_reply = (
                f'🤖 ได้รับข้อความ: "{prompt}" เรียบร้อยแล้วครับ มีอะไรให้ช่วยอธิบายเพิ่มไหมครับ?'
            )
