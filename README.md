# Group4_CN


Instruction to build and run the aplication

## Create and Populate Postgres tables

First start by downloading the MoviesOnStreamingPlatforms_updated.csv [dataset](https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney)
From this [dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv) download the movies_metadata.csv and the ratings.csv
Once finished the download, make sure to put the files on the Create_and_Populate_Database folder:

To organize the data, first run the following files:

    ```python3 AUXILIAR.py
    ```
    ```python3 AUXILIAR2.py
    ```
    ```python3 AUXILIAR3.py
    ```

Now to create and populate our data run the scripts (install any modules missing using python -m pip install SOMEPACKAGE):
NOTE: run all the files by this order 

    ```python3 create_movies_bd.py
    ```
    ```python3 create_streaming_bd.py
    ```
    ```python3 populate_movies_metadata.py
    ```
    ```python3 populate_movies_ratings.py
    ```
    ```python3 populate_movies_streaming_plataforms.py
    ```

This operation should take several minutes to complete.
