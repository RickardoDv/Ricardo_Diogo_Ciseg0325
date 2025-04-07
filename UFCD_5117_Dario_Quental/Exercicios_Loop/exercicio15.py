#Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255)
#e o código correspondente. 
#Dispor de 20 em 20 com a condição de continuação ou saída do programa


for i in range(0, 256, 20):
    print("\nCódigos ASCII de", i, "a", min(i + 19, 255))
    print("-" * 30)
    for j in range(i, min(i + 20, 256)):
        print(f"{j:3} -> {repr(chr(j))}")
    
    resposta = input("\nDeseja continuar? (s para sim / qualquer tecla para sair): ")
    if resposta.lower() != 's':
        print("Programa terminado.")
        break
