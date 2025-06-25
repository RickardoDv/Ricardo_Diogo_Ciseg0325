import argparse
import os

cmd_ping = "ping -c"

parser = argparse.ArgumentParser(description="Script para fazer ping")

parser.add_argument('--address', '-a', type=str, required=True, help="Endereco de IP a conectar")
parser.add_argument('--cont', '-c', type=str, required=True, help="Qtd de request")
# parser.add_argument('--port', '-p', type=str, required=True, help="Porta de ligacao")

args = parser.parse_args()

print(args.address)
print(args.cont)

cmd_ping = "ping -c {} {}".format(args.cont, args.address)
print(cmd_ping)

# resposta= os.system(cmd_ping)
resposta = os.popen(cmd_ping).read()
#print(resposta)

if "ttl" in resposta:
    print("[{}] Ligado".format(args.address))
else:
    print("[{}] DesLigado".format(args.address))