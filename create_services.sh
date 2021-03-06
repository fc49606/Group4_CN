#gcloud auth login

gcloud container clusters create gk-cluster --num-nodes 3 --machine-type n1-standard-4 --zone europe-west2-b

cd src

gcloud iam service-accounts keys create key.json --iam-account cn-projeto@cn2021-kubernetes-colab.iam.gserviceaccount.com
kubectl create secret generic sa-secret --from-file=service_account.json=key.json
kubectl create secret generic secret-db --from-literal=host=127.0.0.1:5432 --from-literal=username=postgres --from-literal=password=root --from-literal=database=movies 
kubectl create secret generic secret-dbstream --from-literal=host=127.0.0.1:5432 --from-literal=username=postgres --from-literal=password=root --from-literal=database=movies_streaming_plataform

cd microservice_budget
gcloud builds submit --tag eu.gcr.io/cn2021-kubernetes-colab/microservice-budget
kubectl apply -f budget-with-proxy.yaml
kubectl expose deployment budget --type LoadBalancer --port 80 --target-port 8080
cd .. 

cd microservice_movies
gcloud builds submit --tag eu.gcr.io/cn2021-kubernetes-colab/microservice-movies
kubectl create -f movies-with-proxy.yaml
kubectl expose deployment movie --type LoadBalancer --port 80 --target-port 8080
cd ..

cd microservice_rating
gcloud builds submit --tag eu.gcr.io/cn2021-kubernetes-colab/microservice-rating
kubectl create -f rating-with-proxy.yaml
kubectl expose deployment rating --type LoadBalancer --port 80 --target-port 8080
cd ..

cd microservice_revenue
gcloud builds submit --tag eu.gcr.io/cn2021-kubernetes-colab/microservice-revenue
kubectl create -f revenue-with-proxy.yaml
kubectl expose deployment revenue --type LoadBalancer --port 80 --target-port 8080
cd ..

kubectl create -f ingress.yaml

kubectl get service

# kubectl autoscale deployment budget --cpu-percent=80 --min=1 --max=5
# kubectl autoscale deployment movie --cpu-percent=80 --min=1 --max=5
# kubectl autoscale deployment rating --cpu-percent=80 --min=1 --max=5
# kubectl autoscale deployment revenue --cpu-percent=80 --min=1 --max=5