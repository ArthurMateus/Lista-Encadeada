# Arthur Ferreira da Silva Mateus
# Lucas Gazoni Araújo 
# Sérgio Murilo Moreira Morais
# Henrique Weirich Meurer siegel


class Node:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def add_lista_comeco(self, elemento):
        node_novo = Node(elemento)
        node_novo.proximo = self.inicio
        self.inicio = node_novo

    def add_lista_final(self, elemento):
        node_novo = Node(elemento)
        if not self.inicio:
            self.inicio = node_novo
        else:
            temp = self.inicio
            while temp.proximo:
                temp = temp.proximo
            temp.proximo = node_novo

    def add_lista_especifico(self, elemento, posicao):
        if posicao == 1:
            self.add_lista_comeco(elemento)
            return
        node_novo = Node(elemento)
        temp = self.inicio
        for _ in range(posicao - 2):
            if not temp:
                print("Posição inválida")
                return
            temp = temp.proximo
        if not temp:
            print("Posição inválida")
            return
        node_novo.proximo = temp.proximo
        temp.proximo = node_novo

    def listar_lista(self):
        print('Lista: ', end='')
        temp = self.inicio
        while temp:
            print(temp.elemento, end=" -> ")
            temp = temp.proximo
        print('')

    def listar_elemento_especifico(self, posicao):
        temp = self.inicio
        for _ in range(posicao - 1):
            if not temp:
                print("Posição inválida")
                return
            temp = temp.proximo
        if not temp:
            print("Posição inválida")
        else:
            print(f'O elemento na posição {posicao} é {temp.elemento}')

    def excluir_comeco(self):
        if not self.inicio:
            print('A lista está vazia')
        else:
            self.inicio = self.inicio.proximo

    def excluir_final(self):
        if not self.inicio:
            print('A lista está vazia')
            return
        if not self.inicio.proximo:
            self.inicio = None
        else:
            temp = self.inicio
            while temp.proximo.proximo:
                temp = temp.proximo
            temp.proximo = None

    def excluir_posicao_especifica(self, posicao):
        if posicao == 1:
            self.excluir_comeco()
            return
        temp = self.inicio
        for _ in range(posicao - 2):
            if not temp:
                print('A posição é inválida')
                return
            temp = temp.proximo
        if not temp or not temp.proximo:
            print('A posição é inválida')
            return
        temp.proximo = temp.proximo.proximo

    def excluir_tudo(self):
        self.inicio = None
        print('Todos os elementos da lista foram excluídos')

def main():
    lista = ListaEncadeada()
    while True:
        print('------------------------------------------------------------------')
        print('                         Menu de Opções                           ')
        print("------------------------------------------------------------------")
        print("[1] Adicionar no início da lista")
        print("[2] Adicionar no final da lista")
        print("[3] Adicionar em um ponto específico da lista")
        print("[4] Listar todos os elementos da lista")
        print("[5] Listar um elemento específico da lista")
        print("[6] Excluir do início da lista")
        print("[7] Excluir do final da lista")
        print("[8] Excluir de um ponto específico da lista")
        print("[9] Liberar os elementos e mostrar a lista vazia")
        print("[0] Terminar")
        print("------------------------------------------------------------------")
        opcao = int(input("Qual a sua opção? "))
        if opcao == 1:
            data = int(input("Digite o valor a ser adicionado no início: "))
            lista.add_lista_comeco(data)
        elif opcao == 2:
            data = int(input("Digite o valor a ser adicionado no final: "))
            lista.add_lista_final(data)
        elif opcao == 3:
            data = int(input("Digite o valor a ser adicionado: "))
            posicao = int(input("Digite a posição onde o valor deve ser adicionado: "))
            lista.add_lista_especifico(data, posicao)
        elif opcao == 4:
            lista.listar_lista()
        elif opcao == 5:
            posicao = int(input("Digite a posição do elemento a ser listado: "))
            lista.listar_elemento_especifico(posicao)
        elif opcao == 6:
            lista.excluir_comeco()
        elif opcao == 7:
            lista.excluir_final()
        elif opcao == 8:
            posicao = int(input("Digite a posição do elemento a ser excluído: "))
            lista.excluir_posicao_especifica(posicao)
        elif opcao == 9:
            lista.excluir_tudo()
        elif opcao == 0:
            print("Terminando o programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()