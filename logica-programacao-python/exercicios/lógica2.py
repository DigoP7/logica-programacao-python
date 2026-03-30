# Exercício: Estruturas condicionais
# Objetivo: Utilizar if/else para tomar decisões com base em condições.

Preço_por_litro = 6.0
NUM_CARS = 5

def le_modelo(i):
	while True:
		s = input(f"Digite o modelo do veiculo {i+1}: ").strip()
		if not s:
			print("Modelo inválido.")
			continue
		# Rejeita entradas que não contenham nenhuma letra (ex.: '123')
		if not any(ch.isalpha() for ch in s):
			print("Modelo inválido. O modelo não pode ser apenas números. Tente novamente (ex.: Gol, Fusca, Fazer, Xj6).")
			continue
		return s

def le_consumo(model):
	while True:
		try:
			v = input(f"Consumo do {model} (km por litro): ").strip()
			consumo = float(v)
			if consumo <= 0:
				print("O consumo deve ser maior que zero.")
				continue
			return consumo
		except ValueError:
			print("Erro digite um número (ex.: 12.5).")

def main():
	modelos = []
	consumos = []

	print("Cadastro de 5 carros\n")
	for i in range(NUM_CARS):
		modelo = le_modelo(i)
		consumo = le_consumo(modelo)
		modelos.append(modelo)
		consumos.append(consumo)

	# Monta lista de registros com índices originais
	registros = []
	for i, (m, c) in enumerate(zip(modelos, consumos), start=1):
		litros = 1000.0 / c
		custo = litros * Preço_por_litro
		registros.append({
			'index': i,
			'model': m,
			'consumo': c,
			'litros': litros,
			'custo': custo,
		})

	# Ordena por consumo (km/l) crescente
	registros_ordenados = sorted(registros, key=lambda r: r['consumo'])

	print("\nRelatório Final")
	print("===============================================")
	for r in registros_ordenados:
		# Formatação para ficar próxima ao exemplo
		idx = r['index']
		model = r['model']
		consumo = r['consumo']
		litros = r['litros']
		custo = r['custo']
		print(f"{idx} - {model:<10} - {consumo:4.1f}  - {litros:7.1f} litros - R$ {custo:,.2f}")

	# Modelo mais econômico -> maior consumo (km/l)
	mais_economico = max(registros, key=lambda r: r['consumo'])
	print("\n>>> O menor consumo é do {}.".format(mais_economico['model']))

if __name__ == '__main__':
	main()

