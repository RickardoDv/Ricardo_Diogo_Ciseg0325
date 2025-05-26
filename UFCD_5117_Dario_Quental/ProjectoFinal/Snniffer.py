from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Determinar o protocolo
        protocol_name = ""
        if protocol == 1:
            protocol_name = "ICMP"
        elif protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Unknown Protocol"

        # Imprime os detalhes do pacote
        print(f"Protocol: {protocol_name}")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print("-" * 50)

def main():
    # Captura os pacotes na interface de rede default
    sniff(prn=packet_callback, filter="ip", store=0)

if __name__ == "__main__":
    main()



"""


Para escrever em um arquivo, basta o seguinte código:

file = open('file.txt', 'w')
file.write('Seu texto aqui')
file.close()

Lembrando que no código acima, o argumento 'w' sobrescreve tudo que havia no .txt

Para adicionar arquivos sem sobrescrever o conteúdo que o .txt já possui, utilizamos o argumento append na forma:

file = open('file.txt', 'a')
file.write('Seu texto aqui')
file.close()


"""