import os


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


class Arvore:
    def __init__(self):
        self.raiz = None

    def obterraiz(self):
        return self.raiz

    def inserir(self, valor):
        no = No(valor)

        if self.raiz == None:
            self.raiz = no

        else:
            no_atual = self.raiz
            no_pai = None

            while True:
                if no_atual != None:
                    no_pai = no_atual

                    if no.obtervalor() < no_atual.obtervalor():
                        no_atual = no_atual.obteresquerda()

                    else:
                        no_atual = no_atual.obterdireita()

                else:
                    if no.obtervalor() < no_pai.obtervalor():
                        no_pai.setesquerda(no)

                    else:
                        no_pai.setdireita(no)

                    break

    def buscar(self, no_atual):
        if no_atual == None:
            return

        else:
            self.buscar(no_atual.obteresquerda())
            print("[" + str(no_atual.obtervalor()) + "]")
            self.buscar(no_atual.obterdireita())


def opcao():
    os.system("clear")
    print("[1] Inserir\n[2] Mostrar\n[0] Sair")


def main():
    tree = Arvore()

    while True:
        opcao()
        op = input()

        if op == "1":
            print("Valor: ", end=" ")
            valor = input()
            tree.inserir(int(valor))

        elif op == "2":
            tree.buscar(tree.obterraiz())
            input()

        else:
            break


if __name__ == "__main__":
    main()

""" tree.inserir(8)
tree.inserir(3)
tree.inserir(6)
tree.inserir(10)
tree.inserir(14)
tree.inserir(1)
tree.inserir(7)
tree.inserir(13)
tree.inserir(4) """