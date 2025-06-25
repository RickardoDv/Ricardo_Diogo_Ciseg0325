#funcoes com multiplos retornos

v=100

def funcao1(arg1):
    valor_modificado=arg1*2
    valor_original=arg1

    return valor_modificado,valor_original
    pass


modificado, original = funcao1(v)

print("Modificado: "+str(modificado))
print("original: "+str(original))