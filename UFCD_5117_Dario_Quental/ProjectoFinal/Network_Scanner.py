import scapy.all as scapy

def scan(ip_range):
    print(f"Scanning IP range: {ip_range}")
    
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    
    print("Sending ARP requests...")
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=True)[0]
    
    if not answered_list:
        print("No responses received.")
    else:
        print("Responses received.")
    
    devices = []
    for element in answered_list:
        device = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        devices.append(device)
        print(f"Device found: IP = {device['ip']}, MAC = {device['mac']}")
    
    return devices


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