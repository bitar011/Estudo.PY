#Práticando Programção Orientada a Objetos utilizando conceitos de biblioteca

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        #ATRIBUTO PROTEGIDO: O status inicial é sempre "disponível"
        self._status = "disponível"

    def emprestar(self):
        #Verifique se status é "disponível"
        if self._status == "disponível":
        #Se for, mude o status para "emprestado" e imprime uma mensagem
            self._status = "emprestado"
            f"{self.titulo} foi emprestado."
        #Se não for (else), imprime uma mensagem de aviso
        else:
            f"O {self.titulo} já está emprestado."
        


    def devolver(self):
        #Verifique se o status é "emprestado"
        if self._status == "emprestado":
        #Se for, muda o status para "disponível" e imprime uma mensagem
            self._status = "disponível"
            f"{self.titulo} foi devolvido."
        #Se não for (else), imprime uma mensagem de aviso
        else:
            f"O {self.titulo} não estava emprestado."
        

    def consultar_status(self):
        #Imprime o título, o autor e o status
        print(f"Livro: {self.titulo} | Autor: {self.autor} | Status: {self._status}")


class Estante:
    def __init__(self):
        #A estante começa com uma lista vazia de livros
        self._livros = []

    def adicionar_livro(self, livro_objeto):
        #Adiciona o 'livro_objeto'
        self._livros.append(livro_objeto)
        print(f"O livro '{livro_objeto.titulo}' foi adicionado à estante.")

    def listar_livros(self):
        print("\n--- Livros na Estante ---")
        
        for livro in self._livros:
            livro.consultar_status()


# --- Área de Testes ---

#1. Cria dois objetos Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro2 = Livro("1984", "George Orwell")

#2. Cria um objeto Estante
minha_estante = Estante()

#3. Adiciona os livros à estante
minha_estante.adicionar_livro(livro1)
minha_estante.adicionar_livro(livro2)

#4. Lista os livros (devem aparecer como "disponível")
#minha_estante.listar_livros()

#5. Empresta o livro1
# print("\n--- Tentando emprestar ---")
livro1.emprestar()

#6. Emprestaa o livro1 novamente (teste do encapsulamento)
livro1.emprestar()

#7.Lista os livros (o livro1 deve aparecer como "emprestado")
#minha_estante.listar_livros()

#8. Devolve o livro1
#print("\n--- Tentando devolver ---")
livro1.devolver()

#9. Devolve o livro1 novamente (teste do encapsulamento)
livro1.devolver()

#10. Lista os livros (o livro1 deve voltar a ser "disponível")
minha_estante.listar_livros()