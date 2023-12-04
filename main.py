def forca_bruta(itens, n, capacidade, melhor_valor, valor_atual, peso_atual, pos, melhor_comb, selecionados):
  # Verifica se é a melhor combinação até agora, caso o item em questão seja o último da lista
  if pos == n:
      if valor_atual > melhor_valor and peso_atual <= capacidade:
          melhor_valor = valor_atual
          for i in range(n):
              melhor_comb[i] = selecionados[i]
      return

  # Inclui o item na combinação
  selecionados[pos] = 1
  valor_atual += itens["valor"][pos]
  peso_atual += itens["peso"][pos]
  forca_bruta(itens, n, capacidade, melhor_valor, valor_atual, peso_atual, pos + 1, melhor_comb, selecionados)

  # Tira o item da combinação
  selecionados[pos] = 0
  valor_atual -= itens["valor"][pos]
  peso_atual -= itens["peso"][pos]
  forca_bruta(itens, n, capacidade, melhor_valor, valor_atual, peso_atual, pos + 1, melhor_comb, selecionados)

def itens_selecionados(melhor_comb, n):
  for i in range(n):
      if melhor_comb[i] == 1:
          print(f"item {i + 1}: selecionado")
      else:
          print(f"item {i + 1}: não selecionado")

def main():
  arquivo = "f8.txt"
  arq = open(arquivo, "r")
  items = 0
  caminhao = 0
  items_disponiveis = {
    "valor":[],
    "peso":[]
  }
  primeiraLinha = True
  for f in arq:
    palavras = f.split()
    if len(palavras) >= 2 and primeiraLinha:
      items, caminhao = int(palavras[0]), int(palavras[1])
      primeiraLinha = not primeiraLinha
    else:
      items_disponiveis["peso"].append(int(palavras[0]))
      items_disponiveis["valor"].append(int(palavras[0]))

  melhor_comb = [0 for i in range(items)]
  selecionados = [0 for i in range(items)]
  melhor_valor = 0
  valor_atual = 0
  peso_atual = 0
  forca_bruta(items_disponiveis, items, caminhao, melhor_valor, valor_atual, peso_atual, 0, melhor_comb, selecionados)
  itens_selecionados(melhor_comb, items)

main()