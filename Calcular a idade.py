from datetime import date
ano_nascimento_str = input("Digite o ano de seu nascimento (ex: 1990): ")
ano_nascimento = int(ano_nascimento_str)
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f"Sua idade é: {idade} anos")