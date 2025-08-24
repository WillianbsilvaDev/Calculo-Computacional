import psutil
import csv
import time
import datetime

usuario = input("digite o nome do responsável:")
arquivo_csv = "dados-monitoramento-v1.csv.csv"

fieldnames = ["usuario", "timestamp", "cpu", "ram", "disco"]

with open(arquivo_csv, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

while True:
    cpu = psutil.cpu_percent(interval=1)         
    ram = psutil.virtual_memory().percent        
    disco = psutil.disk_usage('/').percent 
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    registro = {
        "usuario": usuario,
        "timestamp": timestamp,
        "cpu": cpu,
        "ram": ram,
        "disco": disco
    }
    with open(arquivo_csv, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(registro)

    print(f"Capturado: {registro}") 
    time.sleep(10)
