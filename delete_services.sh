kubectl delete service movie
kubectl delete service budget 
kubectl delete service revenue 
kubectl delete service rating 
kubectl delete ing ingress -n default

cd microservice_budget
kubectl delete -f budget-with-proxy.yaml
cd ..

cd microservice_movies
kubectl delete -f movie-with-proxy.yaml
cd ..

cd microservice_rating
kubectl delete -f rating-with-proxy.yaml
cd ..

cd microservice_revenue
kubectl delete -f revenue-with-proxy.yaml
cd ..

gcloud container clusters delete gk-cluster

gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-movies --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-budget --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-revenue --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-rating --force-delete-tags --quiet
