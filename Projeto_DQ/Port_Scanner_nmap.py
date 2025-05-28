import nmap
import sys

# Função para fazer o scan
def advanced_port_scanner(target, port_range):
    # Inicializa o Nmap PortScanner
    nm = nmap.PortScanner()

    # Faz o scan
    try:
        nm.scan(target, port_range)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

    # Mostra os resultados
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")

            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}\tService: {nm[host][proto][port]['name']}")

if __name__ == "__main__":
    # Replace with your target hostname or IP address
    target = "###"

    # Define the range of ports to scan (e.g., "1-1024" for ports 1 to 1024)
    port_range = "1-1024"

    advanced_port_scanner(target, port_range)