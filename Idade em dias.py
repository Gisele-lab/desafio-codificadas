name = str(input("Digite seu nome: "))
print("Seja bem vindo, " + name + "!")

idade_em_anos = int(input("Digite sua idade em anos: "))
meses_aniversario = int(input("Digite o número do mês do seu aniversário (1-12): "))
dias_aniversario = int(input("Digite o número do dia do seu aniversário (1-31): "))
idade_em_dias = idade_em_anos * 365 + meses_aniversario * 30 + dias_aniversario
print("Sua idade em dias é:", idade_em_dias)