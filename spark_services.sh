gcloud dataproc clusters create spark --project=cn2021-kubernetes-colab --region=us-central1 --single-node

cd src/spark
gcloud dataproc jobs submit pyspark spark_usecase1.py --cluster=spark --region=us-central1 
gcloud dataproc jobs submit pyspark spark_usecase2.py --cluster=spark --region=us-central1