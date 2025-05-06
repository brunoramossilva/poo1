from modulo04 import Livro

livro_bibloteca = Livro("Python in Practice", "Emily Coder", 2021)

livro_bibloteca.emprestar()

print(f"Depois de emprestar (biblioteca): Livro disponível? -> {livro_bibloteca._disponivel}")

ano_especifico = 2020

livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)

print(f"Livros disponíveis em {ano_especifico}: {', '.join(livros_disponiveis_ano)}")
