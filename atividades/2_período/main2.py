# Estrutura de Dados: Lista Encadeada Simples

# Definição do nó
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definição da lista encadeada
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def remove(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    def sum(self):
        elements_sum = 0
        temp = self.head
        while temp:
            elements_sum += temp.data
            temp = temp.next
        return elements_sum
    
    def get_largest(self):
        largest = 0
        temp = self.head
        while temp:
            if largest < temp.data:
                largest = temp.data
            temp = temp.next
        return largest
    
    def get_smallest(self):
        temp = self.head
        smallest = temp.data
        while temp:
            if smallest > temp.data:
                smallest = temp.data
            temp = temp.next
        return smallest

    def insert_at_position(self, data, pos):
        new_node = Node(data)

        if pos == 0:  # inserir no início
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 0
        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Posição inválida!")
            return

        new_node.next = temp.next
        temp.next = new_node

# ----------------------
# Testando o exercício
# ----------------------

lista = LinkedList()

# Inserções
lista.insert_at_end(10)
lista.insert_at_end(20)
lista.insert_at_end(30)
lista.insert_at_beginning(5)
print("Lista após inserções:")
lista.display()

insert_at_position(35,2)

print("Lista após inserções:")
lista.display()


# Removendo um elemento
lista.remove(20)
print("Lista após remover 20:")
lista.display()

# Somando todos os elementos
soma = lista.sum()
print("Soma de todos os elementos da lista:")
print(soma)

# Obtendo o maior elemento da lista
maior = lista.get_largest()
print("Maior elemento da lista:")
print(maior)

# # Obtendo o menor elemento da lista
menor = lista.get_smallest()
print("Menor elemento da lista:")
print(menor)