# Exercício: Estruturas básicas de lógica
# Objetivo: Praticar uso de variáveis, entrada de dados e operações simples.

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
vendas = []

for i in range(12):
    venda = float(input(f"Digite o número de vendas em {meses[i]}: "))
    vendas.append(venda)

media = sum(vendas) / 12
print(f"\nA média anual de vendas foi: {media:.2f}")

meses_acima = []
for i in range(12):
    if vendas[i] > media:
        meses_acima.append(meses[i])

print("\nMeses com vendas acima da média:")
for mes in meses_acima:
    print(mes)

percentual = (len(meses_acima) / 12) * 100
print(f"\nPercentual de meses com vendas acima da média: {percentual:.1f}%")