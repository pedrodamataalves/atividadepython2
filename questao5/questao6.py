import pandas as pd

personagens = pd.read_json('character.json')
episodios = pd.read_json('episode.json')

quantidadeDepersonagens = personagens['id'].count()
print("1) Há", quantidadeDepersonagens, "personagens na lista.\n")

quantidadeDeHumanos = personagens['species'] == 'Human'
print(f'2) Há {len(personagens[quantidadeDeHumanos])} personagens humanos.\n')

quantidadeAliens = personagens['species'] == 'Alien'
print(f'3. Há {len(personagens[quantidadeAliens])} personagens alienigenas.\n')

alien_condicao = personagens['species'] == 'Alien'
tiposdealienQnt = personagens.loc[alien_condicao]
x = tiposdealienQnt['type'].value_counts()
numero_tipos_alienigena = x.shape
print(f'4) Há {numero_tipos_alienigena[0]} tipos de alienígenas diferentes.\n')

alien_condicao = personagens['species'] == 'Alien'
alien_df = personagens.loc[alien_condicao]
numero_aliens, coluna = alien_df.shape

alien_homem_condicao = alien_df['gender'] == 'Male'
alien_homem_df = alien_df.loc[alien_homem_condicao]
numero_homem_aliens, coluna = alien_homem_df.shape

alien_mulher_condicao = alien_df['gender'] == 'Female'
alien_mulher_df = alien_df.loc[alien_mulher_condicao]
numero_mulher_aliens, coluna = alien_mulher_df.shape

print(f'5) Há {numero_homem_aliens} homens e {numero_mulher_aliens} mulheres alienígenas.\n')

crocubot_condicao = personagens['name'] == 'Crocubot'
crocubot = personagens.loc[crocubot_condicao]
episodio = crocubot['episode']
episodio = episodio[80][0]
episodio = episodio.split('/')
episodio = int(episodio[-1])

print(f'6) O personagem Crocubot aparece no episódio {episodio}.\n')

terraquios_condicao = personagens['location'] == 'Earth'
terraquios = personagens.loc[terraquios_condicao]
coluna, terraquios_qnt = terraquios.shape

print(f'7) Há {terraquios_qnt} personagens que estão em planetas chamado Earth.\n')

alien_condicao = personagens['species'] == 'Alien'
alien = personagens.loc[alien_condicao]
numero_earth, coluna= alien.shape

print(f'8) Os personagens da espécie alienígena aparecem em {numero_earth} episódios diferentes.\n')