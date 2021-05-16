import pandas as pd

stream = pd.read_csv("C:/Users/dani-/Desktop/Mestrado/1ºAno/2ºSemestre/Computação_em_Nuvem/projeto velho/teste_spark/MoviesOnStreamingPlatforms_updated.csv", encoding='latin1', index_col=0)

stream.drop(columns=['ID', 'Rotten Tomatoes', 'Age', 'Type'], inplace= True)

stream = stream.rename(columns={'Prime Video': 'Prime_Video', 'Disney+': 'Disney_plus'})

#stream["Prime_Video"] = stream["Prime Video"]

df = stream.to_csv('C:/Users/dani-/Desktop/Mestrado/1ºAno/2ºSemestre/Computação_em_Nuvem/projeto velho/teste_spark/MoviesOnStreamingPlatforms_clean.csv',index=False)