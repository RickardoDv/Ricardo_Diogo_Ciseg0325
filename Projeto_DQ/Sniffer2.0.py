from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
import datetime
import socket

# Abrir ficheiro de texto para registo
txt_file = open("sniffer_output.txt", "a")

def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Desconhecido"

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Defaults
        src_port = dst_port = "-"
        protocol_name = "Outro"

        # Verificar protocolo e portas
        if protocol == 1:
            protocol_name = "ICMP"
        elif protocol == 6 and TCP in packet:
            protocol_name = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif protocol == 17 and UDP in packet:
            protocol_name = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            protocol_name = f"Desconhecido ({protocol})"

        # Resolver nomes (opcional)
        src_host = resolve_hostname(src_ip)
        dst_host = resolve_hostname(dst_ip)

        # Timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Criar entrada de log
        log_entry = (
            f"[{timestamp}]\n"
            f"Protocolo: {protocol_name}\n"
            f"Origem: {src_ip}:{src_port} ({src_host})\n"
            f"Destino: {dst_ip}:{dst_port} ({dst_host})\n"
            + "-" * 70 + "\n"
        )

        print(log_entry, end="")              # Mostra no terminal
        txt_file.write(log_entry)             # Grava no ficheiro
        txt_file.flush()

def main():
    try:
        print("[INFO] A capturar pacotes... Pressiona Ctrl+C para parar.\n")
        sniff(prn=packet_callback, filter="ip", store=0)
    except KeyboardInterrupt:
        print("\n[INFO] Captura interrompida pelo utilizador.")
    finally:
        txt_file.close()

if __name__ == "__main__":
    main()
