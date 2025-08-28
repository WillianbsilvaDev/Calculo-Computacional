import psutil
import csv

# Lista para armazenar os dados dos processos
processos_info = []

# Itera sobre os processos ativos
for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
    try:
        pid = proc.info['pid']
        nome = proc.info['name']
        mem = proc.info['memory_info'].rss / (1024 * 1024)  # memória em MB

        processos_info.append({
            "pid": pid,
            "nome": nome,
            "memoria_mb": round(mem, 2)
        })

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass  # Processo pode ter terminado ou estar inacessível

# Salvar dados dos processos em CSV
with open("processos.csv", "w", newline="", encoding='utf-8') as csvfile:
    campos = ["pid", "nome", "memoria_mb"]
    escritor = csv.DictWriter(csvfile, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(processos_info)

print("CSV de processos salvo com sucesso.")

# Captura do uso da rede (bytes enviados e recebidos)
rede = psutil.net_io_counters()

rede_info = [{
    "bytes_enviados": rede.bytes_sent,
    "bytes_recebidos": rede.bytes_recv,
    "pacotes_enviados": rede.packets_sent,
    "pacotes_recebidos": rede.packets_recv
}]

# Salvar dados de rede em CSV
with open("rede.csv", "w", newline="", encoding='utf-8') as csvfile:
    campos = ["bytes_enviados", "bytes_recebidos", "pacotes_enviados", "pacotes_recebidos"]
    escritor = csv.DictWriter(csvfile, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(rede_info)

print("CSV de rede salvo com sucesso.")
