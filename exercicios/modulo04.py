class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f"Livro: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao}"
    
    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return [livro._titulo for livro in livros_disponiveis]

livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "jane Smith", 2020)
livro3 = Livro("As Sobras de Ontem", "Marcelo Vicintin", 2020)

print(livro1)
print(livro2)

livro4 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar o livro: Livro disponível? -> {livro4._disponivel}")
livro4.emprestar()
print(f"Depois de emprestar o livro: Livro disponível? -> {livro3._disponivel}")

Livro.livros = [livro1, livro2, livro3, livro4]
