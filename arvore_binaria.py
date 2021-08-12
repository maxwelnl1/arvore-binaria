class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def obtervalor(self):
        return self.valor

    def obteresquerda(self):
        return self.esquerda

    def obterdireita(self):
        return self.direita

    def setesquerda(self, esquerda):
        self.esquerda = esquerda

    def setdireita(self, direita):
        self.direita = direita


no1 = No(8)
no2 = No(4)
no3 = No(9)
no4 = No(10)
no5 = No(1)

no1.setesquerda(no2)
no1.setdireita(no3)

no3.setdireita(no4)
no2.setesquerda(no5)

print("No1")
print("[" + str(no1.obtervalor()) + "]")
print(no1.obteresquerda().obtervalor(), end=" ")
print(no1.obterdireita().obtervalor())
print()


print("No2")
print("[" + str(no2.obtervalor()) + "]")
print(no2.obteresquerda().obtervalor())
print()


print("No3")
print("[" + str(no3.obtervalor()) + "]")
print(no3.obterdireita().obtervalor())
print()


print("No4")
print("[" + str(no4.obtervalor()) + "]")
print()


print("No5")
print("[" + str(no5.obtervalor()) + "]")
print()
