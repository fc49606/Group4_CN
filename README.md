# Group4_CN

Instruction to build and run the aplication

## Participantes
    Daniel Ferrão nº49606
    Jaime Mendes nº55919
    Luís Gonçalves nº55742

## 1 - Create and Populate Postgres tables

First start by downloading the MoviesOnStreamingPlatforms_updated.csv [dataset](https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney)
From this [dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv) download the movies_metadata.csv and the ratings.csv
Once finished the download, make sure to put the files on the Create_and_Populate_Database folder:

To organize the data, and to create and populate our data run the following line (install any modules missing using python -m pip install SOMEPACKAGE):

    ./create_and_populate.sh
    
This operation should take several minutes to complete.

#
## 2 - Create the GKE cluster and Deploy the microservices

To create the GKE cluster as well the implementation of the microservices run the following line:

    ./create_services.sh

Note: this may take a few minutes to complete 

This will create all the necessary secrets to allow the connection between the database and the microservices.
 
### 2.1 - Important note

On every XXX-with-proxy.yaml make sure that you have your project-id and the id of your SQL Database

#
## 3 - Create Dataproc and Deploy the spark microservices

To create the dataproc and to deploy the two aditional services run the following line:

    ./spark_services.sh

To see the list of all jobs in Dataproc's 'us-central1' region, run:

    gcloud dataproc jobs list --region=us-central1

To see a list of all active jobs in cluster 'mycluster' with a label env=staging located in 'us-central1', run:

    gcloud dataproc jobs list --region=us-central1  --filter='status.state = ACTIVE AND
    placement.clusterName = 'mycluster' AND labels.env = staging'

To see the output from a dataproc job, run:

    gcloud dataproc jobs wait <JOB-ID> --project cn2021-kubernetes-colab --region us-central1

#
## 4 - Delete the microservices 

To delete the cluster and all the microservices on that cluster as well deleting the dataproc run:
    
    ./delete_services.sh
    

### 4.1 - Delete the dataproc jobs

To delete the spark jobs run the line;

    gcloud dataproc jobs delete <JOB-ID>