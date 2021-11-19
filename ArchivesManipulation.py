#ESCRITA EM ARQUIVOS

arquivo = open("texto.txt", "a")

frases = list()
frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")

arquivo.writelines(frases)

arquivo.close()

#LEITURA EM ARQUIVOS

arquivo = open("texto.txt", "r")

print(arquivo.readlines())

arquivo.close()

""" 
arquivo = open("texto.txt", "r")

print(arquivo.readline(3))

arquivo.close()
"""

#EXEMPLO COM O FECHAMENTO AUTOMÁTICO DO ARQUIVO

with open("texto.txt", "r") as arquivo:
    print(arquivo.readlines())
