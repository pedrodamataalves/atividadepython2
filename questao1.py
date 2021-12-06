nome   = ""
saltos = []
somatorio  = 0

nome = input("Informe o nome do atleta: ")
print(nome)

for cont in range(0, 5):
  salto_dist = input(f"Informe a distancia do {cont + 1} salto: ")
  saltos.append(float(salto_dist))


print("Resultado final:")

print("Atleta: " + nome)

print("Saltos: ")
for salto in saltos:
  somatorio = somatorio + salto #somatorio
  print(f"{salto} - ", end="")

media = somatorio / len(saltos)

print(f"A média dos saltos foi de: {media}" )