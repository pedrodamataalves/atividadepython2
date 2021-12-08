import pandas as pd

personagens = pd.read_json('character.json')
episodios = pd.read_json('episode.json')

quantidadeDePersonagens = personagens['id'].count()
print("1) Há", quantidadeDePersonagens, "personagens nessa lista.\n")