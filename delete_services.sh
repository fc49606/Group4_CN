gcloud container clusters delete gk-cluster --region=europe-west2-b

gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-movies --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-budget --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-revenue --force-delete-tags --quiet
gcloud container images delete eu.gcr.io/cn2021-kubernetes-colab/microservice-rating --force-delete-tags --quiet

gcloud dataproc clusters delete spark --region=us-central1
