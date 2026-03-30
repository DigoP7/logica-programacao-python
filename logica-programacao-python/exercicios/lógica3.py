# Exercício: Laços de repetição
# Objetivo: Trabalhar com loops para executar ações repetidas.

melhores_atletas = []

while True:
    nome_atleta = input("Digite o nome do atleta (ou 'fim' para encerrar): ")
    
    if nome_atleta.lower() == 'fim' or nome_atleta == '':
        break

    if nome_atleta.isdigit():
        print("O nome do atleta não pode ser apenas números. Tente novamente.")
        continue
    
    saltos = []
    
    for i in range(5):
        while True:
            try:
                salto = float(input(f"Digite a distância do {i + 1}º salto: "))
                saltos.append(salto)
                break
            except ValueError:
                print("Valor inválido! Digite um número válido para a distância do salto.")
    
    media = sum(saltos) / 5
    
    melhores_atletas.append({
        'nome': nome_atleta,
        'saltos': saltos,
        'media': media
    })

vencedor = melhores_atletas[0]
for atleta in melhores_atletas[1:]:
    if atleta['media'] > vencedor['media']:
        vencedor = atleta

print("\nResultado final:")
print(f"Atleta: {vencedor['nome']}")
print(f"Média dos saltos: {vencedor['media']:.1f} m")
