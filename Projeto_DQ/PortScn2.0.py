import nmap
import sys
import datetime

# Nome do ficheiro de saída
output_filename = "portscan_output.txt"

def advanced_port_scanner(target, port_range):
    nm = nmap.PortScanner()

    try:
        nm.scan(target, port_range)
    except Exception as e:
        print(f"Erro ao executar o Nmap: {e}")
        sys.exit()

    with open(output_filename, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n[Scan iniciado em {timestamp}]\n")
        f.write(f"Alvo: {target} | Intervalo de Portas: {port_range}\n")
        f.write("=" * 70 + "\n")

        for host in nm.all_hosts():
            hostname = nm[host].hostname()
            state = nm[host].state()

            f.write(f"\nHost: {host} ({hostname})\n")
            f.write(f"Estado: {state}\n")

            print(f"\nHost: {host} ({hostname})")
            print(f"Estado: {state}")

            for proto in nm[host].all_protocols():
                f.write(f"\nProtocolo: {proto}\n")
                print(f"\nProtocolo: {proto}")

                ports = sorted(nm[host][proto].keys())
                for port in ports:
                    port_state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    f.write(f"Porta: {port}\tEstado: {port_state}\tServiço: {service}\n")
                    print(f"Porta: {port}\tEstado: {port_state}\tServiço: {service}")

        f.write("\n" + "=" * 70 + "\n")

if __name__ == "__main__":
    target = "127.0.0.1"  # Alvo padrão (localhost). Substituir conforme necessário.
    port_range = "1-1024"  # Intervalo de portas a verificar
    advanced_port_scanner(target, port_range)
