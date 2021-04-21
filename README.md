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
Note: this may take a few minutes to complete 

After you created a cluster, then go to IAM ADMIN, service acount and finaly create a account. Create a account with two roles papeis (cliente do Cloud SQL e Editor).
Go to keys and create one e then download ir as .json, name it key and place it on the project folder.

To create a secret run:
    ```gcloud iam service-accounts keys create key.json --iam-account cn-projeto@cn2021-kubernetes-colab.iam.gserviceaccount.com
    ```
and
    ```kubectl create secret generic sa-secret --from-file=service_account.json=key.json
    ```
 
##Important note

On every XXX-with-proxy.yaml maku sure that you have your project-id and the id of your SQL Database

## Deploy the microservices

To deploy the microservices to a cluster run:
    ```./create_services.sh
    ```
    
Note: this may take a few minutes to complete
    
## Delete the microservices 

To delete all the microservices on a cluster run:
    ```./delete_services.sh
    ```
