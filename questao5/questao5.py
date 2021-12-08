def conversaodeMb(tamanhoMb):
  tamanhoMb = float(tamanhoMb)
  return (tamanhoMb/(1024*1024))
   
def porcentualPorUsuario(lista, total):
  percentual = (lista[2]/total)*100
  lista.insert((len(usuario)),percentual)

def espacoMedio(lista, total):
  media = 0
  elementos = len(lista)
  media = (total)/(elementos+1)
  return media

usuarios = []
indicePessoa = 1
total = media = 0

with open ("usuarios.txt","r") as arquivo:
  valor = 0
  for linha in arquivo:
    usuarios.append(linha.split()) 

  for usuario in usuarios:
    usuario.insert(0,indicePessoa)
    valor = conversaodeMb(usuario[2])
    total += valor
    usuario[len(usuario) - 1] = valor
    indicePessoa+=1
    
  for usuario in usuarios:
    porcentualPorUsuario(usuario, total)

media = espacoMedio(usuario,total)

with open ("relatorio.txt","w") as arquivo:
  arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários.\n")
  arquivo.write("--------------------------------------------------------------\n")
  arquivo.write("Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n\n")
  print(usuarios)
  for usuario in usuarios:
    percentagem="{0:.2f}".format(round(usuario[2],2))
    arquivo.write(str(usuario[0])+'\t'+"{:<15}".format(usuario[1])+'\t'+"{:<16}".format(percentagem)+'MB'+'\t'+"{0:.2f}".format(usuario[3])+'%'+'\n')

  arquivo.write('\n\nEspaço Total Ocupado: ' + "{0:.2f}".format(total) + ' MB')
  arquivo.write('\n\nEspaço médio Ocupado: ' + "{0:.2f}".format(media) + ' MB')
  arquivo.close()

with open ("relatorio.txt","r") as arquivo:
  print(arquivo.read())