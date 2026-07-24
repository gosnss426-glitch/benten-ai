import random
import time

def line():
    print("=========================================")

def get_random_quote():
    quotes = [
        "วันนี้โชคดีแน่นอน!",
        "สู้ๆ นะ พยายามอีกนิด!",
        "เยี่ยมมาก ทำดีแล้ว!",
        "เชื่อมั่นในตัวเอง คุณทำได้!",
        "พักผ่อนบ้างนะ อย่าหักโหมเกินไป"
    ]
    return random.choice(quotes)

def print_help():
    line()
    print("คำสั่งที่สามารถใช้ได้:")
    print("  - สวัสดี")
    print("  - ชื่ออะไร")
    print("  - เป็นใคร")
    print("  - เวลา")
    print("  - สุ่ม")
    print("  - exit (เพื่อออกจากโปรแกรม)")
    line()

def ai(msg):
    msg_clean = msg.strip()
    
    if msg_clean == "สวัสดี":
        print("BENTEN AI : สวัสดีครับ ยินดีต้อนรับ")
    elif msg_clean == "ชื่ออะไร":
        print("BENTEN AI : ผมชื่อ BENTEN AI v3.0")
    elif msg_clean == "เป็นใคร":
        print("BENTEN AI : ผมคือ AI ที่เขียนด้วยภาษา Python 🐍")
    elif msg_clean == "เวลา":
        current_time = time.strftime("%H:%M:%S (%d/%m/%Y)")
        print(f"BENTEN AI : เวลาปัจจุบันคือ {current_time}")
    elif msg_clean == "สุ่ม":
        print(f"BENTEN AI : {get_random_quote()}")
    elif msg_clean.lower() == "help":
        print_help()
    else:
        print(f'BENTEN AI : ขออภัย ผมยังไม่เข้าใจ "{msg}"')

def main():
    line()
    print("        BENTEN AI v3.0 (Python Version)")
    line()
    print("พิมพ์ 'help' เพื่อดูคำสั่งทั้งหมด")
    print("พิมพ์ 'exit' เพื่อออกจากโปรแกรม\n")

    while True:
        try:
            user_input = input("คุณ : ")
        except EOFError:
            break

        if not user_input.strip():
            continue

        if user_input.strip().lower() == "exit":
            print("BENTEN AI : ลาก่อนครับ")
            break

        ai(user_input)
        print()

if __name__ == "__main__":
    main()
