import pandas as pd
import sys

personagens = pd.read_json('character.json')
episodios = pd.read_json('episode.json')

quantidadeDepersonagens = personagens['id'].count()
print("1) Há", quantidadeDepersonagens, "personagens na lista.\n")

quantidadeDeHumanos = personagens['species'] == 'Human'
print(f'2) Há {len(personagens[quantidadeDeHumanos])} personagens humanos.\n')

quantidadeAliens = personagens['species'] == 'Alien'
print(f'3) Há {len(personagens[quantidadeAliens])} personagens alienigenas.\n')

alienCondicao = personagens['species'] == 'Alien'
alienCondicao = personagens.loc[alienCondicao]
x = alienCondicao['type'].value_counts()
numero_tipos_alienigena = x.shape
print(f'4) Há {numero_tipos_alienigena[0]} tipos de alienígenas diferentes.\n')

alienCondicao = personagens['species'] == 'Alien'
alien_df = personagens.loc[alienCondicao]
numero_aliens, coluna = alien_df.shape

alienHomemCondicao = alien_df['gender'] == 'Male'
alien_homem_df = alien_df.loc[alienHomemCondicao]
numeroDeAliensHomens, coluna = alien_homem_df.shape

alienMulherCondicao = alien_df['gender'] == 'Female'
alien_mulher_df = alien_df.loc[alienMulherCondicao]
numeroDeAliensMulheres, coluna = alien_mulher_df.shape

print(f'5) Há {numeroDeAliensHomens} homens e {numeroDeAliensMulheres} mulheres alienígenas.\n')

crucobotCondicao = personagens['name'] == 'Crocubot'
crocubot = personagens.loc[crucobotCondicao]
episodio = crocubot['episode']
episodio = episodio[80][0]
episodio = episodio.split('/')
episodio = int(episodio[-1])

print(f'6) O personagem Crocubot aparece no episódio {episodio}.\n')

terraquiosCondicao = personagens['location'] == 'Earth'
terraquios = personagens.loc[terraquiosCondicao]
coluna, qntTerraquios = terraquios.shape

print(f'7) Há {qntTerraquios} personagens que estão em planetas chamado Earth.\n')

alienCondicao = personagens['species'] == 'Alien'
alien = personagens.loc[alienCondicao]
qntEpAliens, coluna= alien.shape

print(f'8) Os personagens da espécie alienígena aparecem em {qntEpAliens} episódios diferentes.\n')