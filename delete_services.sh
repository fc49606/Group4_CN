kubectl delete service movie
kubectl delete service budget 
kubectl delete service revenue 
kubectl delete service rating 
gcloud container clusters delete gk-cluster
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-movies --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-budget --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-revenue --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-ratings --force-delete-tags --quiet