import codificador


def main ():
    bits = codificador.codificador("prueba.txt")
    #print(bits)
    txt = codificador.decodificador(bits)
    #print(txt)
if __name__ == '__main__':
    main()