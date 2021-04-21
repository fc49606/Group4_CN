## Group4_CN

Instruction to build and run the aplication

## Create and Populate Postgres tables

First start by downloading the MoviesOnStreamingPlatforms_updated.csv [dataset](https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney)
From this [dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv) download the movies_metadata.csv and the ratings.csv
Once finished the download, make sure to put the files on the Create_and_Populate_Database folder:

To organize the data, and to create and populate our data run the following line (install any modules missing using python -m pip install SOMEPACKAGE):

    ```./create_and_populate.sh
    ```
This operation should take several minutes to complete.

## Create the clusters

Create the GKE cluster, you can do the next step in parallel if you so desire:

    ```gcloud container clusters create gk-cluster --num-nodes 1 --machine-type n1-standard-1 --zone europe-west2-b
    ```
## Deploy the microservices to the cluster
    
    ```./create_services.sh
    ```
    
## Delete the microservices 
    
    ```./delete_services.sh
    ```
