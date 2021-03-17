'''
Código usado para criar o scrip SQL para criar a base de dados
'''

import pandas as pd

# Import CSV
#with open("movies_metadata.txt","w+", encoding="utf-8") as a:
#    data = pd.read_csv(r'movies_metadata.csv', low_memory=False)
#    data = data.drop(['adult','belongs_to_collection','homepage','imdb_id','overview','popularity','poster_path','production_companies','production_countries','spoken_languages','status','tagline','video','vote_average','vote_count'], axis=1)
    # Create Table
#    a.write('USE DatabaseGrupo4;\n')
#    a.write('CREATE TABLE movies_metadata (id bigint, budget bigint, original_language varchar(420), release_date varchar(420), revenue bigint, runtime bigint, title varchar(420));\n')
    #data = data[(data['budget'].isnotnull())]
    #data = data.apply (pd.to_string, errors='coerce')

#    data = data.dropna()
    # Insert DataFrame to Table
#    for index, row in data.iterrows():
#        a.write("INSERT INTO movies_metadata (id, budget, original_language, release_date, revenue, runtime, title) VALUES (\"" + str(row['id']) + "\",\"" + str(row['budget']) + "\",\"" + str(row['original_language']) + "\",\"" + str(row['release_date']) + "\",\"" + str(row['revenue']) + "\",\"" + str(row['runtime']) + "\",\"" + str(row['title']) + "\");\n")

# Import CSV
with open("MoviesOnStreamingPlatforms.txt","w+", encoding="utf-8") as b:
    data2 = pd.read_excel(r'MoviesOnStreamingPlatforms_updated2.xlsx')
    b.write('USE DatabaseGrupo4;\n')
    data2 = data2.drop(['Age','Rotten Tomatoes'], axis=1)
    # Create Table
    data2 = data2.dropna()
    b.write('CREATE TABLE MoviesOnStreamingPlatforms (ID bigint, Title varchar(4200), Year bigint, IMDb bigint, Netflix bigint, Hulu bigint, Prime_Video bigint, DisneyPlus bigint, Directors varchar(4200), Genres varchar(4200), Country varchar(4200), Language varchar(4200), Runtime bigint);\n')
    # Insert DataFrame to Table
    for index, row in data2.iterrows():
        b.write("INSERT INTO MoviesOnStreamingPlatforms (ID, Title, Year, IMDb, Netflix, Hulu, Prime_Video, DisneyPlus, Directors, Genres, Country, Language, Runtime) VALUES (\"" + str(row['ID']) + "\",\"" + str(row['Title']) + "\",\"" + str(row['Year']) + "\",\"" + str(row['IMDb']) + "\",\"" + str(row['Netflix']) + "\",\"" + str(row['Hulu']) + "\",\"" + str(row['Prime Video']) + "\",\"" + str(row['Disney+']) + "\",\"" + str(row['Directors']) + "\",\"" + str(row['Genres']) + "\",\"" + str(row['Country']) + "\",\"" + str(row['Language']) + "\",\"" + str(row['Runtime']) + "\");\n")

# Import CSV
#with open("ratings.txt","w+", encoding="utf-8") as c:
#    data3 = pd.read_csv(r'ratings.csv', low_memory=False)

    # Create Table
#    c.write('CREATE TABLE ratings (movieId int10, rating int10);\n')

    # Insert DataFrame to Table
#    for index, row in data3.iterrows():
#       c.write("INSERT INTO ratings (movieId, rating) VALUES (\"" + str(row['movieId']) + "\",\"" + str(row['rating']) + "\");\n")